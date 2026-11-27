# Layer composition

Layer 1 is the substrate; choose any subset of Layers 2–5. All sixteen configurations are design possibilities, not certified implementations. An omitted optional layer is not a defect. If a needed operation lacks an authorized interface or environment, report it as unavailable rather than assume another layer exists. Every combination must still preserve minimum identity, provenance, authority, state and evidence.

## All Layer-1 compositions

| Composition | Optional interfaces present |
|---|---|
| 1 | None; branch and authorized repository operations only |
| 1 + 2 | Agent operating contract |
| 1 + 3 | Skills and plugins |
| 1 + 2 + 3 | Agent operating contract; Skills and plugins |
| 1 + 4 | LLM-first CLI |
| 1 + 2 + 4 | Agent operating contract; LLM-first CLI |
| 1 + 3 + 4 | Skills and plugins; LLM-first CLI |
| 1 + 2 + 3 + 4 | Agent operating contract; Skills and plugins; LLM-first CLI |
| 1 + 5 | MCP connectivity |
| 1 + 2 + 5 | Agent operating contract; MCP connectivity |
| 1 + 3 + 5 | Skills and plugins; MCP connectivity |
| 1 + 2 + 3 + 5 | Agent operating contract; Skills and plugins; MCP connectivity |
| 1 + 4 + 5 | LLM-first CLI; MCP connectivity |
| 1 + 2 + 4 + 5 | Agent operating contract; LLM-first CLI; MCP connectivity |
| 1 + 3 + 4 + 5 | Skills and plugins; LLM-first CLI; MCP connectivity |
| 1 + 2 + 3 + 4 + 5 | Agent operating contract; Skills and plugins; LLM-first CLI; MCP connectivity |

Examples: 1 + 3 can use a skill that reads the branch through a GitHub connector, without a CLI, MCP or separate AOC suite. 1 + 2 + 4 uses a contract and CLI, without skills or MCP. 1 + 5 can expose branch operations through MCP with no CLI. A subset without Layer 1 can be useful but is not itself a complete branch-native installation.

## All ten pairwise interaction contracts

| Layers | Interaction |
|---|---|
| 1 ↔ 2 | Contract pins installation, maps rules and recovery state; branch preserves contract and evidence. |
| 1 ↔ 3 | Skill resolves trusted branch and reads minimal identity/authority; no required separate contract suite. |
| 1 ↔ 4 | CLI loads exact installation/state revision; returns bounded results, rejects stale writes. |
| 1 ↔ 5 | MCP resolves authorized installation per request; tools/resources expose scoped branch data and operations. |
| 2 ↔ 3 | Skill delegates to installation rules; detect conflicts, never promote skill text over authority. |
| 2 ↔ 4 | Contract explains commands and gates; CLI mechanically checks scope, inputs and outcomes. |
| 2 ↔ 5 | MCP exposes trusted contract and current state; host controls tool approvals. |
| 3 ↔ 4 | Skill selects versioned CLI commands using schema; structured outputs drive next steps. |
| 3 ↔ 5 | Skill chooses advertised MCP tools and resources; fallback does not broaden authority. |
| 4 ↔ 5 | Shared validated core preferred; if MCP calls CLI, use fixed argv/schema, bounds and structured errors. |

Each selected pair uses these contracts where they interact; do not build unnecessary adapters. Resolve source and state separately; enforce authorization in mechanical operations, never via instructions alone. Validate the selected interfaces with positive, denied, stale and interrupted requests where applicable.

## Choosing a configuration
Start with the [Layer 1 guide](layers/01-persistent-branch.md). Add [Layer 2](layers/02-agent-contract.md) for repeatable identity and operating rules; [Layer 3](layers/03-skills-plugins.md) for portable specialist procedures; [Layer 4](layers/04-cli.md) for mechanical shell automation; [Layer 5](layers/05-mcp.md) for structured host connectivity. Select an [execution profile](execution.md) independently.
