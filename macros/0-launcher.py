# This specifically works with "Spotlight Search" on the Mac.
# There must be other ways to do this on other platforms.
from adafruit_hid.keycode import Keycode

def launcher(name):
    return [Keycode.COMMAND, Keycode.SPACE, " {0}.app\n".format(name)]

app = {
    'name' : 'Launcher',
    'macros' : [
        # 1st row
        (0x000000, 'Term',  launcher("iTerm")),
        (0x000000, 'Web',   launcher("Safari")),
        (0x000000, 'Mail',  launcher("Mail")),      

        # 2nd row
        (0x000000, 'File',  launcher("Finder")),
        (0x000000, 'Msg',   launcher("Messages")),
        (0x000000, 'Code',  launcher("Visual Studio Code")),

        # 3rd row
        (0x000000, 'Cal',   launcher("Calendar")),
        (0x000000, 'Calc',  launcher("Calculator")),
        (0x000000, 'Cam',   launcher("Photo Booth")),

        # 4th row
        (0x000000, 'News',  launcher("News")),
        (0x000000, 'Music', launcher("Music")),
        (0x000000, 'DB',    launcher("Querious")),

        # Encoder button
        (0x000000, '', [])
    ]
}
