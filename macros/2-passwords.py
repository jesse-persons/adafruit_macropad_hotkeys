# Password Hotkeys
# Bad idea, but fun to use
from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Passwords',
    'macros' : [
        # 1st row
        (0x000000, 'Work', ['Password 0\n']),   # \n sends the [Enter] key
        (0x000000, 'Home', ['Password 1\n']),   # You can leave it out if you
        (0x000000, 'Park', ['Password 2\n']),   # want to press [Enter] yourself.

        # 2nd row
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),

        # 3rd row
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),

        # 4th row
        (0x000000, '', []),
        (0x000000, '', []),
        (0x000000, '', []),

        # Encoder button
        (0x000000, '', []) # Close window/tab
    ]
}
