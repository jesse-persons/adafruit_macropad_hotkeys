# Password Hotkeys
# Bad idea, but fun to use
from adafruit_hid.keycode import Keycode

app = {
    "name": "Passwords",
    "order": 9,
    "macros": [
        # 1st row
        (0xFF0000, "Work" , ["This can take the pain out of changing...\n"],), # \n sends the [Enter] key
        (0x00FF00, "Home" , ["...your password every 30 days at work...\n"],), # You can leave it out if you
        (0x0000FF, "Vault", ["...not that you'd ever actually do that.\n"],),  # want to send it automatically.
        
        # 2nd row
        (0x000000, "", []),
        (0x000000, "", []),
        (0x000000, "", []),
        
        # 3rd row
        (0x000000, "", []),
        (0x000000, "", []),
        (0x000000, "", []),
        
        # 4th row
        (0x000000, "", []),
        (0x000000, "", []),
        (0x000000, "", []),

        # Encoder button
        (0x000000, "", []),
    ],
}
