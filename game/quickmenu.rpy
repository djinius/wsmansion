## Quick Menu 스크린 ##############################################################
##
## 퀵메뉴는 게임 외 메뉴 접근성을 높여주기 위해 게임 내에 표시됩니다.

default persistent.showQuickMenu = 2
default persistent.showTooltip = True
default quick_menu = True

## 자동 숨기기/보이기 트랜스폼
transform quickMenuHidden():
    yoffset 60

transform quickMenuAppear():
    easein 1. yoffset 0

transform quickMenuFix():
    yoffset 0

transform quickMenuReappear():
    easein .5 yoffset 0

transform quickMenuHide():
    yoffset 0
    pause 1.5
    easein 1. yoffset 60

## 플레이어가 UI(스크린)을 일부러 숨기지 않는 한 퀵메뉴가 게임 내에 오버레이로
## 출력되게 합니다.

default quickMenuAutoHide = 0

screen quick_menu():

    ## 다른 화면 위에 표시되는지 확인합니다.
    zorder 100
    style_prefix "quick"

    if isQuickVisible():
        imagemap:
            pos (1., 1.) anchor (1., 1.)

            if not _in_replay:
                auto ("gui/quickmenu/ingame_%s.png")
            else:
                auto ("gui/quickmenu/replay_%s.png")

            hotspot (  0, 0, 60, 60):
                action ShowMenu('history')
                activate_sound "audio/sfx/paper.mp3"

                if _in_replay:
                    tooltip ["대사록({u}{color=008}L{/color}{/u})", "지나간 대사를 다시 열람합니다.", (1920 - 60 * 9 - 30, 1020), (.5, 1.)]
                else:
                    tooltip ["대사록({u}{color=008}L{/color}{/u})", "지나간 대사를 다시 열람합니다.\n대사록의 대사를 클릭해 해당 시점으로\n되돌아갈 수 있습니다.", (1920 - 60 * 9 - 30, 1020), (.5, 1.)]

            if not _in_replay:
                hotspot ( 60, 0, 60, 60):
                    action Show('inventory')
                    activate_sound "audio/sfx/paper.mp3"
                    sensitive myInventory
                    tooltip ["소지품({u}{color=008}I{/color}{/u})", "소지품을 확인합니다.", (1920 - 60 * 8 - 30, 1020), (.5, 1.)]

            if not isQuickExploring():
                hotspot (180, 0, 60, 60):
                    action Preference("auto-forward", "toggle")
                    activate_sound "audio/sfx/paper.mp3"
                    tooltip ["자동 진행", "대사를 자동으로 진행합니다.", (1920 - 60 * 6 - 30, 1020), (.5, 1.)]
                hotspot (240, 0, 60, 60):
                    action Skip()
                    activate_sound "audio/sfx/paper.mp3"
                    tooltip ["빠르게 진행({u}{color=008}TAB{/color}{/u})", "대사를 빠르게 진행합니다.", (1920 - 60 * 5 - 30, 1020), (.5, 1.)]
                hotspot (300, 0, 60, 60):
                    action Skip(fast=True, confirm=False)
                    activate_sound "audio/sfx/paper.mp3"
                    tooltip ["건너뛰기", "다음 선택지나 장면,\n혹은 마지막으로 진행한 장면까지 건너뜁니다.", (1920 - 60 * 4 - 30, 1020), (.5, 1.)]

            if not _in_replay:
                hotspot (360, 0, 60, 60):
                    action ShowMenu('save')
                    activate_sound "audio/sfx/paper.mp3"
                    tooltip ["저장({u}{color=008}S{/color}{/u})", "현재 게임을 저장합니다.", (1920 - 60 * 3 - 30, 1020), (.5, 1.)]
            else:
                hotspot (360, 0, 60, 60):
                    action EndReplay(confirm=False)
                    activate_sound "audio/sfx/paper.mp3"
                    tooltip ["다시보기 끝", "다시보기를 끝내고 돌아갑니다.", (1920 - 60 * 3 - 30, 1020), (.5, 1.)]
            hotspot (420, 0, 60, 60):
                action ShowMenu('preferences')
                activate_sound "audio/sfx/paper.mp3"
                tooltip ["설정({u}{color=008}P{/color}{/u})", "화면 모드 및 음량, 기타 게임을 진행하기 위한\n편의사항을 설정합니다.", (1920, 1020), (1., 1.)]

            if not _in_replay:
                hotspot (480, 0, 60, 60):
                    action MainMenu(confirm=True)
                    activate_sound "audio/sfx/paper.mp3"
                    tooltip ["시작 화면", "시작 화면으로 돌아갑니다.", (1920, 1020), (1., 1.)]

            hotspot (540, 0, 60, 60):
                action HideInterface()
                activate_sound "audio/sfx/paper.mp3"
                tooltip ["숨기기({u}{color=008}H{/color}{/u})", "게임 인터페이스를 숨깁니다.", (1920, 1020), (1., 1.)]

            if persistent.showQuickMenu == 2:
                at quickMenuFix
            if persistent.showQuickMenu == 1:
                if quickMenuAutoHide == 0:
                    at quickMenuHide
                elif quickMenuAutoHide == 1:
                    at quickMenuAppear

        # 자동 숨기기
        if persistent.showQuickMenu == 1:
            add quickShowHelper(600, 60) xysize(0, 0) pos (1.,1.)

        key "mousedown_4" action ShowMenu("history")
        key "mousedown_5" action ShowMenu("history")

        if renpy.get_screen("input") is None:
            key "K_l" action ShowMenu("history")
            key "K_p" action ShowMenu("preferences")
            if myInventory:
                key "K_i" action ToggleScreen('inventory')

    $ tooltip = GetTooltip('quick_menu')

    if persistent.showTooltip and (tooltip is not None):
        use tooltip(tooltip)


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound "audio/sfx/paper.mp3"

style quick_button_text:
    properties gui.text_properties("quick_button")

style quick_imagemap:
    activate_sound "audio/sfx/paper.mp3"
