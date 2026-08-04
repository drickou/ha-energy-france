"""Authentication services for Enedis."""

from __future__ import annotations

from typing import Protocol


class EnedisAuthService(Protocol):
    """Interface implemented by Enedis authentication backends."""

    async def authenticate(self) -> bool:
        """Authenticate with Enedis."""
        ...  # pragma: no cover

    async def close(self) -> None:
        """Close authentication resources."""
        ...  # pragma: no cover


class MockEnedisAuthService:
    """Temporary authentication backend used to validate the config flow."""

    async def authenticate(self) -> bool:
        """Simulate successful authentication."""
        return True

    async def close(self) -> None:
        """Close the mock backend."""
