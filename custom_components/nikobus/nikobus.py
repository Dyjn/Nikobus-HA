""" Nikobus API """
import logging
import socket
import threading

import voluptuous as vol

from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.dispatcher import async_dispatcher_connect, async_dispatcher_send
from homeassistant.helpers.entity import Entity

from .const import DOMAIN

DATA_LISTENER = 'nikobus_socket_listener'
CONF_PAYLOAD_DELIMITER = '\n'

_LOGGER = logging.getLogger(__name__)

class Nikobus:

    def __init__(self, host: str, port: str) -> None:
        """Initialize Nikobus Bridge."""
        self.host = host
        self.port = port
        self.handlers = []

    @classmethod
    async def create(cls, hass, host: str, port: str):
        """Set up the TCP socket listener."""
        listener = TcpSocketListener(hass, host, port, CONF_PAYLOAD_DELIMITER)
        listener.start()
        hass.data[DATA_LISTENER] = listener
        _LOGGER.info("TCP socket listener created on %s:%s", host, port)
        return True

class TcpSocketListener(threading.Thread):
    """Thread to listen for TCP/IP socket events."""

    def __init__(self, hass, host, port, delimiter):
        """Initialize the listener."""
        super().__init__()
        self.hass = hass
        self.host = host
        self.port = port
        self.delimiter = delimiter
        self._stop_event = threading.Event()

    def run(self):
        """Start the listener."""
        _LOGGER.info("Start for TCP/IP socket on %s:%s", self.host, self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((self.host, self.port))
            sock.listen(1)
            _LOGGER.info("Listening for TCP/IP socket events on %s:%s", self.host, self.port)

            while not self._stop_event.is_set():
                conn, addr = sock.accept()
                _LOGGER.debug("Connected by %s", addr)

                data = b''
                while True:
                    chunk = conn.recv(1024)
                    if not chunk:
                        break
                    data += chunk

                    if self.delimiter in data.decode():
                        event_data, data = data.split(self.delimiter, 1)
                        event_data = event_data.decode().strip()
                        _LOGGER.debug("Received data: %s", event_data)
                        async_dispatcher_send(self.hass, DATA_LISTENER, event_data)

                conn.close()
        except OSError as err:
            _LOGGER.error("Error listening on %s:%s: %s", self.host, self.port, err)
        finally:
            sock.close()

    def stop(self):
        """Stop the listener."""
        self._stop_event.set()

class TcpSocketEventSensor(Entity):
    """Representation of a TCP/IP socket event sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    async def async_added_to_hass(self):
        """Register dispatcher callback."""
        self.async_on_remove(async_dispatcher_connect(
            self.hass, DATA_LISTENER, self._update_callback))

    async def _update_callback(self, data):
        """Handle event updates."""
        self._state = data
        self.async_write_ha_state()

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'TCP Socket Event'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def should_poll(self):
        """Disable polling."""
        return False
