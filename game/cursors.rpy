## 마우스 커서 - 애니메이션 #########################################################################
image pressed_say:
    Animation(
        "gui/cursors/pressed_say_f1.png", .5,
        "gui/cursors/pressed_say_f2.png", .5)

image button_cursor:
    Animation(
        "gui/cursors/button_f1.png", .5,
        "gui/cursors/button_f2.png", .5)

image pressed_button_cursor:
    Animation(
        "gui/cursors/pressed_button_f1.png", .5,
        "gui/cursors/pressed_button_f2.png", .5)

## 마우스 커서 #########################################################################
define config.mouse_displayable = MouseDisplayable(
    "gui/cursors/default.png", 1, 63).add(
    "pressed_default", "pressed_say", 1, 63).add(
    "pressed_say", "pressed_say", 1, 63).add(
    "button", "button_cursor", 1, 63).add(
    "pressed_button", "pressed_button_cursor", 1, 63).add(
    "drag", "gui/cursors/drag.png", 1, 63)

