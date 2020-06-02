import homeassistant.components.alarm_control_panel as alarm
from homeassistant.const import (
    STATE_ALARM_ARMED_AWAY,
    STATE_ALARM_DISARMED
)
from homeassistant.components.alarm_control_panel.const import (
    SUPPORT_ALARM_ARM_AWAY
)

from .const import (
    DEVICE_NAME,
    PASSCODE,
    STAUROIS_URL,
    STAUROIS_SECRET
)

import requests

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([SMAUG()])

class SMAUG(alarm.AlarmControlPanel):
    def __init__(self):
        self._state = STATE_ALARM_DISARMED

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
        # if self._code is None:
        #     return None
        # if isinstance(self._code, str) and re.search("^\\d+$", self._code):
        #     return alarm.FORMAT_NUMBER
        return alarm.FORMAT_TEXT

    @property
    def code_arm_required(self):
        """Whether the code is required for arm actions."""
        return False

    def alarm_disarm(self, code=None):
        """Send disarm command."""
        if code != PASSCODE:
            return
        self._state = STATE_ALARM_DISARMED
        requests.post(STAUROIS_URL, json={'arm': False, 'secret': STAUROIS_SECRET})

    def alarm_arm_away(self, code=None):
        """Send arm away command."""
        if code != PASSCODE:
            return
        self._state = STATE_ALARM_ARMED_AWAY
        requests.post(STAUROIS_URL, json={'arm': True, 'secret': STAUROIS_SECRET})

    @property
    def supported_features(self)-> int:
        """Return the list of supported features."""
        return SUPPORT_ALARM_ARM_AWAY
