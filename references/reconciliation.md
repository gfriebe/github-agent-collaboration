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

## Finite recovery

At 20 minutes without acknowledgement/artifact/review/merge, post one evidence-based state request. After another 60 minutes, recheck and request hand-back or reassign where possible. Never repeat nudges without a state change or threshold.

After repeated non-converging technical fixes, publish a deduplicated finding ledger and use one fresh worker/reviewer recovery attempt before human escalation.

Escalate immediately only for active security incidents, secret exposure, destructive migration authority, licensing/publication, incompatible product/security choices, stable promotion, or deployment.