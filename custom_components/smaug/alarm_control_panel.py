import homeassistant.components.alarm_control_panel as alarm
from homeassistant.const import (
    STATE_ALARM_ARMED_HOME,
    STATE_ALARM_DISARMED
)
from homeassistant.components.alarm_control_panel.const import (
    SUPPORT_ALARM_ARM_HOME
)

from .const import (
    DEVICE_NAME,
    PASSCODE,
    AMNIRANA_URL,
    AMNIRANA_SECRET
)

import requests

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([SMAUG(hass)])

class SMAUG(alarm.AlarmControlPanel):
    def __init__(self, hass):
        self._state = STATE_ALARM_DISARMED
        self._hass = hass

    @property
    def name(self):
        """Name of the device."""
        return DEVICE_NAME

    @property
    def state(self):
        """If the switch is currently on or off."""
        return self._state

    @property
    def code_format(self):
        """Return one or more digits/characters."""
        if PASSCODE is None:
            return None
        if isinstance(PASSCODE, str) and PASSCODE.isdigit():
            return alarm.FORMAT_NUMBER
        return alarm.FORMAT_TEXT

    @property
    def code_arm_required(self):
        """Whether the code is required for arm actions."""
        return False

    def alarm_disarm(self, code=None):
        """Send disarm command."""
        requests.post("http://192.168.222.221:7896/echo", json={'hass_debug': str(self._hass.states.get("device_tracker.falco").state)})
        if code != PASSCODE and self._hass.states.get("device_tracker.falco").state != "home":
            return
        self._state = STATE_ALARM_DISARMED
        requests.post(AMNIRANA_URL, json={'arm': False, 'secret': AMNIRANA_SECRET})

    def alarm_arm_home(self, code=None):
        """Send arm away command."""
        self._state = STATE_ALARM_ARMED_HOME
        requests.post(AMNIRANA_URL, json={'arm': True, 'secret': AMNIRANA_SECRET})

    @property
    def supported_features(self)-> int:
        """Return the list of supported features."""
        return SUPPORT_ALARM_ARM_HOME
