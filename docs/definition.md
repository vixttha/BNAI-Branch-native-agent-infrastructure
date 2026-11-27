# Definition and boundaries

A BNAI installation is a reusable engineering environment installed in a long-lived, separately identifiable version-control branch associated with an adopter project. It must supply (1) recoverable product identity and instructions, (2) versioned capabilities or mechanical procedures, (3) durable adopter-scoped state or references to it, and (4) a verifiable execution and evidence path. Authority and target repository/revision must be explicit. Source distribution and adopter instances are distinct; adoption must not copy unrelated adopter state.

A branch is durable by lifecycle policy, not immutable. Updates are allowed with provenance and conflict controls. GitHub is the first reference platform, not the definition of the category.

## Distinctions

| Concept | Distinction |
|---|---|
| Agent harness | Hosts the LLM and tools; BNAI provides a project-bound engineering environment. |
| AGENTS.md | Instructions alone do not supply mechanical capability or durable state. |
| Agent Skill | Reusable instructions and optional resources; does not by itself establish a project installation. |
| Plugin | Packages capabilities for a host; not intrinsically branch-native. |
| CLI | Mechanical command interface; can work without a model. |
| MCP | Standard protocol for context exchange and tools, not a model, permission grant or persistence guarantee. |
| CI | Runs jobs; does not by itself supply agent identity or state. |
| Git worktree / short-lived feature branch | Isolates edits; not necessarily a durable reusable specialist installation. |

## Vocabulary

Product: reusable engineering capability. Installation: adopter-specific branch and its state. Primary skill: role and discovery entry point. Capability: versioned operation with declared effects. Receipt: revision-bound result evidence. Synchronization: resolve identity, authority, capabilities, state and evidence before sensitive work. Qualification: scoped observed tests, never inferred from a name or README.

A product may be a component example without meeting the full installation definition. No claims that BNAI is a novel invention or established industry term are made. The examples are evidence of related implementations, not proof of market adoption.
