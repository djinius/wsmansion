## 마우스 커서 - 애니메이션 #########################################################################
image pressed_say:
    "gui/cursors/pressed_say_f1.png" with Dissolve(.5)
    pause .5
    "gui/cursors/pressed_say_f2.png" with Dissolve(.5)
    pause .5
    repeat

image button_cursor:
    "gui/cursors/button_f1.png" with Dissolve(.5)
    pause .5
    "gui/cursors/button_f2.png" with Dissolve(.5)
    pause .5
    repeat

image pressed_button_cursor:
    "gui/cursors/pressed_button_f1.png" with Dissolve(.5)
    pause .5
    "gui/cursors/pressed_button_f2.png" with Dissolve(.5)
    pause .5
    repeat

## 마우스 커서 #########################################################################
define config.mouse_displayable = MouseDisplayable(
    "gui/cursors/default.png", 1, 63).add(
    "pressed_default", "pressed_say", 1, 63).add(
    "button", "button_cursor", 1, 63).add(
    "pressed_button", "pressed_button_cursor", 1, 63)

