import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Initialize RGB module
rgb = RGB(pixel_pin=board.D7, num_pixels=2)
keyboard.modules.append(rgb)

PINS = [board.D5, board.D10, board.D11, board.D12]
ENCODER_PINS = (board.D9, board.D8)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


encoder_handler.pins = [ENCODER_PINS]  
encoder_handler.map = [((KC.VOLU, KC.VOLD),)]

sleep_restart = KC.MACRO(
    on_press=[Press(KC.LCMD), Press(KC.LSHIFT), Press(KC.OPTION), Press(KC.Q), Release(KC.LCMD), Release(KC.LSHIFT), Release(KC.OPTION)],
    on_hold=[Press(KC.LCMD), Press(KC.LSHIFT), Tap(KC.Q), Release(KC.LSHIFT), Release(KC.LCMD)],
    hold_time=500
)

minimize_all = KC.MACRO(Press(KC.LCMD), Press(KC.LALT), Tap(KC.M), Release(KC.LALT), Release(KC.LCMD))

open_slack = KC.MACRO(
    Press(KC.LCMD), Press(KC.LSHIFT), Tap(KC.S), Release(KC.LSHIFT), Release(KC.LCMD)
)

open_vscode = KC.MACRO(
    Press(KC.LCMD), Press(KC.LSHIFT), Tap(KC.S), Release(KC.LSHIFT), Release(KC.LCMD)
)

# Set Neopixel colors
rgb.colors = [
    (0, 0, 255),  # Blue
    (255, 255, 0)  # Yellow
]

keyboard.keymap = [
    [sleep_restart, minimize_all, KC.NO, open_slack, open_vscode]
]

if __name__ == '__main__':
    keyboard.go()
