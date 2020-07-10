/* Good on you for modifying your layout! if you don't have
 * time to read the QMK docs, a list of keycodes can be found at
 *
 * https://github.com/qmk/qmk_firmware/blob/master/docs/keycodes.md
 *
 * There's also a template for adding new layers at the bottom of this file!
 */

#include QMK_KEYBOARD_H
#include "g/keymap_combo.h"

#define BASE 0  // default layer
#define SYMB 1  // symbols
#define NUMB 2  // numbers/motion

/* Combomap
 *
 * ,-----------------------------.       ,--------------------------------.
 * |      |    ESC    |     |     |      |     |    ESC    |    BSLH      |
 * |-----+-----+-----+-----+------|      |--------------------------------|
 * |      |   BSPC   ENT    |     |      |    LES   COLN  GRT    |        |
 * |-----+-----+-----+--RMB+-LMB--+       |--------------------------------|
 * |      |   MINS    |     |     |      |    QUO   UNDR   |     |        |
 * `------+-----+-----+------+----'       `--------------------------------'
 *  .-------------------------.           .-----------------.
 *  |        |       |        |           |        |    |   |
 *  '-------------------------'           '-----------------'
 */

// Blank template at the bottom
const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    /* Keymap 0: Basic layer
     *
     * ,-----------------------------.       ,--------------------------------.
     * |    Q |  W  |  E  |  R  |  T  |      |  Y  |  U  |  I  |  O  |    P   |
     * |-----+-----+-----+-----+------|      |--------------------------------|
     * |CTRL/A|  S  |  D  |  F  |  G  |      |  H  |  J  |  K  |  L  | CTRL/; |
     * |-----+-----+-----+-----+------+       |--------------------------------|
     * |SHFT/Z|  X  |  C  |  V  |  B  |      |  N  |  M  |  <  |  >  | SHFT/? |
     * `------+-----+-----+------+----'       `--------------------------------'
     *  .-------------------------.           .-----------------.
     *  |ESC/META|ENT/ALT|SPC(SYM)|           |SPC(NUM)|BSPC|TAB|
     *  '-------------------------'           '-----------------'
     */
[BASE] = LAYOUT_gergoplex(
    KC_Q,                KC_W, KC_E, KC_R, KC_T,    KC_Y, KC_U, KC_I,    KC_O,    KC_P, 
    MT(MOD_LCTL, KC_A),  KC_S, KC_D, KC_F, KC_G,    KC_H, KC_J, KC_K,    KC_L,    MT(MOD_LGUI, KC_SCLN),
    MT(MOD_LGUI, KC_Z),  KC_X, KC_C, KC_V, KC_B,    KC_N, KC_M, KC_COMM, KC_DOT,  MT(MOD_LCTL, KC_SLSH),

    LT(SYMB, KC_NO), MT(MOD_RSFT, KC_ENT), ALT_T(KC_ESC),
    KC_TAB, LT(NUMB, KC_SPC), LT(NUMB, KC_NO)
    ),
    /* Keymap 1: Symbols layer
     * ,-----------------------------.       ,--------------------------------.
     * |  !   |  @  |  {  |  }  |  `  |      |  ~  |     |     |  \  |
     * |-----+-----+-----+-----+------|      |--------------------------------|
     * |  #   |  $  |  (  |  )  | LMB |      |  +  |  -  |  /  |  *  |    '   |
     * |-----+-----+-----+-----+------+      |--------------------------------|
     * |  %   |  ^  |  [  |  ]  | RMB |      |  &  |  =  |  ,  |  .  |   -    |
     * `------+-----+-----+------+----'      `--------------------------------'
     *          .-----------------.           .------------------.
     *          |MMB |  ;  |  =   |           |  =  |  ;  |  DEL |
     *j          '-----------------'           '------------------'
     */

[SYMB] = LAYOUT_gergoplex(
    KC_NO,   KC_LBRC, KC_LCBR,  KC_TILD, KC_NO,   KC_NO,   KC_GRV,   KC_RCBR, KC_RBRC, KC_NO,
    KC_LPRN, KC_DLR,  KC_PERC,  KC_MINS, KC_NO,   KC_HASH, KC_QUOT,  KC_DQUO, KC_EQL,  KC_RPRN,
    KC_AT,   KC_ASTR, KC_CIRC,  KC_PIPE, KC_NO,   KC_NO,   KC_PLUS,  KC_AMPR, KC_EXLM, KC_BSLS,
                      KC_NO,    KC_NO,   KC_NO,   KC_DEL,  KC_UNDS,  KC_NO
    ),
    /* Keymap 2: Pad/Function layer
     * ,-----------------------------.       ,-------------------------------.
     * |  1   |  2  |  3  |  4  |  5  |      |  6  |  7  |  8  |  9  |   0   |
     * |-----+-----+-----+-----+------|      |-------------------------------|
     * |  F1  | F2  | F3  | F4  |  F5 |      | LFT | DWN | UP  | RGT | VOLUP |
     * |-----+-----+-----+-----+------+      |-------------------------------|
     * |  F6  | F7  | F8  | F9  | F10 |      |MLFT | MDWN| MUP | MRGT| VOLDN |
     * `------+-----+-----+------+----'      `-------------------------------'
     *          .-----------------.           .-----------------.
     *          | F11 | F12|      |           |     | PLY | SKP |
     *          '-----------------'           '-----------------'
     */

[NUMB] = LAYOUT_gergoplex(
    KC_5,  KC_LCBR,  KC_LPRN,  KC_LBRC,     KC_9,       KC_NO,  KC_RBRC,   KC_RPRN,  KC_RCBR,   KC_9,
    KC_1,  KC_2,  KC_3,  KC_4,     KC_5,     KC_6,    KC_7,     KC_8,    KC_9,    KC_0,
    KC_5,  KC_6,  KC_7,  KC_BTN1,     KC_BTN2,       KC_MS_L,  KC_MS_D, KC_MS_U,  KC_MS_R, KC_VOLD,
                  KC_NO, KC_TILD,  KC_BTN2,    KC_BTN2,  KC_BTN1, KC_MNXT
    )
};
