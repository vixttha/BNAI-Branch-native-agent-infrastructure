# Layer 3 — Skills and plugins

Purpose: package specialist task knowledge separately from installation state. Follow the [Agent Skills format](https://agentskills.io/specification): a skill directory contains SKILL.md with required name and description metadata, plus optional resources. A plugin is host-specific distribution and may bundle multiple skills and other components; neither guarantees a universal invocation alias.

Build a primary entry skill for discovery, bounded capability selection and references. Add specialist skills only for distinct tasks. Resolve branch and approved revision at runtime using authorized access. Avoid stale embedded copies, arbitrary shell execution, hidden writes and host-specific assumptions. Test actual supported packaging and invocation on each claimed host.

With Layer 1 alone, the skill can use a repository connector. With Layer 2, follow contract and authority. With Layer 4, consume command schemas and JSON results. With Layer 5, discover supported tools. Do not require a CLI or MCP if absent.

Qualify fresh session, wrong repo, wrong revision, unavailable capabilities, denial, invocation and recovery. Keep packaged skills within their own licensing and distribution permissions.
