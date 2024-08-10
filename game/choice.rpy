## Choice 스크린 ##################################################################
##
## menu 명령어로 생성된 게임내 선택지를 출력하는 스크린입니다. 한 개의 매개변수
## items를 받고, 이는 선택지 내용(caption)과 선택지 결과(action)이 있는 오브젝트
## 가 들어있는 리스트입니다.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

transform choiceAppear(delay=.0):
    xpos .5 xanchor .0 alpha .0 xoffset 200
    pause delay
    easein .5 alpha 1. xanchor .5 xoffset 0

screen choice(items):
    style_prefix "choice"

    vbox:
        for n, i in enumerate(items):
            textbutton i.caption action i.action at choiceAppear(n * .25)


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 605
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


