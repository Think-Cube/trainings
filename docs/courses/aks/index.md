# Kubernetes on Microsoft Azure (AKS)

<div class="grid" markdown>

:octicons-calendar-24: **3 days** · 9:00–16:00
:octicons-mortar-board-24: **Intermediate**
:octicons-beaker-24: **15 hands-on labs**
:octicons-globe-24: on-site or remote · English / Polish

</div>

Build, secure and operate a production-style platform on **Azure Kubernetes Service**. Participants create one cluster on day one and extend it lab by lab – networking, ingress with the Gateway API, TLS, identity, secrets, storage, monitoring, GitOps and CI/CD – ending with a troubleshooting challenge.

[:octicons-beaker-24: Go to the labs](labs/index.md){ .md-button .md-button--primary }
[:material-github: Lab repository](https://github.com/Think-Cube/aks-labs){ .md-button }

## Who it's for

DevOps and platform engineers, cloud architects and developers who run – or are about to run – workloads on AKS.

**Prerequisites:** basic Kubernetes (pods, deployments, services), Linux shell, an Azure subscription with *Owner* rights on a resource group and quota for ~8 vCPUs.

## What you will be able to do

- Design an AKS cluster: tiers, versions, node pools, Azure CNI Overlay with Cilium
- Expose applications with **Gateway API** – App Routing and Application Gateway for Containers – with automatic **TLS**
- Lock down traffic with **network policies** and access with **Entra ID**, Azure RBAC and no local accounts
- Give workloads secretless access to Azure with **Workload Identity** and **Key Vault**
- Run stateful workloads on Azure Disk and Azure Files
- Observe and scale: Container insights, managed Prometheus, HPA, cluster autoscaler
- Deliver changes with **GitOps (Flux)** and **CI/CD pipelines** in Azure DevOps or GitHub Actions
- Troubleshoot the most common pod, network and platform problems

## Agenda

=== "Day 1 – Containers, AKS & networking"

    | Topic | Lab |
    |---|---|
    | Containers, images, Azure Container Registry | [LAB01](labs/LAB01-containers-acr.md) |
    | AKS overview: tiers, versions, capacity, node OS | |
    | Creating clusters with the CLI and IaC | [LAB02](labs/LAB02-create-aks.md) |
    | Network architecture: CNI Overlay, Cilium, API server access | |
    | Services, Azure Load Balancer, egress | [LAB03](labs/LAB03-services-load-balancers.md) |

=== "Day 2 – Ingress, security & identity"

    | Topic | Lab |
    |---|---|
    | Ingress in 2026: Gateway API and App Routing | [LAB04](labs/LAB04-gateway-api.md) |
    | TLS with cert-manager | [LAB05](labs/LAB05-tls-cert-manager.md) |
    | Application Gateway for Containers | [LAB06](labs/LAB06-app-gateway-for-containers.md) |
    | Network policies, Pod Security, Azure Policy, Defender | [LAB07](labs/LAB07-network-policies.md) |
    | Kubeconfig, Kubernetes RBAC | [LAB08](labs/LAB08-kubeconfig-users-rbac.md) |
    | Entra ID, Azure RBAC, local accounts | [LAB09](labs/LAB09-entra-id-azure-rbac.md) |
    | Workload Identity and Key Vault | [LAB10](labs/LAB10-workload-identity-keyvault.md) |

=== "Day 3 – Operations & delivery"

    | Topic | Lab |
    |---|---|
    | Storage with CSI drivers | [LAB11](labs/LAB11-storage.md) |
    | Monitoring, logging, autoscaling | [LAB12](labs/LAB12-monitoring-autoscaling.md) |
    | Upgrades, high availability, disaster recovery, migration | |
    | GitOps with Flux | [LAB13](labs/LAB13-gitops-flux.md) |
    | CI/CD with Helm | [LAB14](labs/LAB14-cicd-pipeline.md) |
    | Troubleshooting challenge | [LAB15](labs/LAB15-troubleshooting.md) |

## Environment

Labs run in **Azure Cloud Shell** – no local installation needed. One cluster (2–3 small nodes) is created in LAB02 and reused until the end; stopping it overnight keeps costs to a few euros per day.

## Book this training

[Get in touch :octicons-arrow-right-24:](https://thinkcube.dev){ .md-button .md-button--primary }
