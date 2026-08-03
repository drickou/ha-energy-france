"""Tests for HA Energy France setup."""

from homeassistant.config_entries import ConfigEntryState
from homeassistant.helpers import entity_registry as er
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.ha_energy_france import HAEnergyFranceConfigEntry
from custom_components.ha_energy_france.const import DOMAIN, NAME
from custom_components.ha_energy_france.coordinator import (
    HAEnergyFranceDataUpdateCoordinator,
)


async def test_setup_and_unload_entry(hass) -> None:
    """Test setup, sensor creation, and unloading."""
    entry: HAEnergyFranceConfigEntry = MockConfigEntry(
        domain=DOMAIN,
        unique_id=DOMAIN,
        title=NAME,
        data={},
    )
    entry.add_to_hass(hass)

    assert await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()

    assert entry.state is ConfigEntryState.LOADED
    assert isinstance(entry.runtime_data, HAEnergyFranceDataUpdateCoordinator)
    assert entry.runtime_data.last_update_success

    entity_registry = er.async_get(hass)
    entity_id = entity_registry.async_get_entity_id(
        "sensor",
        DOMAIN,
        f"{entry.entry_id}_status",
    )
    assert entity_id is not None
    assert hass.states[entity_id].state == "ready"

    assert await hass.config_entries.async_unload(entry.entry_id)
    await hass.async_block_till_done()
    assert entry.state is ConfigEntryState.NOT_LOADED
