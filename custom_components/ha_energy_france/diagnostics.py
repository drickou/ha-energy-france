"""Diagnostics support for HA Energy France."""

from __future__ import annotations

from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.core import HomeAssistant

from . import HAEnergyFranceConfigEntry

TO_REDACT = {
    "access_token",
    "api_key",
    "email",
    "meter_id",
    "password",
    "refresh_token",
}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant,
    entry: HAEnergyFranceConfigEntry,
) -> dict[str, Any]:
    """Return diagnostics for a config entry."""
    return {
        "config_entry": {
            "data": async_redact_data(dict(entry.data), TO_REDACT),
            "options": async_redact_data(dict(entry.options), TO_REDACT),
        },
        "coordinator": {
            "last_update_success": entry.runtime_data.last_update_success,
            "last_updated": entry.runtime_data.data.last_updated.isoformat(),
            "status": entry.runtime_data.data.status,
        },
    }
