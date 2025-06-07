import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.LED import LED
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)
keyboard.row_pins = (board.GP8, board.GP9, board.GP10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

Mirror = KC.Macro(
    Press(KC.SHIFT)
    Tap(KC.M)
    Release(KC.SHIFT)
)

Boolean = KC.Macro(
    Press(KC.SHIFT)
    Tap(KC.B)
    Release(KC.SHIFT)
)

Split = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.S)
    Release(CTRLSHIFT)
)

Scetch = KC.Macro(
    Press(SHIFT)
    Tap(KC.S)
    Release(SHIFT)
)

Equal = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.E)
    Release(CTRLSHIFT)
)

Mid = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.M)
    Release(CTRLSHIFT)
)

Perpendicular = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.L)
    Release(CTRLSHIFT)
)

Mater = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.M)
    Release(CTRLSHIFT)
)

Transparent = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.t)
    Release(CTRLSHIFT)
)

Isolate = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.I)
    Release(CTRLSHIFT)
)

Fit = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.N0)
    Release(CTRLSHIFT)
)

Replace = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.R)
    Release(CTRLSHIFT)
)

Context = KC.Macro(
    Press(CTRLSHIFT)
    Tap(KC.S)
    Release(CTRLSHIFT)
)

#Shiftup = KC.DF(keyboard.active_layers + 1)
#Trans#rights = KC.MO(1)


#if keyboard.active_layers[3] == 3:
#    KC.DF(0)

rgb = RGB(pixel_pin=board.GP7, num_pixels=3)
keyboard.extensions.append(rgb)

if keyboard.active_layers[0] == 0:
    KC.RGB_TOG(0)
    KC.RGB_TOG(2)

if keyboard.active_layers[1] == 1:
    KC.RGB_TOG(1)
    KC.RGB_TOG(0)

if keyboard.active_layers[2] == 2:
    KC.RGB_TOG(2)
    KC.RGB_TOG(1)


keyboard.keymap = [
    [#0, Assembly
        KC.DF(1), KC.Z
        KC.M,  Mater,  KC.I, KC.G, Transparent
        Isolate, KC.R, Fit, Replace, Context
    ],
     [#1, Part Studio
        KC.DF(2), KC.Z
        KC.E,  KC.C,  KC.F, KC.C, Mirror
        Boolean, KC.P, Split, KC.T, Scetch
    ],
    [#2, Scetch
        KC.DF(0), KC.Z
        KC.L,  KC.C,  KC.D, KC.I, KC.B
        KC.T, Equal, Mid, Perpendicular, KC.N
    ],
]

if __name__ == '__main__':
    keyboard.go()






