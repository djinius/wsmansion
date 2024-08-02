default itemDescriptions = {
    "gloves": "장갑은 빨간고무 목장갑이 최고야!",
    "tarotbook": "타로카드가 그려진 책.",
    "tornbook": "소설책 같다. 왜 페이지가 찢겨 있는지는 모르겠다.",
    "page1": "소설이 적혀 있는 페이지이다.",
    "sketchbook": "난 방학숙제가 싫어!",
    "camera": "골동품 카메라 같다.\n비싸게 팔 수 있지 않으려나?",
    "photo": "피사체로는 글래머 여성이 좋다.",
    "earring": "뱀이 꼬리를 물고 있는 모양의 귀걸이.",
    "page2": "소설이 적혀 있는 페이지이다.",
    "death": "사신이 그려진 타로 카드",
    "knife": "녹슨 칼.",
}

screen inventory():
    modal True
    
    default description = ""

    frame:
        align (.5, .5)
        has vbox

        hbox:
            xalign .5
            for o in myInventory:
                imagebutton:
                    auto "images/minigame/" + o + "_%s.png"
                    action SetScreenVariable("description", itemDescriptions[o])

        text description xalign .5 text_align .5

        textbutton "닫기" action Hide('inventory') xalign .5
