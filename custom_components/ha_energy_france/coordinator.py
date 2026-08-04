"""Data update coordinator for HA Energy France."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class HAEnergyFranceData:
    """Data exposed by the integration coordinator."""

    status: str
    last_updated: datetime


class HAEnergyFranceDataUpdateCoordinator(DataUpdateCoordinator[HAEnergyFranceData]):
    """Coordinate HA Energy France data updates."""

    config_entry: ConfigEntry

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            logger=_LOGGER,
            config_entry=entry,
            name=DOMAIN,
            update_interval=UPDATE_INTERVAL,
        )

    async def _async_update_data(self) -> HAEnergyFranceData:
        """Return locally available integration data.

        This intentionally performs no I/O. Future data providers can replace this
        implementation while preserving the coordinator contract used by entities.
        """
        return HAEnergyFranceData(
            status="ready",
            last_updated=datetime.now(UTC),
        )
