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
    yoffset 60
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

default quickMenuAutoHide = 3

screen quick_menu():

    ## 다른 화면 위에 표시되는지 확인합니다.
    zorder 100

    if isQuickVisible():

        $ tooltip = GetTooltip('quick_menu')

        if persistent.showTooltip and (tooltip is not None):
            use tooltip(tooltip)

        imagemap:
            align (1., 1.)

            if not _in_replay:
                auto ("gui/quickmenu/%s.png")
            else:
                auto ("gui/quickmenu/replay_%s.png")
            hotspot (  0, 0, 60, 60):
                action ShowMenu('history')
                if _in_replay:
                    tooltip ["대사록({u}{color=008}L{/color}{/u})", "지나간 대사를 다시 열람합니다.", (1920 - 60 * 8 - 30, 1020), (.5, 1.)]
                else:
                    tooltip ["대사록({u}{color=008}L{/color}{/u})", "지나간 대사를 다시 열람합니다.\n대사록의 대사를 클릭해 해당 시점으로\n되돌아갈 수 있습니다.", (1920 - 60 * 8 - 30, 1020), (.5, 1.)]

            if not _in_replay:
                hotspot ( 60, 0, 60, 60):
                    action Show('inventory')
                    sensitive myInventory
                    tooltip ["소지품({u}{color=008}I{/color}{/u})", "소지품을 확인합니다.", (1920 - 60 * 7 - 30, 1020), (.5, 1.)]

            if not isQuickExploring():
                hotspot (180, 0, 60, 60):
                    action Preference("auto-forward", "toggle")
                    tooltip ["자동 진행", "대사를 자동으로 진행합니다.", (1920 - 60 * 5 - 30, 1020), (.5, 1.)]
                hotspot (240, 0, 60, 60):
                    action Skip()
                    tooltip ["빠르게 진행({u}{color=008}TAB{/color}{/u})", "대사를 빠르게 진행합니다.", (1920 - 60 * 4 - 30, 1020), (.5, 1.)]
                hotspot (300, 0, 60, 60):
                    action Skip(fast=True, confirm=False)
                    tooltip ["건너뛰기", "다음 선택지, 혹은 다음 장면까지 건너뜁니다.", (1920 - 60 * 3 - 30, 1020), (.5, 1.)]
                    
            if not _in_replay:
                hotspot (360, 0, 60, 60):
                    action ShowMenu('save')
                    tooltip ["저장({u}{color=008}S{/color}{/u})", "현재 게임을 저장합니다.", (1920 - 60 * 2 - 30, 1020), (.5, 1.)]
            else:
                hotspot (360, 0, 60, 60):
                    action EndReplay(confirm=False)
                    tooltip ["다시보기 끝", "다시보기를 끝내고 돌아갑니다.", (1920 - 60 * 2 - 30, 1020), (.5, 1.)]
            hotspot (420, 0, 60, 60):
                action ShowMenu('preferences')
                tooltip ["설정({u}{color=008}P{/color}{/u})", "화면 모드 및 음량, 기타 게임을 진행하기 위한\n편의사항을 설정합니다.", (1920, 1020), (1., 1.)]
            hotspot (480, 0, 60, 60):
                action HideInterface()
                tooltip ["숨기기({u}{color=008}H{/color}{/u})", "게임 인터페이스를 숨깁니다.", (1920, 1020), (1., 1.)]

            # 자동 숨기기
            if persistent.showQuickMenu == 1:
                add quickShowHelper() xysize(0, 0) pos (1.,1.)

                if quickMenuAutoHide == 0:
                    at quickMenuHidden
                elif quickMenuAutoHide == 1:
                    at quickMenuAppear
                    timer 1. action SetVariable("quickMenuAutoHide", 2)
                elif quickMenuAutoHide == 2:
                    at quickMenuFix
                elif quickMenuAutoHide == 3:
                    at quickMenuHide
                    timer 2.5 action SetVariable("quickMenuAutoHide", 0)
                elif quickMenuAutoHide == 4:
                    at quickMenuReappear
                    timer .5 action SetVariable("quickMenuAutoHide", 2)

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
