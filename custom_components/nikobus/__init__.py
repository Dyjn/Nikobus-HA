"""The Nikobus integration."""

from homeassistant import config_entries, core
from homeassistant.components import binary_sensor, light, switch, sensor, select
from homeassistant.const import CONF_PASSWORD, CONF_USERNAME
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN
from .coordinator import NikobusDataCoordinator
from .nikobus import Nikobus

 def async_setup_entry(hass: core.HomeAssistant, entry: config_entries.ConfigEntry) -> bool:
    """Set up the Nikobus component."""
    await Nikobus.create(hass, config)

    """ 
    coordinator = AquariteDataCoordinator(hass, api)
    coordinator.data = await hass.async_add_executor_job(api.get_pool, entry.data["pool_id"])
    
    hass.async_add_executor_job(api.subscribe, entry.data["pool_id"], coordinator.set_updated_data)

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    """
    return True

async def async_setup(hass: core.HomeAssistant, config: dict) -> bool:
    """Async setup component."""
    return True
