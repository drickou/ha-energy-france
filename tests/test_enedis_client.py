"""Tests for the asynchronous Enedis client."""

from unittest.mock import AsyncMock

import pytest

from custom_components.ha_energy_france.enedis import EnedisClient
from custom_components.ha_energy_france.enedis.exceptions import (
    EnedisAuthenticationError,
)


async def test_default_mock_authentication_succeeds() -> None:
    """Test the temporary default authentication backend."""
    client = EnedisClient()

    assert await client.authenticate() is True
    await client.close()


async def test_custom_authentication_backend() -> None:
    """Test that a future authentication backend can be injected."""
    auth_service = AsyncMock()
    auth_service.authenticate.return_value = True
    client = EnedisClient(auth_service)

    assert await client.authenticate() is True
    await client.close()

    auth_service.authenticate.assert_awaited_once_with()
    auth_service.close.assert_awaited_once_with()


async def test_authentication_failure_raises() -> None:
    """Test that a rejected authentication is exposed consistently."""
    auth_service = AsyncMock()
    auth_service.authenticate.return_value = False
    client = EnedisClient(auth_service)

    with pytest.raises(EnedisAuthenticationError):
        await client.authenticate()
