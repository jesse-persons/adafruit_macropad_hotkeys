# This is for the "Magnet" window manager on the Mac.
# It could easily be adapted to work with something like FancyZones.
from adafruit_hid.keycode import Keycode

def magnet(key):
    return [Keycode.CONTROL, Keycode.OPTION, key]

app = {
    'name' : 'Magnet',
    'macros' : [
        # 1st row
        (0x000000, '<1/2', magnet(Keycode.LEFT_ARROW)),
        (0x000000, '1', magnet(Keycode.ENTER)),
        (0x000000, '1/2>', magnet(Keycode.RIGHT_ARROW)),      

        # 2nd row
        (0x000000, '', [Keycode.COMMAND, Keycode.SHIFT, '`']),
        (0x000000, '', [Keycode.COMMAND, Keycode.SHIFT, Keycode.TAB]),
        (0x000000, '', [Keycode.COMMAND, '`']),

        # 3rd row
        (0x000000, '<2/3', magnet('e')),
        (0x000000, '', [Keycode.COMMAND, Keycode.TAB]),
        (0x000000, '2/3>', magnet('t')),

        # 4th row
        (0x000000, '<1/3', magnet('d')),
        (0x000000, '1/3', magnet('f')),
        (0x000000, '1/3>', magnet('g')),

        # Encoder button
        (0x000000, '', [])
    ]
}
