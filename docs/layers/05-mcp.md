# Layer 5 — MCP connectivity

Purpose: expose approved operations and contextual resources to compatible AI hosts via the [Model Context Protocol](https://modelcontextprotocol.io/docs/learn/architecture). MCP is a protocol, not an identity engine, model or permission grant.

Build a small versioned server interface with typed tool input/output, explicit read vs mutation, bounded execution and validation, resource provenance and per-repository authorization. Choose a maintained language SDK appropriate to the existing core; use supported stdio or remote transport for the target host. Remote hosting requires authenticated access, isolation, secret handling and cost controls. Do not use an ephemeral Actions job as permanent server hosting.

With Layer 1, retrieve installation identity and state or execute scoped operations. With Layer 2, expose current contract and resources without allowing resource text to change authority. With Layer 3, skills select advertised capabilities. With Layer 4, share the core or safely adapt CLI. MCP alone with Layer 1 is valid; a CLI or dedicated skill is not a requirement.

Qualify handshake/discovery, version compatibility, authentication, wrong-target rejection, schema errors, denied writes, cancellation, stale state and receipt retrieval. A local stdio test does not qualify remote browser access. Host-specific tool availability and actual invocation need independent evidence.
