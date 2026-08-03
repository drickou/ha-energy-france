# Contributing

Thank you for helping build HA Energy France. Contributions should preserve the
provider-independent architecture and current Home Assistant conventions.

## Development setup

Requirements:

- Git;
- Python 3.13 or newer;
- a fork or write access to the repository.

```bash
git clone https://github.com/drickou/ha-energy-france.git
cd ha-energy-france
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Run Home Assistant manually with the integration copied or linked to
`<config>/custom_components/ha_energy_france` when end-to-end UI verification is
needed.

## Branch naming

Create branches from the latest `main` using lowercase kebab-case:

- `feature/provider-interface`
- `fix/stale-data-availability`
- `docs/statistics-specification`
- `refactor/coordinator-snapshot`
- `test/contract-change-detection`

Do not mix unrelated changes on one branch.

## Commit conventions

Commit each logical step separately. Use an imperative, concise subject that
describes the outcome, for example:

```text
Add provider capability protocol
Handle stale consumption snapshots
Document HP/HC notification behavior
```

Commits must build on one another coherently and must not contain generated,
editor, credential, or unrelated files.

## Quality checks

Run all checks before opening or updating a pull request:

```bash
ruff check .
ruff format --check .
pytest
```

Also validate affected JSON and YAML files. GitHub Actions runs Ruff, the test
suite with coverage, hassfest, and HACS validation. Do not merge with required
checks failing.

New behavior requires tests. Provider tests must use recorded or constructed
fixtures with secrets and personal identifiers removed; tests must not call live
energy services.

## Pull requests

Every pull request must cover exactly one functional topic. A functional topic
may include its implementation, tests, translations, migration, and directly
related documentation, but not unrelated cleanup or features.

The pull request description must include:

- the problem and intended user outcome;
- architectural decisions and alternatives considered;
- files or subsystems affected;
- privacy, migration, and compatibility impact;
- exact automated and manual testing performed;
- step-by-step rollback instructions;
- known limitations and follow-up work.

Testing and rollback instructions are mandatory in every pull request. “Revert
the PR” alone is insufficient when config-entry data, statistics, credentials, or
external state could be affected; explain any cleanup or migration reversal.

Keep pull requests reviewable. Prefer a sequence of focused changes over a large
provider implementation that mixes transport, domain modeling, entities, and UI.

## Architecture rules

- Providers translate external data into domain models.
- Entities consume coordinator snapshots and never call providers directly.
- Runtime objects belong in typed `ConfigEntry.runtime_data`, not `hass.data`.
- External I/O must be asynchronous or moved off the event loop.
- Data freshness, partial results, corrections, and unavailable states must be
  explicit.
- Logs and diagnostics must redact credentials and personal or meter identifiers.
- User-facing names, states, errors, and notifications must be translatable.
- Solar, batteries, and EVs remain outside the first functional release.

## Documentation

Update the relevant specification, architecture, roadmap, UI, or README section
when behavior changes. Documentation must describe current behavior separately
from planned behavior so users do not mistake roadmap items for implemented
features.
