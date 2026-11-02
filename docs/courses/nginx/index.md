# NGINX in Practice

<div class="grid" markdown>

:octicons-calendar-24: **2 days** · 9:00–16:00
:octicons-mortar-board-24: **Beginner – Intermediate**
:octicons-beaker-24: **11 hands-on labs**
:octicons-globe-24: on-site or remote · English / Polish

</div>

Run **NGINX 1.30** as the edge of a small online shop – *PixelShop*. Participants start with one web server and grow it lab by lab into a production-style edge: reverse proxy, load balancing with failover, caching, TLS with HTTP/2 and HTTP/3, access control and rate limiting, observability, njs scripting and a Web Application Firewall – ending with a break-fix challenge.

[:octicons-beaker-24: Go to the labs](labs/index.md){ .md-button .md-button--primary }
[:material-github: Lab repository](https://github.com/Think-Cube/nginx-labs){ .md-button }

## Who it's for

System administrators, DevOps engineers and developers who deploy web applications and APIs behind NGINX – or are about to.

**Prerequisites:** Linux shell, basic HTTP (methods, headers, status codes), a little Docker.

## What you will be able to do

- Structure an NGINX configuration: server blocks, `location` matching, includes, safe reloads
- Put applications behind a **reverse proxy** – headers, timeouts, WebSockets
- **Load balance** with failover, sticky routing, DNS re-resolution and a backup server
- Speed things up with **compression**, browser caching and the **proxy cache** as a safety net
- Serve **TLS** properly – HTTP/2, **HTTP/3 (QUIC)**, HSTS, SNI
- Protect the edge: basic auth, `auth_request`, geo blocking, **rate limiting**, security headers
- Observe traffic with JSON logs, request IDs and **Prometheus** metrics
- Balance TCP/UDP with `stream`, build dynamic modules and script with **njs**
- Stop common attacks with **ModSecurity + OWASP CRS**
- Find and fix broken configurations under time pressure

## Agenda

=== "Day 1 – Core"

    | Topic | Lab |
    |---|---|
    | Architecture, configuration model, virtual hosts, location matching | [LAB01](labs/LAB01-virtual-hosts.md) |
    | Reverse proxy, headers, WebSockets | [LAB02](labs/LAB02-reverse-proxy.md) |
    | Load balancing, failover, sticky routing | [LAB03](labs/LAB03-load-balancing.md) |
    | Static content, caching, compression | [LAB04](labs/LAB04-caching-compression.md) |
    | TLS, HTTP/2, HTTP/3, ACME | [LAB05](labs/LAB05-tls-http3.md) |

=== "Day 2 – Security, operations, cloud-native"

    | Topic | Lab |
    |---|---|
    | Access control, rate limiting, security headers | [LAB06](labs/LAB06-access-control.md) |
    | Logging, request tracing, monitoring | [LAB07](labs/LAB07-logging-monitoring.md) |
    | TCP/UDP load balancing with `stream` | [LAB08](labs/LAB08-stream-tcp-udp.md) |
    | Dynamic modules and njs | [LAB09](labs/LAB09-modules-njs.md) |
    | Web Application Firewall: attack & defend | [LAB10](labs/LAB10-waf.md) |
    | NGINX in containers and Kubernetes | |
    | Break-fix challenge | [LAB11](labs/LAB11-break-fix.md) |

## Environment

Labs run on one Linux VM (Ubuntu 24.04, 2 vCPU, 4 GB RAM) with **Docker Compose** – the whole shop starts with `./bin/ngx up`. Anyone who falls behind catches up with one command (`./bin/ngx catchup <N>`), so nobody gets stuck.

## Book this training

[Get in touch :octicons-arrow-right-24:](https://thinkcube.dev){ .md-button .md-button--primary }
