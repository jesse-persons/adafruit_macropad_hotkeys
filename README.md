# :keyboard: App Group Hackropad!

## Hello, App Group!

What could be a better gift for your keyboard than another, smaller, keyboard! This [Adafruit Macropad RP2040s](https://learn.adafruit.com/adafruit-macropad-rp2040) is everything your keyboard is looking for in a mate. It's cute as a button, fun at parties, and able to be quickly assembled without soldering. Powered by a [RP2040](https://www.raspberrypi.com/products/rp2040/) microcontroller, and customizable with [Arduino IDE](https://www.arduino.cc/en/software) or [CircuitPython](https://circuitpython.org) (and maybe QMK in [late August](https://github.com/qmk/qmk_firmware/issues/11649#issuecomment-1173050422)?), you'll find a lot of room to tinker and play.

The code in this repo is based on the work of [Phillip Burgess](https://github.com/PaintYourDragon) from [Adafruit](https://www.adafruit.com). You could easily use the original code in place of mine. It has been a good jumping off point and highlights some of the _odder_ features of the pad.

- [Phillip's article explaining the details of the code](https://learn.adafruit.com/macropad-hotkeys)
- [Download code from article directly](https://learn.adafruit.com/pages/22617/elements/3099360/download?type=zip)
- [GitHub repo with code from the article ](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/Macropad_Hotkeys)

Others:
- [deckerego/Macropad_Hotkeys](https://github.com/deckerego/Macropad_Hotkeys)
    - Much improved organization and modularity
    - I stole the app "order" code from here

## Assembly

1. Clear a little time in your schedule.
    - The physical assembly goes fast, but you may want to add time to futz with the software.
2. Clear a space to work.
    - It doesn't have to be much. I successfully assembled the macropad in about 2 cubic feet[^1].
3. Follow along with the [assembly video](https://www.youtube.com/watch?v=_aW90ufD6X0) from Adafruit.
    - There are also [written instructions](https://learn.adafruit.com/adafruit-macropad-rp2040/macropad-assembly) if you'd rather.
    - Pay special attention to the pins on the keyswitches. Make sure to straighten them before inserting as they may have been bent during shipping.
4. The feet that come with the kit are okay but don't provide any "pinball machine" angle [^2], making it tough to see the screen if you use the default (screen at the top) orientation.
    - I've added conical rubber feet[^3] to mine, but the angle is still a little too shallow.
    - The maker community has already created several examples of 3D printed stands and enclosures.
        - https://learn.adafruit.com/3d-printed-stand-for-macropad-rp2040/3d-printing
        - https://www.thingiverse.com/thing:4943775
    - You can rotate the display in software if you'd like the screen/rotary encoder at the bottom. [^4]

## Software

### Host Machine

1. The [Mu editor](https://codewith.mu) is a nice place to start with CircuitPython.
    - It should automatically find and identify your board when you plug it in.
    - The serial console window will be invaluable as you start.
2. [Visual Studio Code](https://code.visualstudio.com), with the Python and CircuitPython plugins, is also excellent.
3. You can download the [Arduino IDE](https://www.arduino.cc/en/software) if you'd like. It's a nice next step to CircuitPython.

### Macropad

The pad comes with an Arduino based demo that shows the full range of RGB capability of the onboard LEDs. It also lets you test that your keyswitches and rotary encoder are working correctly. Please take a moment to press all the keys (even all at once if you want) and give the rotary knob a spin.

Replacing the initial demo and getting functional code on the macropad takes a few steps.

1. Download the latest stable version[^5] of CircuitPython for the macropad: https://circuitpython.org/board/adafruit_macropad_rp2040/
    - You should get a UF2[^6] file, a firmware bundle for the microcontroller
2. Download the CircuitPython library bundle that matches the version of the CircuitPython firmware you downloaded in the previous step: https://circuitpython.org/libraries [^7]
3. Clone or download the code from this repository.
4. Put the macropad in "bootloader mode" by plugging it in while holding down the rotary encoder switch (releasing after plugging in), or by holding the reset button on the side along with the rotary encoder, then releasing the reset button and rotary encoder switch in turn.
    - This will prepare the microcontroller to receive new software.
    - You should see a new drive, named "RPI-RP2" connected to your computer.
5. Drag and drop the UF2 file from step 1 into the "RPI-RP2" drive. It will take a few seconds and the pad will reboot into the new firmware.
6. If all went well...
    - the "RPI-RP2" drive will be replaced with a drive named "CIRCUITPY"
    - the macropad display will show a picture of a snake[^8] and the words "Hello World!\n\nCode Done Running."
    
![](https://user-images.githubusercontent.com/488418/180620410-814385e7-e1d3-4115-998b-c69607bec525.mp4)

7. Opening up the CIRCUITPY drive, you should see a file called "code.py"
8. Copy the following libraries from the CircuitPython library bundle (downloaded in step 2) into the "lib" directory on the "CIRCUITPYTHON" drive:
    - lib/adafruit_debouncer.mpy
    - lib/adafruit_display_shapes
    - lib/adafruit_display_text
    - lib/adafruit_hid
    - lib/adafruit_macropad.mpy
    - lib/adafruit_midi
    - lib/adafruit_simple_text_display.mpy
    - lib/adafruit_ticks.mpy
    - lib/neopixel.mpy
9. Copy the following files from this repository into the root of the "CIRCUITPYTHON" drive (if prompted, choose to overwrite existing files):
    - boot.py
    - code.py
    - macros
10. Your macropad should do a "soft reboot" when the new code has finished copying, and you should see...

![Adafruit Macropad RP2040 showing numpad screen after booting custom code](https://user-images.githubusercontent.com/488418/180620517-7babf656-3f1b-4ee5-8c99-cc13901a7bea.jpg)

## What Now?

Start making changes to code.py and the contents of the macros. Customize it and make it yours. Share the changes you make with the group, but don't wait until you're proud. We're all learning together. Look at things that other people have done. Steal it and use it to make your macropad better!

## boot.py tweak

When you're satisfied with the state of your pad, you'll probably want to keep the CIRCUITPY drive from mounting every time you connect the pad. This code will prevent the drive from being mounted unless you press and hold the rotary encoder shortly after a hard reset (or when applying power). If the encoder is held down while the neopixel under the first key is flashing, the drive will mount. Somewhat more convenient than having it always disabled and struggling to get the board into safe mode.

```python
import board
import digitalio
import storage

# Mount the CIRCUITPY drive if the encoder switch is held down
encoder_switch = digitalio.DigitalInOut(board.BUTTON)
encoder_switch.switch_to_input(pull=digitalio.Pull.UP)
if(encoder_switch.value):
    print("NOT Mounting CIRCUITPY")
    storage.disable_usb_drive()
else:
    print("Mounting CIRCUITPY")
```


## Features

### Achieved :tada:
- [x] Sleep mode that disables the screen, keys, and LEDs
- [x] Mouse jiggle function to keep session from timing out

### Intended
- [ ] Bi-directional communication with macropad
- [ ] Automatic switching configurations on host app switch
- [ ] App specific notifications for launcher
- [ ] Time and date display
- [ ] Allow binding of arbitrary functions
- [ ] Modifier keys / level shifting

[^1]: 2 cubic-feet of mulch can cover 24 square feet to a depth of 1 inch.
[^2]: Typically 6.5-7°
[^3]: Never search "silicone feet" on Amazon
[^4]: It does put the cable right in the way, but you could always run a flat USB-C connector up through the underside of the pad.
[^5]: v7.3.2 at the time of writing
[^6]: [UF2 Technical Spec](https://github.com/microsoft/uf2)
[^7]: v7.X at the time of writing
[^8]: representing Blinka, the CircuitPython mascot
