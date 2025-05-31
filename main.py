import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

PINS = [board.D3, board.D4, board.D2, board.D1]
ENCODER_PINS = (board.D5, board.D6)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


encoder_handler.pins = [ENCODER_PINS]  
encoder_handler.map = [((KC.VOLU, KC.VOLD),)]

sleep_restart = KC.MACRO(
    on_press=[Press(KC.LCTL), Press(KC.LCMD), Tap(KC.PWR), Release(KC.LCMD), Release(KC.LCTL)],
    on_hold=[Press(KC.LCTL), Press(KC.LCMD), Press(KC.PWR), Release(KC.PWR), Release(KC.LCMD), Release(KC.LCTL)],
    hold_time=500
)

minimize_all = KC.MACRO(Press(KC.LCMD), Press(KC.LALT), Tap(KC.M), Release(KC.LALT), Release(KC.LCMD))

open_slack = KC.MACRO(
    Press(KC.LCMD), Tap(KC.T), Release(KC.LCMD),
    Tap(KC.S), Tap(KC.L), Tap(KC.A), Tap(KC.C), Tap(KC.K), Tap(KC.ENTER)
)

open_vscode = KC.MACRO(
    Press(KC.LCMD), Tap(KC.T), Release(KC.LCMD),
    Tap(KC.V), Tap(KC.S), Tap(KC.SPACE), Tap(KC.C), Tap(KC.O), Tap(KC.D), Tap(KC.E), Tap(KC.ENTER)
)

keyboard.keymap = [
    [sleep_restart, minimize_all, KC.NO, open_slack, open_vscode]
]

if __name__ == '__main__':
    keyboard.go()