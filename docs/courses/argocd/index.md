# GitOps with Argo CD

<div class="grid" markdown>

:octicons-calendar-24: **2 days** · 9:00–16:00
:octicons-mortar-board-24: **Intermediate**
:octicons-beaker-24: **12 hands-on labs**
:octicons-globe-24: on-site or remote · English / Polish

</div>

Continuous delivery to Kubernetes the GitOps way with **Argo CD 3.5**. Participants take *ParcelPal*, a parcel-delivery startup, from `kubectl apply` on laptops to a platform driven entirely by Git – applications, Helm and Kustomize, projects and RBAC, secrets, sync waves and hooks, app of apps and ApplicationSets, multi-cluster, notifications, Image Updater and progressive delivery with Argo Rollouts – ending with a break-fix challenge.

[:octicons-beaker-24: Go to the labs](labs/index.md){ .md-button .md-button--primary }
[:material-github: Lab repository](https://github.com/Think-Cube/argocd-labs){ .md-button }

## Who it's for

Platform and DevOps engineers, SREs and developers who deploy to Kubernetes and want reproducible, auditable releases.

**Prerequisites:** Kubernetes basics (pods, deployments, services), Git, Linux shell. Helm or Kustomize experience helps.

## What you will be able to do

- Install Argo CD with Helm and work with the UI, CLI and API
- Deploy applications from Git and understand **sync status vs. health**
- Automate: **auto-sync, self-heal, prune**, webhooks and tracking strategies
- Use **Helm, Kustomize** and **multiple sources** per environment
- Set guard rails with **projects, RBAC** and CI tokens
- Connect private repositories and keep secrets in Git safely with **Sealed Secrets**
- Order deployments with **sync waves and hooks**, tune diffs
- Bootstrap everything with **app of apps** and generate apps with **ApplicationSets**
- Manage **many clusters** from one Argo CD
- Notify teams, bump images automatically with **Image Updater** and release with **Argo Rollouts** canaries

## Agenda

=== "Day 1 – Foundations"

    | Topic | Lab |
    |---|---|
    | GitOps principles, Argo CD architecture and installation | [LAB01](labs/LAB01-install-argocd.md) |
    | Applications: create, sync, health, history | [LAB02](labs/LAB02-first-application.md) |
    | Automation: auto-sync, self-heal, prune, tracking | [LAB03](labs/LAB03-gitops-loop.md) |
    | Helm, Kustomize and multiple sources | [LAB04](labs/LAB04-helm-kustomize.md) |
    | Projects and RBAC | [LAB05](labs/LAB05-projects-rbac.md) |
    | Private repositories and secrets | [LAB06](labs/LAB06-private-repos-secrets.md) |

=== "Day 2 – Scale & automation"

    | Topic | Lab |
    |---|---|
    | Sync waves, hooks, sync options | [LAB07](labs/LAB07-sync-waves-hooks.md) |
    | App of apps and ApplicationSets | [LAB08](labs/LAB08-app-of-apps-applicationset.md) |
    | Multi-cluster management | [LAB09](labs/LAB09-multi-cluster.md) |
    | Notifications and Image Updater | [LAB10](labs/LAB10-notifications-image-updater.md) |
    | Progressive delivery with Argo Rollouts | [LAB11](labs/LAB11-progressive-delivery.md) |
    | Break-fix challenge | [LAB12](labs/LAB12-break-fix.md) |

## Environment

Labs run on one Linux VM (4 vCPU, 8 GB RAM) with Docker: two **kind** clusters and a **Gitea** server as everyone's own Git – no cloud account needed. Anyone who falls behind catches up with `./bin/lab catchup <N>`.

## Book this training

[Get in touch :octicons-arrow-right-24:](https://thinkcube.dev){ .md-button .md-button--primary }
