# Security policy

## Reporting

Please report suspected vulnerabilities privately through GitHub's private vulnerability reporting feature when enabled. If it is unavailable, contact the repository owner privately rather than opening a public issue.

Include the affected release, reproduction conditions, likely impact, and any evidence that can be shared safely. Do not include live credentials, tokens, private repository content, or personal host information.

## Scope

The portable skill is a coordination specification. Runtime adapters remain responsible for credential storage, least-privilege GitHub permissions, dispatch isolation, auditability, secret redaction, and safe scheduling.

Stable-branch promotion, deployment, destructive migrations, secret exposure, and security-authority decisions must fail closed pending explicit human authorization.
