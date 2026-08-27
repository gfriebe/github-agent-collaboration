# Contributing

Contributions should preserve the separation between the portable protocol, repository profiles, and runtime adapters.

## Changes

1. Open an issue describing the observed problem, intended outcome, compatibility impact, and acceptance evidence.
2. Keep each pull request bounded to one protocol or adapter concern.
3. Add or update fixture tests for behavioral changes.
4. State whether the change affects the state model, repository-profile contract, or adapter contract.
5. Request review from someone other than the author.

Do not add real repository names, personal identities, hostnames, URLs, absolute paths, credentials, secrets, or private configuration to fixtures or documentation.

## Validation

Run:

```sh
python3 -m unittest discover -s tests -v
```

Behavioral claims about a runtime adapter require evidence from that adapter. Portable fixture tests alone do not establish end-to-end interoperability.
