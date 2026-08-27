# Platform adapters

The portable skill defines behavior and GitHub state. Each runtime adapter defines discovery, installation, scheduling, dispatch, acceptance, credentials, and health without changing the state model.

## OpenClaw

Package as an OpenClaw skill proposal. Use Skill Workshop for durable updates and require explicit human application. Store runtime-specific tool names and scheduling configuration outside the portable core.

## Hermes

Publish the same versioned skill bundle or a synchronized rendered copy through the Hermes-supported skill/configuration path. The Hermes coordinator must provide a durable top-level reconciliation scheduler and an issue-scoped worker dispatcher with an observable acceptance signal. A watcher that can only comment is unavailable for automatic claims.

## Compatibility contract

Every adapter reports:

- protocol version and content digest
- repository profile version
- last successful reconciliation
- dispatch availability and acceptance signal
- actor identity and permissions
- degraded/error state

Adapters must produce identical GitHub transitions for the same fixture. Platform-specific comments or task IDs may differ, but Status, assignee, reviewer request, checks, and Next action must agree.

## Sharing and upgrades

Keep the canonical portable source in a neutral versioned repository or dedicated directory. Publish immutable tagged releases and SHA-256 digests. GitHub issue comments may announce versions but are not the source.

Use semantic versions:

- patch: wording, diagnostics, non-behavioral clarification
- minor: backward-compatible fields, transitions, or adapter capability
- major: incompatible state model or repository-profile contract

Upgrade one adapter in a fixture repository first, run transition tests, then roll out to the other adapter. During mixed versions, the older compatible version governs claims; incompatible versions pause new claims while review/remediation may continue.