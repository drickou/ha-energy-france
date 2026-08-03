"""Config flow for HA Energy France."""

from __future__ import annotations

from typing import Any

from homeassistant import config_entries

from .const import DOMAIN


class HAEnergyFranceConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Handle a config flow for HA Energy France."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Handle the initial configuration step."""

        if user_input is not None:
            await self.async_set_unique_id(DOMAIN)
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title="HA Energy France",
                data={},
            )

        return self.async_show_form(
            step_id="user",
            data_schema=None,
        )