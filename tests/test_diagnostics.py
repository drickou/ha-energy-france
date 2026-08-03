"""Tests for HA Energy France diagnostics."""

from homeassistant.components.diagnostics import REDACTED
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.ha_energy_france import HAEnergyFranceConfigEntry
from custom_components.ha_energy_france.const import DOMAIN, NAME
from custom_components.ha_energy_france.diagnostics import (
    async_get_config_entry_diagnostics,
)


async def test_config_entry_diagnostics(hass) -> None:
    """Test config entry diagnostics and sensitive-value redaction."""
    entry: HAEnergyFranceConfigEntry = MockConfigEntry(
        domain=DOMAIN,
        unique_id=DOMAIN,
        title=NAME,
        data={"api_key": "secret"},
        options={},
    )
    entry.add_to_hass(hass)
    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    diagnostics = await async_get_config_entry_diagnostics(hass, entry)

    assert diagnostics["config_entry"]["data"]["api_key"] == REDACTED
    assert diagnostics["coordinator"]["last_update_success"] is True
    assert diagnostics["coordinator"]["status"] == "ready"
    assert diagnostics["coordinator"]["last_updated"]
