# Layer 4 — LLM-first CLI

Purpose: deterministic, model-independent mechanical interfaces that humans and agents can both operate. A CLI is optional; code should not require paid inference simply to perform deterministic work.

Build against a shared validated core. Provide version/help/capability discovery, typed input, stable JSON result/error schemas, meaningful exit codes, noninteractive operation, bounded timeout/cancellation, explicit workspace and target, dry run where applicable, no implicit overwrite, stale revision checks, safe retry guidance and artifact receipts. Preserve human help. Document unsupported operations and dependencies.

With Layer 1, pin installation and state. With Layer 2, map contract and gates. With Layer 3, let skills select valid commands from documented schemas. With Layer 5, prefer shared core; if subprocess wrapping is necessary, use fixed arguments, no shell interpolation, limits and structured errors.

Qualify success, malformed input, permission denial, timeout, stale state, overwrite denial and recovery on relevant environments. See [BART issue #117](https://github.com/vixttha/Blender-Agent-Refinement-Toolkit/issues/117) and [CLI Guidelines](https://clig.dev/). No universal command set is implied.

## Related reference
[Guide index](../README.md) · [Composition and interfaces](../composition.md) · [Lifecycle and recovery](../lifecycle-guide.md) · [Illustrative receipt](../interface-example.md). Apply only the selected layers and qualify the actual product, not this example.
