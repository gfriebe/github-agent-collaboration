# GitHub Agent Collaboration

An opinionated, portable Agent Skill for coordinating humans and coding agents through GitHub Issues, Pull Requests, and optionally GitHub Projects.

The protocol favors observable delivery over agent status prose: bounded work in progress, explicit readiness, independent review, scheduled reconciliation, finite recovery, and human-controlled promotion and deployment.

## Status

This repository starts at `v0.1.0`. The protocol has been exercised in one real multi-agent project, but portability is still being validated.

- The portable workflow specification is included.
- OpenClaw and Hermes adapter responsibilities are documented.
- Runtime installation, scheduling, dispatch, and credentials remain adapter-specific.
- Full OpenClaw/Hermes interoperability is **not yet claimed**. Fixture validation currently checks the portable bundle and core state invariants only.

## Contents

```text
SKILL.md
references/
  platform-adapters.md
  reconciliation.md
  state-model.md
templates/
  REPOSITORY_PROFILE.md
tests/
  test_bundle.py
```

`SKILL.md` contains the essential operating loop. Detailed transitions, recovery behavior, and adapter boundaries are loaded only when needed.

## Installation

Pin an immutable release rather than tracking `main` automatically.

1. Download or clone a tagged release.
2. Copy the bundle into the skill directory supported by your agent runtime.
3. Create a repository profile from `templates/REPOSITORY_PROFILE.md` outside the portable bundle.
4. Configure the runtime adapter for authentication, polling, dispatch, acceptance signals, and health reporting.
5. Verify the loaded release and checksum before enabling claims.

OpenClaw installations should use Skill Workshop and require explicit human application. Hermes installations need a durable reconciliation scheduler and an issue-scoped worker dispatcher; a comment-only watcher is insufficient.

## Design boundaries

This is intentionally not workflow-neutral. It assumes:

- GitHub Issues and Pull Requests as durable delivery state;
- an optional GitHub Project with one six-stage Status field;
- limited work in progress and a distinct reviewer;
- periodic reconciliation rather than webhook dependence;
- explicit human authority for stable promotion and deployment.

Repository identities, paths, credentials, dispatch commands, and hosting details belong in the repository profile or runtime adapter, never in the portable core.

## Versioning

Public releases use semantic versioning from `v0.1.0`. Earlier internal protocol revisions are development history, not public major releases. See [VERSIONING.md](VERSIONING.md).

## Security

Do not report suspected vulnerabilities in public issues. Follow [SECURITY.md](SECURITY.md).

## License

Apache License 2.0. See [LICENSE](LICENSE).
