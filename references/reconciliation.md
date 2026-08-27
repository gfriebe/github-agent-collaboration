# Reconciliation and recovery

Default full reconciliation cadence: 10 minutes, configurable to 10–15.

Scan open issues, comments and edits, PR reviews/threads, formal requests, checks, mergeability, participant branches, Project fields, dependencies, assignments, stale transitions, and merged work needing cleanup.

Maintain durable watermarks with overlap. Advance only after a complete scan. On partial failure keep the old watermark, retry with backoff, and expose degraded reconciliation.

## Work priority

1. Safety/security contradiction
2. Approved green PR awaiting reviewer integration
3. Formal review/re-review
4. Requested changes, failed CI, conflict, blocking question
5. Active implementation
6. Dependency/terminal reconciliation
7. Next eligible Ready claim

## Invariants

- One implementation per agent.
- No Backlog or Ready item is assigned.
- Every In progress item has accepted owner and visible artifact.
- Every In review item has a non-draft PR and formal reviewer.
- Every Ready item has satisfied dependencies, working dispatch, and independent reviewer.
- Done work triggers immediate dependent reevaluation.
- Coordination containers are excluded from Delivery.
- Genuine human gates remain visible, Blocked, and precisely described.
- No duplicate Status system exists.
- Comments never override conflicting native state.

## Finite recovery and technical authority

At 20 minutes without acknowledgement/artifact/review/merge, post one evidence-based state request. After another 60 minutes, recheck and request hand-back or reassign where possible. Never repeat nudges without a state change or threshold.

Allow at most two review/remediation rounds on substantially the same finding. Then freeze a deduplicated finding ledger with evidence and executable acceptance tests and use one fresh, bounded worker/reviewer recovery attempt.

After that attempt, the repository profile's technical decision authority must record one binding outcome: accept one approach; require a bounded prerequisite or re-scope; or stop/park because a named external capability is absent. A dissent reopens the decision only with new reproducible evidence of an acceptance, security, or compatibility violation.

A parked issue records failed approaches, owner, unblock condition, review trigger, and continuing independent work. It is not a human gate unless a separate plain-language scope, priority, cost, downtime, exposure, or cancellation decision is required.

Escalate immediately only for active security incidents, secret exposure, destructive migration authority, licensing/publication, incompatible product/security choices, stable promotion, or deployment.
