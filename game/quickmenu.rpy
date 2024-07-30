## Quick Menu 스크린 ##############################################################
##
## 퀵메뉴는 게임 외 메뉴 접근성을 높여주기 위해 게임 내에 표시됩니다.

default persistent.showQuickMenu = True
default persistent.showTooltip = True
default quick_menu = True

## 플레이어가 UI(스크린)을 일부러 숨기지 않는 한 퀵메뉴가 게임 내에 오버레이로
## 출력되게 합니다.

init python:
    class quickTooltip:
        def __init__(self, titleText, descText, p, a):
            self.titleText = titleText
            self.descText = descText
            self.p = p
            self.a = a

    def isQuickVisible():
        global quick_menu

        return quick_menu and persistent.showQuickMenu and (renpy.get_screen("exploreMap") is None) and (renpy.get_screen("exploreFound") is None) and (renpy.get_screen("cameraMinigame") is None)

screen quick_menu():

    ## 다른 화면 위에 표시되는지 확인합니다.
    zorder 100

    if isQuickVisible():

        $ tooltip = GetTooltip('quick_menu')

        if persistent.showTooltip and (tooltip is not None):
            $ [t, d, p, a] = tooltip

            frame:
                pos p anchor a
                padding (20, 10)
                has vbox
                xalign .5

                text t size 35 xalign .5
                text d size 20 xalign .5

        imagemap:
            align (1., 1.)
            auto ("gui/quickmenu/%s.png")
            hotspot (  0, 0, 60, 60):
                action ShowMenu('history')
                tooltip ["대사록(L)", "대사록을 엽니다.", (1920 - 60 * 8 - 30, 1000), (.5, 1.)]
            hotspot ( 60, 0, 60, 60):
                action Show('inventory')
                sensitive myInventory
                tooltip ["보관함(I)", "보관함을 엽니다.", (1920 - 60 * 7 - 30, 1000), (.5, 1.)]

            hotspot (180, 0, 60, 60):
                action Preference("auto-forward", "toggle")
                tooltip ["자동 진행", "대사를 자동으로 진행합니다.", (1920 - 60 * 5 - 30, 1000), (.5, 1.)]
            hotspot (240, 0, 60, 60):
                action Skip()
                tooltip ["빠르게 진행", "대사를 빠르게 진행합니다.", (1920 - 60 * 4 - 30, 1000), (.5, 1.)]
            hotspot (300, 0, 60, 60):
                action Skip(fast=True, confirm=False)
                tooltip ["건너뛰기", "다음 선택지, 혹은 다음 장면까지 건너뜁니다.", (1920 - 60 * 3 - 30, 1000), (.5, 1.)]
            hotspot (360, 0, 60, 60):
                action ShowMenu('save')
                tooltip ["저장(S)", "현재 게임을 저장합니다.", (1920 - 60 * 2 - 30, 1000), (.5, 1.)]
            hotspot (420, 0, 60, 60):
                action ShowMenu('preferences')
                tooltip ["설정(P)", "게임 설정을 엽니다.", (1920, 1000), (1., 1.)]
            hotspot (480, 0, 60, 60):
                action HideInterface()
                tooltip ["숨기기(H)", "게임 인터페이스를 숨깁니다.", (1920, 1000), (1., 1.)]

        key "mousedown_4" action ShowMenu("history")
        key "mousedown_5" action ShowMenu("history")
        key "K_l" action ShowMenu("history")
        key "K_p" action ShowMenu("preferences")
        if myInventory:
            key "K_i" action ToggleScreen('inventory')

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


