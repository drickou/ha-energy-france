"""Constants for HA Energy France."""

from datetime import timedelta

DOMAIN = "ha_energy_france"
NAME = "HA Energy France"
UPDATE_INTERVAL = timedelta(minutes=15)

CONF_PROVIDER = "provider"
CONF_PDL = "pdl"
CONF_AUTH_METHOD = "authentication_method"

PROVIDER_ENEDIS = "enedis"
AUTH_METHOD_MOCK = "mock"
