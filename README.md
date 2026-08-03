# HA Energy France

HA Energy France is a custom Home Assistant integration that will provide French
energy data through a modern, maintainable integration architecture.

> [!IMPORTANT]
> Version 0.2 is an architectural bootstrap. It does not connect to Enedis, EDF,
> or another external API yet. It creates one diagnostic status sensor so the
> complete Home Assistant lifecycle can be installed and tested safely.

## Current functionality

- UI-based configuration with a single config entry.
- A local `DataUpdateCoordinator` that performs no network I/O.
- A translated diagnostic sensor reporting whether the integration is ready.
- Downloadable, privacy-conscious diagnostics.
- English and French translations.
- Clean unloading and reloading through Home Assistant's config-entry lifecycle.

## Requirements

- Home Assistant 2026.1.0 or newer.

No account, API key, or external service is required for this bootstrap release.

## Installation with HACS

Until the repository is listed in HACS, add it as a custom repository:

1. Open HACS in Home Assistant.
2. Open the three-dot menu and select **Custom repositories**.
3. Enter `https://github.com/drickou/ha-energy-france`.
4. Select **Integration** as the category and add the repository.
5. Install **HA Energy France** and restart Home Assistant.

## Manual installation

1. Copy `custom_components/ha_energy_france` into the `custom_components`
   directory inside your Home Assistant configuration directory.
2. Restart Home Assistant.

The resulting path must be:

```text
<config>/custom_components/ha_energy_france/manifest.json
```

## Configuration

1. Open **Settings → Devices & services**.
2. Select **Add integration**.
3. Search for **HA Energy France**.
4. Confirm the setup form.

Only one config entry is supported. After setup, Home Assistant creates the
diagnostic **Integration status** sensor with the state `ready`.

## Diagnostics

Diagnostics can be downloaded from the integration's device-and-service page.
Known credential and account fields are redacted. The bootstrap diagnostics
contain only config-entry metadata and coordinator health information.

## Removal

1. Open **Settings → Devices & services**.
2. Select **HA Energy France**.
3. Delete the config entry from its menu.
4. To uninstall completely, remove it through HACS or delete the
   `custom_components/ha_energy_france` directory, then restart Home Assistant.

## Development

Use Python 3.13 or newer:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
ruff check .
ruff format --check .
pytest
```

The runtime is intentionally provider-independent. A future Enedis implementation
should supply data through the existing coordinator contract instead of coupling
API calls directly to entities.

## Support

Report problems through the
[GitHub issue tracker](https://github.com/drickou/ha-energy-france/issues).

## License

MIT
