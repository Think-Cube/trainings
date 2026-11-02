"""Pull lab instructions from the course repositories into docs/ and generate the catalog.

For every course in courses.yml with a `labs_repo`:
  - download the repository archive from GitHub (no git needed),
  - copy <labs_dir>/LABnn-*/README.md to docs/courses/<id>/labs/LABnn-*.md,
  - rewrite relative links/images so they point to the files on GitHub,
  - write docs/courses/<id>/labs/index.md with the list of labs.
Then docs/index.md is generated from courses.yml.
"""
import io
import pathlib
import re
import shutil
import sys
import tarfile
import urllib.request

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
LINK = re.compile(r"(!?\[[^\]]*\])\(([^)\s]+)\)")


def download(repo, branch):
    url = f"https://codeload.github.com/{repo}/tar.gz/refs/heads/{branch}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        return tarfile.open(fileobj=io.BytesIO(resp.read()), mode="r:gz")


def rewrite_links(text, repo, branch, src_dir):
    """Relative links -> GitHub URLs (files) or local pages (other labs)."""
    def fix(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"^(https?:|mailto:|#)", target):
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = (pathlib.PurePosixPath(src_dir) / path).as_posix()
        parts = []
        for p in resolved.split("/"):          # normalise ../
            if p == "..":
                parts and parts.pop()
            elif p not in ("", "."):
                parts.append(p)
        resolved = "/".join(parts)
        lab = re.match(r"^labs/(LAB\d+[^/]*)/README\.md$", resolved)
        if lab:                                  # link to another lab -> page on this site
            return f"{label}({lab.group(1)}.md{'#' + anchor if anchor else ''})"
        kind = "raw" if label.startswith("!") else "blob"
        base = f"https://github.com/{repo}/{kind}/{branch}/{resolved}"
        return f"{label}({base}{'#' + anchor if anchor else ''})"
    return LINK.sub(fix, text)


def first_heading(text, fallback):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def sync_course(course):
    repo, branch = course["labs_repo"], course.get("labs_branch", "main")
    labs_dir = course.get("labs_dir", "labs").strip("/")
    out = DOCS / "courses" / course["id"] / "labs"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    labs = []
    with download(repo, branch) as tar:
        for member in tar.getmembers():
            # archive paths look like <repo>-<branch>/labs/LAB01-x/README.md
            rel = member.name.split("/", 1)[-1]
            m = re.match(rf"^{re.escape(labs_dir)}/(LAB\d+[^/]*)/README\.md$", rel)
            if not m:
                continue
            text = tar.extractfile(member).read().decode("utf-8")
            name = m.group(1)
            text = rewrite_links(text, repo, branch, f"{labs_dir}/{name}")
            source = f"https://github.com/{repo}/tree/{branch}/{labs_dir}/{name}"
            text += f"\n\n---\n\n:material-github: Files for this lab: [{repo}/{labs_dir}/{name}]({source})\n"
            (out / f"{name}.md").write_text(text, encoding="utf-8")
            labs.append((name, first_heading(text, name)))

    labs.sort()
    course["_labs"] = labs
    lines = [f"# Labs – {course['title']}", "",
             f"All lab files live in [{repo}](https://github.com/{repo}). "
             "Clone it once and work through the labs in order – each one builds on the previous.", "",
             "```bash", f"git clone https://github.com/{repo}.git", "```", "",
             "| # | Lab |", "|---|---|"]
    for name, title in labs:
        num = re.match(r"LAB(\d+)", name).group(1)
        lines.append(f"| {num} | [{title}]({name}.md) |")
    (out / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{course['id']}: {len(labs)} labs from {repo}@{branch}")
    return len(labs)


def write_catalog(courses):
    cards = []
    for c in courses:
        if c.get("labs_repo"):
            link = f"[:octicons-arrow-right-24: Course details](courses/{c['id']}/index.md)"
        else:
            link = ":octicons-clock-24: Coming soon"
        cards.append(
            f"-   __{c['title']}__\n\n    ---\n\n    {c['summary']}\n\n"
            f"    :octicons-calendar-24: {c['duration']} · :octicons-mortar-board-24: {c['level']}\n\n"
            f"    {link}\n")
    head = (DOCS / "_index_head.md").read_text(encoding="utf-8")
    tail = (DOCS / "_index_tail.md").read_text(encoding="utf-8")
    body = '<div class="grid cards" markdown>\n\n' + "\n".join(cards) + "\n</div>\n"
    (DOCS / "index.md").write_text(head + "\n" + body + "\n" + tail, encoding="utf-8")


def write_nav(courses):
    """mkdocs.gen.yml = mkdocs.yml + generated navigation."""
    nav = [{"Home": "index.md"}]
    for c in courses:
        if not c.get("labs_repo"):
            continue
        labs = [{"Overview": f"courses/{c['id']}/labs/index.md"}]
        labs += [{title: f"courses/{c['id']}/labs/{name}.md"} for name, title in c["_labs"]]
        nav.append({c.get("nav_title", c["title"]): [
            {"About the course": f"courses/{c['id']}/index.md"},
            {"Labs": labs},
        ]})
    gen = {"INHERIT": "mkdocs.yml", "nav": nav}
    (ROOT / "mkdocs.gen.yml").write_text(
        "# generated by scripts/sync_labs.py - do not edit\n" + yaml.safe_dump(gen, sort_keys=False, allow_unicode=True),
        encoding="utf-8")


def main():
    courses = yaml.safe_load((ROOT / "courses.yml").read_text(encoding="utf-8"))["courses"]
    total = 0
    for course in courses:
        if course.get("labs_repo"):
            total += sync_course(course)
    write_catalog(courses)
    write_nav(courses)
    if total == 0:
        sys.exit("no labs synced - check courses.yml")


if __name__ == "__main__":
    main()
