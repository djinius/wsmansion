## Quick Menu 스크린 ##############################################################
##
## 퀵메뉴는 게임 외 메뉴 접근성을 높여주기 위해 게임 내에 표시됩니다.

default persistent.showQuickMenu = True

init python:
    def isQuickVisible():
        global quick_menu

        return quick_menu and persistent.showQuickMenu and (renpy.get_screen("exploreMap") is None) and (renpy.get_screen("exploreFound") is None) and (renpy.get_screen("cameraMinigame") is None)

screen quick_menu():

    ## 다른 화면 위에 표시되는지 확인합니다.
    zorder 100

    if isQuickVisible():

        imagemap:
            align (1., 1.)
            auto ("gui/quickmenu/%s.png")
            hotspot (  0, 0, 60, 60) action ShowMenu('history')
            hotspot ( 60, 0, 60, 60) action Show('inventory') sensitive myInventory

            hotspot (180, 0, 60, 60) action Preference("auto-forward", "toggle")
            hotspot (240, 0, 60, 60) action Skip()
            hotspot (300, 0, 60, 60) action Skip(fast=True, confirm=True)
            hotspot (360, 0, 60, 60) action ShowMenu('save')
            hotspot (420, 0, 60, 60) action ShowMenu('preferences')
            hotspot (480, 0, 60, 60) action HideInterface()

        key "mousedown_4" action ShowMenu("history")
        key "mousedown_5" action ShowMenu("history")

## 플레이어가 UI(스크린)을 일부러 숨기지 않는 한 퀵메뉴가 게임 내에 오버레이로
## 출력되게 합니다.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


