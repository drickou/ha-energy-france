"""Sensor platform for HA Energy France."""

from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.const import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import HAEnergyFranceConfigEntry

PARALLEL_UPDATES = 0

STATUS_SENSOR_DESCRIPTION = SensorEntityDescription(
    key="status",
    translation_key="status",
    device_class=SensorDeviceClass.ENUM,
    entity_category=EntityCategory.DIAGNOSTIC,
    options=["ready"],
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: HAEnergyFranceConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up HA Energy France sensors from a config entry."""
    async_add_entities([HAEnergyFranceStatusSensor(entry)])


class HAEnergyFranceStatusSensor(
    CoordinatorEntity,
    SensorEntity,
):
    """Represent the status of the HA Energy France integration."""

    _attr_has_entity_name = True
    entity_description = STATUS_SENSOR_DESCRIPTION

    def __init__(self, entry: HAEnergyFranceConfigEntry) -> None:
        """Initialize the status sensor."""
        super().__init__(entry.runtime_data)
        self._attr_unique_id = f"{entry.entry_id}_status"

    @property
    def native_value(self) -> str:
        """Return the integration status."""
        return self.coordinator.data.status
