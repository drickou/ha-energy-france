# UI Guidelines

## Goals

The recommended Home Assistant dashboard should answer five questions quickly:

1. How much electricity have I used today?
2. How does this compare with the equivalent period last year?
3. What are my month and year trends?
4. What contract and HP/HC period applies now?
5. Is the underlying data current and complete?

Readability and useful comparisons take priority over visual density.

## Design principles

- Use native Home Assistant cards when they communicate the data clearly.
- Lead with current consumption and one relevant comparison.
- Keep units, periods, and freshness visible.
- Use consistent date boundaries across values shown together.
- Reserve strong color for actionable exceptions such as stale data or a
  confirmed contract schedule change.
- Avoid excessive gauges, gradients, traffic-light colors, decorative cards,
  animated backgrounds, and duplicate representations of the same value.
- Do not imply that estimated costs or partial data are authoritative.

## Suggested dashboard structure

### 1. Today

- Today's electricity consumption in kWh.
- Difference and percentage change versus the equivalent N-1 day.
- A compact intraday or recent-days graph when interval data is available.
- Freshness badge or last successful update.

Use plain values and a small history chart. A gauge is inappropriate unless a
meaningful, user-configured limit exists.

### 2. Month

- Current calendar-month total.
- Equivalent elapsed-period comparison with N-1.
- Daily bars for the current month.
- Partial-period indicator when source days are missing.

Do not compare an incomplete current month with the entirety of last year's
month without labeling the mismatch.

### 3. Year

- Current calendar-year total.
- Equivalent elapsed-period N-1 difference and percentage.
- Monthly trend with no more color series than needed.
- Optional indication of incomplete or corrected months.

### 4. Contract

- Contract option.
- Subscribed power in kVA.
- Provider or distributor label when useful.
- Contract data timestamp.

Contract identifiers and account details must not be displayed by default.

### 5. HP/HC

- Current tariff period: peak, off-peak, or unknown.
- Next transition time.
- Complete daily HP/HC schedule in chronological order.
- Effective date and last verification time.
- A visible but restrained alert after a confirmed schedule change.

## State presentation

### Loading

Show placeholders or unavailable entities without substituting zero. Zero is a
valid consumption value and must never mean “not loaded.”

### Missing data

State which period is missing and suppress derived comparisons that would be
misleading. Example: “Two daily intervals are unavailable; monthly total is
partial.”

### Stale data

Keep the last known value only when it remains useful. Pair it with the source
timestamp and a clear “stale” label. Do not use an alarming full-page treatment
unless user action is required.

### Unavailable provider

Show the last successful update and a concise explanation. Authentication
failures should link users toward reauthentication; temporary failures should not
request credentials repeatedly.

### Changed HP/HC schedule

Show the effective date, old and new windows, and a reminder to review dependent
automations. Once acknowledged, the dashboard should return to its normal visual
hierarchy while retaining the current schedule.

## Accessibility and localization

- Never communicate meaning through color alone.
- Maintain readable contrast in light and dark Home Assistant themes.
- Keep labels concise and translatable; do not embed units in translated names.
- Allow French text expansion without truncating essential values.
- Use locale-aware dates, times, decimal separators, and units.
