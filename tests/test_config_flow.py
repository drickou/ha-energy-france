"""Tests for the HA Energy France config flow."""

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResultType
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.ha_energy_france.const import (
    AUTH_METHOD_MOCK,
    CONF_AUTH_METHOD,
    CONF_PDL,
    CONF_PROVIDER,
    DOMAIN,
    NAME,
    PROVIDER_ENEDIS,
)


async def test_user_flow(hass) -> None:
    """Test creating an Enedis config entry from the user flow."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_USER},
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "user"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_PROVIDER: PROVIDER_ENEDIS},
    )

    assert result["type"] is FlowResultType.FORM
    assert result["step_id"] == "enedis"

    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            CONF_PDL: "12345678901234",
            CONF_AUTH_METHOD: AUTH_METHOD_MOCK,
        },
    )

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["title"] == NAME
    assert result["data"] == {
        CONF_PROVIDER: PROVIDER_ENEDIS,
        CONF_PDL: "12345678901234",
        CONF_AUTH_METHOD: AUTH_METHOD_MOCK,
    }


async def test_optional_pdl_defaults_to_empty_string(hass) -> None:
    """Test that the PDL can be omitted."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_USER},
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_PROVIDER: PROVIDER_ENEDIS},
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_AUTH_METHOD: AUTH_METHOD_MOCK},
    )

    assert result["type"] is FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_PDL] == ""


async def test_duplicate_entry_aborts(hass) -> None:
    """Test that only one config entry can be created."""
    MockConfigEntry(domain=DOMAIN, unique_id=DOMAIN, data={}).add_to_hass(hass)

    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": config_entries.SOURCE_USER},
    )

    assert result["type"] is FlowResultType.ABORT
    assert result["reason"] == "single_instance_allowed"
