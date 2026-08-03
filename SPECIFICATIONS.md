# First Functional Release Specifications

## Purpose and scope

The first functional release turns normalized French electricity data into a
small, reliable set of Home Assistant entities and statistics. It builds on the
existing provider-independent bootstrap. The selected provider and authorization
mechanism are decided during data-source evaluation.

## Required data

The runtime snapshot must contain:

- daily electricity consumption;
- calendar-month totals;
- calendar-year totals;
- N-1 comparisons for equivalent daily, monthly, and yearly periods;
- HP/HC periods, including current period and next transition;
- contract details available from the selected source;
- source timestamp, retrieval timestamp, completeness, and freshness state.

All timestamps must be timezone-aware. Consumption has a canonical internal unit
and must preserve enough precision to avoid aggregation drift.

## Proposed Home Assistant entities

| Entity | Native unit | Device class | State class | Normal update frequency |
| --- | --- | --- | --- | --- |
| Today's consumption | kWh | `energy` | `total_increasing`* | Provider limit, target 30–60 min |
| Current month consumption | kWh | `energy` | `total` | After coordinator refresh |
| Current year consumption | kWh | `energy` | `total` | After coordinator refresh |
| Daily N-1 difference | kWh | `energy` | `measurement` | After coordinator refresh |
| Daily N-1 change | % | — | `measurement` | After coordinator refresh |
| Monthly N-1 difference | kWh | `energy` | `measurement` | After coordinator refresh |
| Monthly N-1 change | % | — | `measurement` | After coordinator refresh |
| Yearly N-1 difference | kWh | `energy` | `measurement` | After coordinator refresh |
| Yearly N-1 change | % | — | `measurement` | After coordinator refresh |
| Tariff period | enum (`peak`, `off_peak`, `unknown`) | `enum` | — | At transition and refresh |
| Next tariff transition | timestamp | `timestamp` | — | At schedule refresh |
| Contract power | kVA | — | `measurement` | Daily or on contract refresh |
| Contract option | enum/text | `enum` when bounded | — | Daily or on contract refresh |
| Data freshness | enum (`fresh`, `delayed`, `stale`, `unknown`) | `enum` | — | Every coordinator refresh |
| Last successful data update | timestamp | `timestamp` | — | Every successful refresh |

\* If provider data can revise the current day downward, the implementation must
avoid an invalid `total_increasing` series. It may expose completed-day totals or
use another statistics strategy documented before implementation.

Entity names and enum states must use translation keys. Less frequently useful
contract and freshness entities should be diagnostic or disabled by default when
appropriate.

## Aggregation and comparisons

- Day boundaries use the Home Assistant instance timezone unless the provider
  contract requires a documented French-market timezone.
- Monthly and yearly totals are calendar aligned.
- N-1 compares equivalent elapsed periods, not a complete previous period with
  an incomplete current period.
- Leap-day behavior must be explicit and tested.
- Missing source intervals make an aggregate partial; they must not be treated as
  zero.
- Corrected provider data must replace previous intervals without double counting.

## Freshness

The coordinator must expose the last successful retrieval, source data timestamp,
expected publication delay, and a derived freshness state. Entities become
unavailable only when their value cannot be trusted; stale but valid last-known
data may remain visible with an explicit freshness indicator.

Refresh frequency must respect provider limits. The initial target is every 30 to
60 minutes for consumption, with slower contract refreshes unless the provider
offers change events.

## HP/HC schedule change detection

Schedules are normalized into ordered periods with local start/end times,
effective dates, timezone, and source. A canonical fingerprint excludes retrieval
metadata so identical schedules do not appear changed.

A change notification is emitted only when:

1. both the previous and new schedules are complete and fresh;
2. their canonical fingerprints differ;
3. the new fingerprint has not already been acknowledged or notified;
4. the effective date is known, or explicitly reported as unknown.

The translated notification must include:

- title identifying an HP/HC schedule change;
- contract or meter label without exposing sensitive identifiers;
- previous schedule;
- new schedule;
- effective date and timezone;
- source and data timestamp;
- advice to verify dependent automations and provider documentation.

Transient missing data, reordered equivalent periods, reloads, and repeated
provider responses must not produce notifications.

## Non-functional requirements

- Setup, reauthentication, reload, and removal are supported through the UI.
- Provider failures use Home Assistant retry and reauthentication semantics.
- Diagnostics redact credentials and personal or meter identifiers.
- All provider behavior, aggregations, migrations, and notifications are tested.
- Entities never call provider APIs directly.

## Explicit exclusions

The first functional release does not include solar production, photovoltaic
forecasting, batteries, energy storage optimization, electric vehicles, or EV
charging. These remain future roadmap phases.
