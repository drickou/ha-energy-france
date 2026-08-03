"""HA Energy France integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .coordinator import HAEnergyFranceDataUpdateCoordinator

PLATFORMS: list[Platform] = [Platform.SENSOR]

type HAEnergyFranceConfigEntry = ConfigEntry[HAEnergyFranceDataUpdateCoordinator]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HAEnergyFranceConfigEntry,
) -> bool:
    """Set up HA Energy France from a config entry."""
    coordinator = HAEnergyFranceDataUpdateCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: HAEnergyFranceConfigEntry,
) -> bool:
    """Unload a HA Energy France config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
