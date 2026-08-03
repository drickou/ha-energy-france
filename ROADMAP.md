# Roadmap

The roadmap is sequential at the product level. Research may overlap, but a
phase is complete only when its acceptance criteria are met.

## Phase 1 — Home Assistant bootstrap

### Deliverables

- Config-entry setup and unload lifecycle.
- Typed `ConfigEntry.runtime_data`.
- Provider-independent `DataUpdateCoordinator`.
- Sensor platform with a local diagnostic status entity.
- Diagnostics, translations, tests, Ruff, CI, README, and HACS metadata.

### Acceptance criteria

- The integration installs, configures, reloads, and unloads without an external
  API.
- Ruff, tests, hassfest, and HACS validation pass in CI.
- Diagnostics redact likely credential and account fields.
- No Enedis-specific model is embedded in entities.

## Phase 2 — Data-source evaluation

### Deliverables

- Documented evaluation of official and permitted French energy data sources.
- Authentication, consent, rate-limit, availability, and retention analysis.
- Provider interface prototype and representative fixtures.
- Decision record selecting the first production source.

### Acceptance criteria

- Legal and technical usage constraints are documented.
- Required consumption and contract fields are mapped to domain concepts.
- Failure modes, refresh limits, and data latency are known.
- No credential is stored or logged outside Home Assistant conventions.

## Phase 3 — Enedis consumption data

### Deliverables

- Enedis provider adapter behind the provider interface.
- UI authorization and reauthentication flows.
- Daily consumption retrieval with coordinator error handling.
- Freshness metadata and privacy-safe diagnostics.

### Acceptance criteria

- A user can authorize, load, refresh, reauthenticate, and remove the provider.
- Daily consumption is normalized to watt-hours or kilowatt-hours with explicit
  timestamps and quality metadata.
- Offline, unauthorized, partial, and rate-limited responses are handled without
  log spam or loss of the last valid snapshot.
- Provider tests use fixtures and make no live API calls.

## Phase 4 — Daily, monthly, and yearly statistics

### Deliverables

- Daily values and calendar-aligned monthly and yearly aggregates.
- N-1 comparison models for equivalent periods.
- Home Assistant-compatible entities and long-term statistics.
- Backfill and duplicate-prevention strategy.

### Acceptance criteria

- Aggregates are reproducible from normalized source data.
- Time-zone changes, leap years, incomplete periods, and corrections are tested.
- Statistics do not double-count after reload or backfill.
- Comparisons clearly report unavailable or non-equivalent baselines.

## Phase 5 — HP/HC contract schedules and change detection

### Deliverables

- Normalized contract and HP/HC schedule models.
- Current-period and next-transition entities.
- Persisted schedule fingerprint and change detection.
- Translated Home Assistant notification on confirmed changes.

### Acceptance criteria

- Multiple daily HP/HC windows and overnight periods are represented correctly.
- A notification is sent once per newly confirmed schedule change.
- The notification shows the old schedule, new schedule, effective date, source,
  and recommended verification action.
- Missing or stale schedules never produce false change notifications.

## Phase 6 — Cost estimation

### Deliverables

- Tariff model with effective dates and HP/HC pricing.
- Daily, monthly, and yearly estimated cost entities.
- Transparent estimation metadata and documented limitations.

### Acceptance criteria

- Every estimate identifies currency, covered period, tariff source, and
  freshness.
- Tariff changes split calculations at the correct effective timestamp.
- Taxes, subscriptions, and unavailable price components are not silently
  invented.
- Estimated costs are clearly distinguished from invoices.

## Phase 7 — Dashboard and user experience

### Deliverables

- Recommended day, month, year, contract, and HP/HC dashboard sections.
- Examples using native Home Assistant cards where practical.
- Missing, loading, partial, stale, and unavailable states.
- Setup, troubleshooting, and migration documentation.

### Acceptance criteria

- Core questions can be answered without opening provider portals.
- Comparisons remain readable on desktop and mobile.
- Stale and missing data are prominent without dominating healthy views.
- The dashboard avoids excessive gauges, colors, and decorative cards.

## Phase 8 — Future solar, battery, and EV support

### Deliverables

- Separate discovery and design proposals for solar, batteries, and EVs.
- Extended domain models that preserve the electricity-consumption API.
- Provider capability negotiation for optional energy flows.

### Acceptance criteria

- Existing consumption entities and statistics remain backward compatible.
- Each technology has a validated data source and clear user value.
- Energy-flow accounting avoids double counting between grid, production,
  storage, and vehicle charging.
- These features are delivered only after the first functional release is stable.
