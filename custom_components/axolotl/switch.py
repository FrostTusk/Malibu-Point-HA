from homeassistant.components.switch import SwitchDevice
import requests

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([MySwitch()])

class MySwitch(SwitchDevice):
    def __init__(self):
        self._is_on = False

    @property
    def name(self):
        """Name of the device."""
        return "My Switch"

    @property
    def is_on(self):
        """If the switch is currently on or off."""
        return self._is_on

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        self._is_on = True
        requests.post('http://192.168.111.181:7896/echo', json={'test': 'test'})

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        self._is_on = False
