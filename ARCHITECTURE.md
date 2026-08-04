# Architecture

## Overview

HA Energy France uses a provider-independent, layered architecture. External
data formats are normalized at the boundary, while Home Assistant entities
consume stable domain models. This prevents upstream API changes—or the addition
of another provider—from forcing entity and dashboard rewrites.

The current bootstrap implements the Home Assistant lifecycle, a local
coordinator, one diagnostic sensor, diagnostics, and translations. It does not
implement Enedis or another external provider yet.

## Layers and responsibilities

### Data providers

Provider adapters own authentication, transport, rate limits, response parsing,
and provider-specific errors. They return domain objects rather than exposing raw
JSON. Provider code must not create Home Assistant entities or notifications.

A future provider protocol should expose capability-based operations such as:

- fetch consumption for a bounded date range;
- fetch contract details;
- fetch HP/HC schedules;
- report source timestamps and data quality.

### Domain models

Domain models represent consumption intervals, aggregates, comparisons,
contracts, schedules, and freshness. They use explicit units and timezone-aware
timestamps. They contain no Home Assistant objects and should be independently
testable.

### Coordinator

The coordinator owns one provider session per config entry, refresh scheduling,
error translation, snapshot consistency, and listener notification. It publishes
a single immutable runtime snapshot. Entities read that snapshot and never call
providers directly.

The bootstrap coordinator currently performs no I/O and returns a local `ready`
status. Future work should extend its data contract without coupling it to a
single provider implementation.

### Entities

Entities adapt domain values to Home Assistant units, device classes, state
classes, availability, and translations. Entity unique IDs derive from stable
domain identifiers, not display names or provider response ordering.

Entities must remain provider-agnostic. Adding a provider that implements the
same capabilities should require configuration and adapter work, not duplicated
sensor classes.

### Statistics

The statistics layer validates intervals, performs calendar-aware aggregation,
handles corrections and backfills, and prevents duplicate sums. Long-term
statistics must follow Home Assistant requirements and preserve source units.

### Contract monitoring

Contract monitoring compares normalized contract snapshots. HP/HC schedule
changes are detected from canonical schedule fingerprints, confirmed with fresh
data, and persisted so reloads do not repeat notifications.

### Notifications

Notifications are a Home Assistant boundary concern. They consume confirmed
domain events and produce translated, actionable messages. Providers never send
notifications directly.

## Adding a future provider

1. Implement the provider protocol and capability declarations.
2. Map raw responses and errors to existing domain types.
3. Add provider-specific config-flow and reauthentication steps.
4. Supply the provider to the coordinator through runtime data.
5. Add contract tests using provider fixtures.

If a provider needs a genuinely new concept, extend the domain model first. Do
not add provider conditionals throughout entities.

## Home Assistant lifecycle

1. The config flow creates a single `ConfigEntry`.
2. `async_setup_entry` creates the coordinator and awaits its first refresh.
3. The coordinator is assigned to typed `ConfigEntry.runtime_data`.
4. Home Assistant awaits `async_forward_entry_setups` for supported platforms.
5. Platforms create coordinator-backed entities.
6. `async_unload_entry` awaits `async_unload_platforms`.
7. Home Assistant releases `runtime_data` with the config-entry lifecycle.

Runtime objects must not be placed in the legacy `hass.data` integration map.
Future listeners and sessions should be registered with config-entry unload
callbacks where automatic cleanup is required.

## Proposed directory structure

```text
custom_components/ha_energy_france/
├── __init__.py                 # Config-entry setup and unload
├── config_flow.py              # Setup, reauth, and reconfigure flows
├── const.py                    # Shared constants
├── coordinator.py              # Refresh orchestration and runtime snapshot
├── diagnostics.py              # Privacy-safe diagnostics
├── manifest.json
├── sensor.py                   # Provider-independent sensor entities
├── strings.json
├── translations/
│   ├── en.json
│   └── fr.json
├── models/
│   ├── consumption.py
│   ├── contract.py
│   ├── freshness.py
│   └── schedule.py
├── providers/
│   ├── __init__.py             # Provider protocol and capabilities
│   └── enedis.py               # Future Enedis adapter
├── statistics/
│   ├── aggregation.py
│   └── comparison.py
└── monitoring/
    ├── contracts.py
    └── notifications.py

tests/
├── fixtures/
├── providers/
├── test_config_flow.py
├── test_diagnostics.py
├── test_init.py
└── test_statistics.py
```

Directories should be added only when their phase begins; the bootstrap remains
deliberately small today.
