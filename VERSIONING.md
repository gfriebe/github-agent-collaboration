# Versioning policy

This project follows Semantic Versioning.

- Patch: wording, diagnostics, or non-behavioral clarification.
- Minor: backward-compatible fields, transitions, or adapter capabilities.
- Major: incompatible state-model, repository-profile, or adapter-contract changes.

Public history begins at `v0.1.0`; internal protocol revision numbers are not public release versions.

Releases must be immutable and include a SHA-256 digest of the skill bundle. Runtime adapters should report the loaded release and digest. Upgrade one fixture environment first. During a mixed compatible rollout, the older version governs new claims. Incompatible versions pause new claims while safe review and remediation may continue.
