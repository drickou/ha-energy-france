# Vision

## Product vision

HA Energy France aims to become the reference energy cockpit for French Home
Assistant users: a clear, trustworthy place to understand household electricity
consumption, contracts, tariffs, and meaningful changes over time.

The integration should turn fragmented French energy information into useful,
privacy-conscious Home Assistant data. It should help users understand what they
consume, compare it with relevant historical periods, and react when their
contract conditions change.

## Mission

Our mission is to provide a reliable bridge between French energy data sources
and Home Assistant while preserving a provider-independent product model. The
integration should make energy information understandable without forcing users
to know the details of utility APIs, tariff codes, or statistics internals.

## Target users

- French households that want to understand their electricity consumption.
- Home Assistant users who want daily, monthly, and yearly energy views.
- HP/HC subscribers who need accurate off-peak schedules and change alerts.
- Renters and homeowners who want contract context beside consumption data.
- Advanced users who want dependable entities and statistics for automations and
  dashboards without surrendering control of their data.

## Problems solved

French energy information is often split across provider portals, distributor
services, invoices, and tariff documents. Historical comparisons can be awkward,
HP/HC schedules may change, and raw values rarely fit directly into Home
Assistant's statistics model.

HA Energy France will solve these problems by:

- normalizing provider data into stable domain models;
- exposing consistent Home Assistant entities and long-term statistics;
- presenting daily, monthly, yearly, and previous-year comparisons;
- keeping contract details and HP/HC periods visible and actionable;
- detecting schedule changes and notifying users with useful context;
- reporting data freshness so users know when values are trustworthy.

## Product principles

1. **Clarity before density.** Prefer a few meaningful values and comparisons to
   a wall of entities or decorative charts.
2. **Stable contracts.** Provider-specific details must not leak into entity APIs
   or dashboard semantics.
3. **Honest freshness.** Stale, partial, estimated, and unavailable data must be
   identified explicitly.
4. **Home Assistant native.** Use config entries, coordinators, entity
   translations, diagnostics, repairs, statistics, and notifications according
   to current Home Assistant conventions.
5. **Incremental delivery.** Each phase must provide a testable, useful outcome
   without pre-implementing future providers or technologies.
6. **Useful automation.** Changes that matter, such as an HP/HC schedule update,
   should be easy to act on.

## Privacy principles

- Process and store only data required for the selected features.
- Never expose credentials, tokens, meter identifiers, or personal information
  in diagnostics or logs.
- Keep data in the user's Home Assistant instance whenever practical.
- Explain every external data source, permission, retention behavior, and
  limitation before authorization.
- Avoid analytics, telemetry, and third-party data sharing by default.
- Give users clear removal and reauthentication paths.

## Initial scope

The first functional product scope is intentionally focused on grid electricity:

- electricity consumption;
- daily, monthly, and yearly views;
- N-1 comparisons against equivalent previous-year periods;
- electricity contract information;
- HP/HC schedules;
- notifications when an HP/HC schedule changes.

The current `0.2` implementation is only the provider-independent Home Assistant
bootstrap. It validates lifecycle, diagnostics, translations, and test tooling
without contacting an external API.

## Long-term vision

Over time, HA Energy France should become a coherent household energy layer for
Home Assistant. Multiple approved providers should feed the same domain model,
allowing entities, statistics, dashboards, and automations to remain stable when
a user changes provider or when an upstream API evolves.

Solar production, home batteries, and electric vehicles are part of that
long-term vision, but they remain future phases. They must not complicate or
delay the first electricity-consumption release.
