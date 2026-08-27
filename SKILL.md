---
name: "github-agent-collaboration"
description: "GitHub coordination for humans and coding agents with bounded WIP, independent review, reconciliation, and human gates."
---

# GitHub agent collaboration

Use GitHub as durable shared state for asynchronous software delivery. Keep workflow observable, recoverable, and platform-neutral.

Read the repository profile first. Load only the reference needed for the current action:

- `references/state-model.md` — intake, readiness, claiming, review, completion
- `references/reconciliation.md` — polling, invariants, stalls, recovery
- `references/platform-adapters.md` — OpenClaw and Hermes integration boundary
- `templates/REPOSITORY_PROFILE.md` — repository-specific configuration

## Core rules

- GitHub issue/PR facts and Project fields are operational truth; comments are audit history.
- Use one Status field: `Backlog → Ready → In progress → In review → Blocked → Done`.
- Backlog means accepted but not claimable. Ready means dependency-free, bounded, and reviewable.
- Never assign Backlog or Ready work in advance. Assignment means an execution worker accepted active responsibility.
- One short-lived branch and one author per bounded issue; require a distinct reviewer.
- Each agent owns at most one implementation and one bounded review/remediation action.
- Prefer finishing review, remediation, and integration before claiming new work.
- Labels classify durable type or handling; never duplicate Status or Priority.
- Promotion to stable/default and deployment are separate human gates.
- Human input is for genuine authority decisions, not ordinary technical uncertainty or slow execution.

## Human-decision clarity

A human gate is valid only when a non-technical decision owner can understand the choice and its consequences without translating implementation jargon.

- State the decision first in plain language: what outcome the human is authorizing, rejecting, prioritizing, funding, exposing, or accepting.
- Explain why the decision belongs to the human and what happens under each option.
- Put technical mechanisms in optional supporting detail after the plain-language question, never in place of it.
- Include one recommended option with a plain-language reason.
- Apply the repository's human-decision label only after this clarity test passes, and keep it synchronized with `Blocked` status, the decision record, and the exact next action.
- If the question cannot be reduced to an outcome choice a non-technical owner can reasonably make, it is not a human decision. Reclassify it as a technical blocker, architecture task, investigation, or agent-owned decomposition.
- Agents must resolve technical design choices themselves within existing product, security, scope, and risk constraints. Escalate only the residual authority decision, if one remains.

Clarity test: “Can the named human understand the options, consequences, recommendation, and authority being requested without knowing the proposed implementation?” If no, do not escalate it as a human gate.

## Action loop

1. Read live issues, PRs, checks, formal review requests, Project fields, dependencies, and execution availability.
2. Repair harmless stale metadata only when authorized.
3. Select the highest-ranked actionable item:
   safety gate; approved merge; review; remediation; active implementation; reconciliation; next Ready claim.
4. Perform one bounded action.
5. Read back GitHub state and record the next action.
6. Stay silent when state is healthy and no threshold is due.

## Delivery boundary

A claim is valid only after the dispatcher receives worker acceptance. Set assignee and `In progress` together, then require a pushed artifact or explicit blocker within the repository profile’s lease.

Formal review requires a non-draft PR, current base/head, linked issue, acceptance evidence, green required checks, and a formal distinct reviewer request. Any head change invalidates approval and requires fresh checks and re-review.

Completion requires satisfied acceptance, reviewer-owned integration, verified Project state, branch cleanup, and immediate dependent reevaluation.

## Safety

Fail closed on contradictory state, unavailable dispatch, missing independent review, security authority decisions, destructive migrations, secret exposure, stable promotion, and deployment. Continue safe non-overlapping work while waiting.

Do not embed repository names, agent identities, paths, credentials, or platform-specific dispatch commands in this portable core.
