# Media controls
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    'name' : 'Media Keys',
    'order' : 1,
    'macros' : [
        # 1st row
        (0x666666, '<<', [ConsumerControlCode.REWIND]),
        (0xFFFFFF, 'Play',  [ConsumerControlCode.PLAY_PAUSE]),
        (0x666666, '>>', [ConsumerControlCode.FAST_FORWARD]),

        # 2nd row
        (0x663300, '<', [Keycode.COMMAND, Keycode.SHIFT, Keycode.E]),
        (0x111111, 'Stop', []),
        (0x663300, '>', [Keycode.COMMAND, Keycode.SHIFT, Keycode.H]),

        # 3rd row
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),

        # 4th row
        (0x200000, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x080F54, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]]),

        # Encoder button
        (0x000000, '', [])
    ]
}