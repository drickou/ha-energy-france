"""Config flow for HA Energy France."""

from __future__ import annotations

from typing import Any

from homeassistant import config_entries
import voluptuous as vol

from .const import (
    AUTH_METHOD_MOCK,
    CONF_AUTH_METHOD,
    CONF_PDL,
    CONF_PROVIDER,
    DOMAIN,
    NAME,
    PROVIDER_ENEDIS,
)
from .enedis import EnedisClient


class HAEnergyFranceConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Handle a config flow for HA Energy France."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Let the user select an energy provider."""
        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        if user_input is not None:
            return await self.async_step_enedis()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_PROVIDER): vol.In([PROVIDER_ENEDIS]),
                }
            ),
        )

    async def async_step_enedis(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> config_entries.ConfigFlowResult:
        """Configure the Enedis authentication backend."""
        if user_input is not None:
            client = EnedisClient()
            try:
                await client.authenticate()
            finally:
                await client.close()

            return self.async_create_entry(
                title=NAME,
                data={CONF_PROVIDER: PROVIDER_ENEDIS, **user_input},
            )

        return self.async_show_form(
            step_id="enedis",
            data_schema=vol.Schema(
                {
                    vol.Optional(CONF_PDL, default=""): str,
                    vol.Required(
                        CONF_AUTH_METHOD,
                        default=AUTH_METHOD_MOCK,
                    ): vol.In([AUTH_METHOD_MOCK]),
                }
            ),
        )
