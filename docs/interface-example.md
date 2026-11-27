# Illustrative interface contract

This is an educational example, not an installed API, real run or universal BNAI schema. The [JSON Schema](examples/inspection-receipt.schema.json) describes a minimal read-only inspection receipt. The [sample JSON](examples/inspection-receipt.json) uses fictional SHAs. A real producer must report actual revisions and outcomes. For the observed product inventory use the separate [example catalog](../examples/catalog.json) and [human-readable guide](../examples/README.md).

## Producer and consumer
A Layer 4 CLI or Layer 5 MCP tool could produce a receipt after authorized inspection of Layer 1. A Layer 3 skill or Layer 2 review procedure could consume its reference SHA, target SHA, operation, status and findings. Validate the schema and compare both revisions with the authorized scope before accepting the result; blocked status must never be promoted to success. No code execution, write authority or runtime qualification follows from parsing the receipt. Use the actual product interface where one exists.

[Composition](composition.md) · [Lifecycle](lifecycle-guide.md) · [Guide index](README.md).
