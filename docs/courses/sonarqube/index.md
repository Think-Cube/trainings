# SonarQube for DevOps

<div class="grid" markdown>

:octicons-calendar-24: **2 days** · 9:00–16:00
:octicons-mortar-board-24: **Intermediate**
:octicons-beaker-24: **10 hands-on labs**
:octicons-globe-24: on-site or remote · English / Polish

</div>

Automated code review with **SonarQube Community Build 26.10** for *BookShelf*, a small online bookstore with a Java and a Python service. Participants take it from "nobody looks at code quality" to gated code reviews in every pipeline – scanners, tests and coverage, third-party analyzers, quality profiles and gates, Jenkins, GitHub Actions and Azure DevOps, security, the Web API and troubleshooting.

[:octicons-beaker-24: Go to the labs](labs/index.md){ .md-button .md-button--primary }
[:material-github: Lab repository](https://github.com/Think-Cube/sonarqube-labs){ .md-button }

## Who it's for

DevOps engineers, developers, team leads and QA engineers who want automated, enforceable code quality in their delivery pipelines.

**Prerequisites:** basic Git and CI/CD knowledge, Linux shell, reading Java or Python code.

## What you will be able to do

- Install and configure SonarQube with PostgreSQL in Docker
- Analyse code with the **Maven plugin** and **SonarScanner CLI**, read and triage issues
- Import **tests and coverage**, scope analyses, understand *new code*
- Bring **Bandit, Ruff, Pylint** and your own tools in with the generic issue format
- Build inherited **quality profiles** and **quality gates** that block bad releases
- Gate pipelines in **Jenkins**, **GitHub Actions** and **Azure DevOps**
- Secure SonarQube: permissions, templates, least-privilege tokens
- Automate with the **Web API**, custom rules and quality configuration as code
- Diagnose broken analyses quickly

## Agenda

=== "Day 1 – Foundations"

    | Topic | Lab |
    |---|---|
    | Code quality, the Sonar family, architecture, installation | [LAB01](labs/LAB01-environment.md) |
    | Scanners and the first analysis | [LAB02](labs/LAB02-first-analysis.md) |
    | Tests, coverage and analysis parameters | [LAB03](labs/LAB03-tests-coverage.md) |
    | Third-party analyzers and external issues | [LAB04](labs/LAB04-third-party-analyzers.md) |
    | Quality profiles and quality gates | [LAB05](labs/LAB05-profiles-gates.md) |

=== "Day 2 – DevOps integration & operations"

    | Topic | Lab |
    |---|---|
    | Jenkins pipelines with `waitForQualityGate` | [LAB06](labs/LAB06-jenkins.md) |
    | GitHub Actions and Azure DevOps | [LAB07](labs/LAB07-github-azure-devops.md) |
    | Security: permissions, tokens, findings | [LAB08](labs/LAB08-security.md) |
    | Web API, custom rules, quality as code | [LAB09](labs/LAB09-web-api-custom-rules.md) |
    | Troubleshooting break-fix | [LAB10](labs/LAB10-troubleshooting.md) |

## Environment

Labs run on one Linux VM (4 vCPU, 8 GB RAM) with **Docker Compose**: SonarQube, PostgreSQL, Jenkins and Gitea start with `./bin/lab up`. LAB07 additionally needs a GitHub account or an Azure DevOps organisation.

## Book this training

[Get in touch :octicons-arrow-right-24:](https://thinkcube.dev){ .md-button .md-button--primary }
