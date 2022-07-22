# Microsoft Teams - Mac Desktop App
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

app = {
    'name' : 'Teams',
    'macros' : [
        # 1st row
        (0x540908, 'Audio', [Keycode.COMMAND, Keycode.SHIFT, Keycode.M]),
        (0x000754, 'Chat',  [Keycode.COMMAND, 2]),
        (0x04541B, 'Video', [Keycode.COMMAND, Keycode.SHIFT, Keycode.O]),    

        # 2nd row
        (0x002000, 'Share', [Keycode.COMMAND, Keycode.SHIFT, Keycode.E]),
        (0x000000, '', []),
        (0x000754, 'Leave', [Keycode.COMMAND, Keycode.SHIFT, Keycode.H]),

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