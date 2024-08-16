default persistent.showCTC = True

## Say 스크린 #####################################################################
##
## Say 스크린은 플레이어에게 대사를 출력할 때 씁니다. 화자 who와 대사 what, 두
## 개의 매개변수를 받습니다. (화자 이름이 없으면 who는 None일 수 있음)
##
## 이 스크린은 id "what"을 가진 텍스트 디스플레이어블을 생성해야 합니다. (이 디
## 스플레이어블은 렌파이의 대사 출력에 필요합니다.) id "who" 와 id "window" 디스
## 플레이블이 존재할 경우 관련 스타일 속성이 적용됩니다.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## 사이드 이미지가 있는 경우 글자 위에 표시합니다. 휴대폰 환경에서는 보이지
    ## 않습니다.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Character 객체를 통해 스타일을 지정할 수 있도록 namebox를 사용할 수 있게 만듭
## 니다.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input 스크린 ###################################################################
##
## 플레이어 입력을 받는 renpy.input을 출력할 때 쓰이는 스크린입니다. prompt 매개
## 변수를 통해 입력 지문을 표시할 수 있습니다.
##
## 이 스크린은 id "input"을 가진 input 디스플레이어블을 생성해야 합니다.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input" color "#FFF"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

image mouseLeftClick = Animation("gui/cursors/mouse_unclicked.png", .5, "gui/cursors/mouse_leftclicked.png", .5,)
image mouseRightClick = Animation("gui/cursors/mouse_unclicked.png", .5, "gui/cursors/mouse_rightclicked.png", .5,)

## 자동 숨기기/보이기 트랜스폼
transform ctcHidden():
    offset (-20, -10)

transform ctcAppear():
    offset (-20, -10)
    easein 1. offset (-20, -70)

transform ctcFix():
    offset (-20, -70)

transform ctcReappear():
    easein .5 offset (-20, -70)

transform ctcHide():
    offset (-20, -70)
    pause 1.5
    easein 1. offset (-20, -10)

default showCTC = False

screen ctc:
    style_prefix "ctc"

    if persistent.showCTC:
        if splashPhase:
            hbox:
                align (1., 1.) offset (-20, -10) spacing 15
                add "mouseLeftClick"
                text "진행"

                if persistent.splashPlayed:
                    textbutton "건너뛰기":
                        idle_foreground "gui/quickmenu/skip_idle.png"
                        hover_foreground "gui/quickmenu/skip_hover.png"
                        padding (42, 26, 0, 0)
                        action Jump("splashFinished")

        elif renpy.get_screen('nvl') is None:
            # on "show" action SetVariable("showCTC", True)
            # on "hide" action SetVariable("showCTC", False)
            hbox:
                align (1., 1.)
                spacing 20

                hbox:
                    add "mouseLeftClick"
                    text "진행"

                hbox:
                    add "mouseRightClick"
                    text "게임 메뉴"

                if persistent.showQuickMenu == 0:
                    at ctcHidden
                elif persistent.showQuickMenu == 1:
                    if quickMenuAutoHide == 0:
                        at ctcHidden
                    else:
                        at ctcFix
                else:
                    at ctcFix

style ctc_hbox:
    spacing 5

style ctc_text:
    size 20
    color "#FFF"
    font "fonts/NEXON Lv2 Gothic Medium.ttf"
    yalign 1.
    outlines [(1, "#000000", 0, 0)]

style ctc_button_text is button_text:
    size 20
    font "fonts/NEXON Lv2 Gothic Medium.ttf"
    yalign 1.
    idle_color "#FFF"
    hover_color "#F40"
    outlines [(1, "#000000", 0, 0)]