# State model

## Intake

Create delivery issues only from a human request, accepted roadmap decomposition, discovered defect/security/dependency, or a bounded follow-up separated from active work.

Every issue records outcome, scope/non-goals, acceptance, source/parent, dependencies, Priority, compatibility/rollback, eligible owner, distinct reviewer, and Next action. Check duplicates first.

New delivery work starts unassigned in Backlog.

## Status definitions

- Backlog: accepted work that is not currently claimable.
- Ready: acceptance is bounded, dependencies are satisfied, base is known, execution dispatch works, and an independent reviewer is available.
- In progress: a worker accepted the issue; assignee, branch/artifact, milestone, and recent progress are visible.
- In review: an open non-draft PR has current evidence and a formal reviewer request.
- Blocked: a concrete condition prevents progress; record owner, evidence, recovery, and Next action.
- Done: acceptance is satisfied and integration is verified.

Coordination containers remain Backlog with `coordination` and are excluded from delivery views. They are not claimed.

## Dependency transition

Whenever an issue becomes Done or a dependency changes, immediately evaluate every dependent:

1. Re-read all dependencies.
2. Verify bounded acceptance, current base, eligible execution route, and distinct reviewer availability.
3. If all conditions pass, move Backlog → Ready and set the exact next action.
4. Otherwise keep Backlog and record the exact unmet condition in Next action.
5. Recalculate queue order.

Test invariant: completing issue A makes directly dependent B Ready when eligible; later dependents remain Backlog.

## Claiming

Only Ready issues may be claimed. The coordinator serializes claims. Dispatch issue, base SHA, branch, boundaries, milestone, and reviewer. Assign and set In progress only after worker acceptance.

No advance reservation by assignee. Use `Eligible owner` for planning.

Default lease: acknowledge and push the first tested artifact within 20 minutes, otherwise release to Ready or mark Blocked with recovery.

## Priority

Use High, Normal, Low. Human priority is authoritative.

High blocks active delivery or multiple downstream items. Normal is ordinary accepted work. Low is optional improvement without current dependency impact.

## Review and completion

Authors do not self-approve or self-merge. Reviewers verify exact SHA, diff, checks, mergeability, unresolved threads, and human gates. Head changes invalidate approval.

After merge: verify acceptance, set Done, close issue, delete branch, reevaluate dependents, and recompute the Ready queue.