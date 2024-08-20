define itemDescriptions = {
    "gloves": ("장갑", "검은 가죽 장갑이다."),
    "tornbook": ("책", "내용을 알 수 없는 책.\n나머지 페이지는 어디 갔을까?"),
    "page1": ("찢어진 페이지", "영어로 된 페이지라 읽을 수가 없다.\n어디서 떨어져나온 걸까."),
    "camera": ("골동품 카메라", "빛 바랜 사진이 들어 있던 골동품 카메라이다."),
    "photo": ("사진", "어딘가 쓸쓸해 보이는 소녀가 담긴 빛 바랜 사진이다."),
    "page2": ("찢어진 페이지", "영어로 된 페이지라 읽을 수가 없다.\n어디서 떨어져나온 걸까."),
    "frag0": ("거울 조각", "베이지 않게 조심해서 만지자."),
    "frag1": ("거울 조각", "베이지 않게 조심해서 만지자."),
    "frag2": ("거울 조각", "베이지 않게 조심해서 만지자."),
    "frag3": ("거울 조각", "베이지 않게 조심해서 만지자."),
    "frag4": ("거울 조각", "베이지 않게 조심해서 만지자."),
    "completeBook": ("완성된 책", "모두 완성된 묵직하고, 기이한 느낌이 드는 책.\n저택을 처음 보았을 때도 이런 느낌을 받았지."),
    "ballet": ("목이 떨어진 발레리나 인형", "엘리한텐 뭐라고 말해야 하나…….")
}

screen inventory():
    modal True

    style_prefix "inventory"
    
    frame:
        align (.5, .5)

        has vbox

        label "소지품"

        grid 2 6:
            xalign .5

            for o in myInventory:
                hbox:
                    add "gui/minigame/" + o + "_idle.png" yalign .5
                    vbox:
                        yalign .5
                        text itemDescriptions[o][0] size 25
                        text itemDescriptions[o][1] size 20 yminimum 50

        textbutton "닫기" action Hide('inventory') xalign .5

style inventory_frame:
    padding (20, 12)

style inventory_hbox:
    spacing 5

style inventory_vbox:
    align (.0, .5)
    spacing 5

style inventory_label:
    xalign .5

style inventory_label_text:
    color "#ff4400"

style inventory_text:
    color "#FFFFFF"

style inventory_button_text is button_text:
    idle_color "#FFFFFF"
    hover_color "#ff4400"
