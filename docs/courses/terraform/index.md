# Terraform on Microsoft Azure

<div class="grid" markdown>

:octicons-calendar-24: **2 days** · 9:00–16:00
:octicons-mortar-board-24: **Beginner – Intermediate**
:octicons-beaker-24: **12 hands-on labs**
:octicons-globe-24: on-site or remote · English / Polish

</div>

Build Azure infrastructure the way production teams do: **Terraform 1.17** with **azurerm 5** and **AzAPI 2**. Participants take *GreenGrid*, an energy start-up, from portal clicks to tested, reviewed and automated infrastructure as code – remote state with Entra ID, refactoring with `moved`, modules, import and drift, `terraform test` with mocked providers, secrets that never reach the state, managed identities and CI/CD pipelines without stored secrets.

[:octicons-beaker-24: Go to the labs](labs/index.md){ .md-button .md-button--primary }
[:material-github: Lab repository](https://github.com/Think-Cube/terraform-azure-labs){ .md-button }

## Who it's for

Cloud and DevOps engineers, administrators and developers who provision or maintain Azure resources and want them reproducible and reviewable.

**Prerequisites:** Azure basics (subscriptions, resource groups, networking), a terminal, Git.

## What you will be able to do

- Write, plan and apply Terraform for Azure – and read a plan before it hurts
- Enforce naming, tagging and input rules with **variables, validations and locals**
- Keep **state** in Azure Storage with Entra ID, locking and versioning
- Use **count, for_each, lifecycle** and refactor safely with **moved** blocks
- Generate configuration with **complex types, for expressions and dynamic blocks**
- Build and version **modules**, use **Azure Verified Modules**
- Adopt existing resources with **import** blocks, handle **drift**, use **removed**
- Test without Azure: **terraform test** with mocked providers, **tflint**, check blocks
- Reach every Azure feature with **AzAPI 2.x**
- Keep secrets out of the state with **ephemeral values and write-only attributes**, use **managed identities**
- Run Terraform in **GitHub Actions** or **Azure DevOps** with OIDC – plan on pull requests, apply after approval

## Agenda

=== "Day 1 – Foundations"

    | Topic | Lab |
    |---|---|
    | IaC, Terraform architecture, providers, authentication | [LAB01](labs/LAB01-first-deployment.md) |
    | Variables, validations, locals, outputs | [LAB02](labs/LAB02-variables-locals.md) |
    | State and remote backends | [LAB03](labs/LAB03-remote-state.md) |
    | Meta-arguments and `moved` | [LAB04](labs/LAB04-meta-arguments.md) |
    | Expressions and dynamic blocks | [LAB05](labs/LAB05-expressions-dynamic.md) |
    | Modules | [LAB06](labs/LAB06-modules.md) |

=== "Day 2 – Production-ready"

    | Topic | Lab |
    |---|---|
    | Import, drift and `removed` | [LAB07](labs/LAB07-import-drift.md) |
    | Testing and code quality | [LAB08](labs/LAB08-testing-quality.md) |
    | AzAPI – the whole Azure API | [LAB09](labs/LAB09-azapi.md) |
    | Secrets and managed identities | [LAB10](labs/LAB10-secrets-identity.md) |
    | CI/CD with OIDC: GitHub Actions or Azure DevOps | [LAB11](labs/LAB11-cicd.md) |
    | Break-fix challenge | [LAB12](labs/LAB12-break-fix.md) |

## Environment

Participants share one Azure subscription, each with a personal prefix; a terminal with Terraform and the Azure CLI (or Azure Cloud Shell) is all they need. Reference solutions for every lab come with the repository – anyone who falls behind catches up with `./bin/catchup <N>`.

## Book this training

[Get in touch :octicons-arrow-right-24:](https://thinkcube.dev){ .md-button .md-button--primary }
