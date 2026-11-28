# Design methodology

BNAI is a way to design reusable project-bound engineering infrastructure, not a way to build or host an AI model. Begin with the owner's engineering problem, not an agent harness or a list of tools. This guide connects the existing [definition](definition.md), [architecture](architecture.md), [composition](composition.md) and [lifecycle](lifecycle-guide.md) into a usable design process. It is guidance, not a mandatory schema or runtime.

## Design from the problem

| Step | Decision | Record |
|---|---|---|
| 1. Define the job | What repeatable engineering work needs to survive a session? What is explicitly out of scope? | Purpose, target project, representative task and success criteria |
| 2. Establish the durable substrate | Which dedicated branch holds reusable capabilities and adopter-specific state? How are source and state separated? | Repository/ref, source pin, installation identity, state location, evidence path |
| 3. Choose the smallest composition | Which optional layers solve actual needs? | Selected layers, reasons, omitted layers and alternatives |
| 4. Bind authority and interfaces | Who authorizes reads, writes, execution and integration? How are operations discovered and constrained? | Authority boundary, inputs, effects, errors, permitted interfaces and revision guards |
| 5. Choose execution and evidence | Where can each operation safely run, and how is its outcome demonstrated? | Host/compute profile, tests, receipt requirements, privacy and cost constraints |
| 6. Plan recovery and evolution | How does a fresh session find state? How are interrupted operations, upgrades and retirement handled? | Recovery path, compatibility boundary, handoff and owner decisions |

If any essential responsibility cannot be satisfied, record a gap rather than imply a full installation. Use [Layer 1](layers/01-persistent-branch.md) for the substrate, the [optional layer guides](README.md#how-to-guides) for selected interfaces and the [ten pairwise contracts](composition.md#all-ten-pairwise-interaction-contracts) when selected layers interact. Do not require all layers.

## Separate reasoning from execution

| Responsibility | Suitable component |
|---|---|
| Understand intent, select operations, interpret results | Existing capable agent and its host |
| Persist installation identity, scoped state, reusable capabilities and evidence | Dedicated branch (Layer 1) |
| Explain role, boundaries and procedures | Minimal recoverable instructions or optional dedicated contract |
| Provide deterministic work | Authorized repository operations, optional CLI or MCP, or existing tools |
| Run mechanical tests | Standard public GitHub-hosted runners when suitable; other approved profiles as needed |
| Decide integration and scope | Human owner |

The agent's inference does not need to run on the mechanical CI runner. A read-only architecture assessment can be performed without a runner. A runner's green result does not prove agent understanding. See [execution profiles](execution.md).

## Worked design example

Illustrative design, not an installed or tested product: an owner wants a reusable repository documentation audit. The agent should recover prior audit results and inspect a pinned revision in a new session.

- Start with Layer 1: dedicated long-lived branch, discoverable instructions, target/source pins, adopter-scoped audit records and evidence links.
- Use authorized read-only repository operations to inspect documents. Do not require a CLI, skill, MCP server or a dedicated contract suite simply because they exist as architectural options.
- Add Layer 2 only if a separate contract is useful for recurring role, authority and handoff responsibilities; add Layer 4 if deterministic link checking needs a discoverable command. Those are independent decisions.
- Use existing public CI for an authorized deterministic check; retain actual checkout, run and outcome. Keep assessment findings separate from test results.
- Persist the last verified revision and unresolved findings. On a fresh session, re-pin current state, compare the previous receipt and refresh affected conclusions. Any write or integration requires explicit authority.

The proposed design is not proof of installation, agent compatibility or execution.

## Development and evidence stages

| Stage | Objective | Evidence |
|---|---|---|
| Development | Improve architecture and implementation guidance in bounded checkpoints | Exact changes, source review, applicable mechanical regression checks |
| Exploratory review | Discover ambiguous instructions, missing responsibilities and usability gaps | Actual scoped feedback with source pins and limitations; same-agent vs external distinguished |
| Formal qualification | Demonstrate selected mature capabilities on actual hosts or installations | Applicable journey assertions and real transcripts, traces or execution receipts |

Exploratory feedback is not a certification gate for every development checkpoint. Select formal qualification only when the owner agrees the relevant capability is sufficiently mature, the target and scope are defined, and the evidence can be observed. Never relabel blocked or unrun tests as passing. Preserve previous evidence, defer unresolved qualification explicitly and revalidate affected claims when scope or revisions change. No automatic maturity claim or mandatory model, harness, runtime or paid compute follows from these stages.

See [acceptance gates](../GATE.md), [qualification journeys](qualification-journeys.md) and [principles](principles.md).
