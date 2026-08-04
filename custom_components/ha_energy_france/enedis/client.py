"""Asynchronous client for Enedis."""

from __future__ import annotations

from .auth import EnedisAuthService, MockEnedisAuthService
from .exceptions import EnedisAuthenticationError


class EnedisClient:
    """Expose the public interface used to interact with Enedis."""

    def __init__(self, auth_service: EnedisAuthService | None = None) -> None:
        """Initialize the Enedis client."""
        self._auth_service = auth_service or MockEnedisAuthService()

    async def authenticate(self) -> bool:
        """Authenticate using the configured backend."""
        if not await self._auth_service.authenticate():
            raise EnedisAuthenticationError
        return True

    async def close(self) -> None:
        """Close resources held by the authentication backend."""
        await self._auth_service.close()
