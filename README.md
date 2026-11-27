# Branch-native agent infrastructure (BNAI)

**A reference specification for persistent, composable agent engineering.**

Current candidate: **v0.0.0.3** · License: [PolyForm Strict 1.0.0](LICENSE) · [Scope and permissions](NOTICE.md)

BNAI describes how to install reusable agent-oriented engineering capabilities into durable version-control branches so compatible AI agents can recover project context, perform bounded operations, and produce revision-bound evidence. It is an architectural methodology and reference specification, not a model, agent harness, orchestration service, certification scheme or mandatory product.

Converium is an independent ecosystem of example products. BNAI defines the architecture; it does not run or manage those products. This repository is the canonical reference, not a BNAI adopter installation. Do not install a permanent BNAI branch into itself or into a project merely to consult these docs.

## Start here

| Want to… | Read |
|---|---|
| Understand the category | [Definition](docs/definition.md) |
| Choose a combination of layers | [Architecture](docs/architecture.md) · [Composition](docs/composition.md) |
| Build a persistent project branch | [Layer 1](docs/layers/01-persistent-branch.md) |
| Design agent identity and authority | [Layer 2](docs/layers/02-agent-contract.md) |
| Add skills or plugins | [Layer 3](docs/layers/03-skills-plugins.md) |
| Build an LLM-first CLI | [Layer 4](docs/layers/04-cli.md) |
| Add MCP connectivity | [Layer 5](docs/layers/05-mcp.md) |
| Operate without a PC or CI runner | [Execution profiles](docs/execution.md) |
| Ask an agent to review a project | [AGENTS.md](AGENTS.md) · [WORKFLOW.md](WORKFLOW.md) |
| Understand the rules | [STANDARD.md](STANDARD.md) · [GATE.md](GATE.md) · [Principles](docs/principles.md) |
| Compare actual implementations | [Examples](examples/README.md) · [Primary sources](docs/sources.md) |

## BNAI Mode

Tell a GitHub-capable agent: “Use BNAI to review OWNER/REPO. Read the BNAI main branch AGENTS.md at an exact revision and follow its review workflow. Read-only.”

The alias `$BNAI` expresses the same intent when the host recognizes it or the user defines it. It is not a registered universal skill command. No installation is needed to consult this reference. Say “Turn BNAI off” to end the voluntary role in the current session. A host must be able to read the reference and target; activation does not grant tools, permissions or persistence.

## Execution

Standard public GitHub-hosted Actions runners are the primary reference qualification profile; private, self-hosted, other cloud, local and connector-only approaches are possible. Choose the minimum safe permissions for each operation. No mandatory AI provider, paid compute, runner or local PC.

## Project status

A small, evolving reference repository. [Contribute](CONTRIBUTING.md) · [Security](SECURITY.md) · [Version history](CHANGELOG.md). No claim of exclusive ownership of architectural ideas or certification of the examples. Documentation CI is not live agent qualification.
