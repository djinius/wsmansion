# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define 나 = Character(None)
define 난설 = Character('난설', color="#C5CAB6")
define 아비게일 = Character('아비게일', color="#FFDF01")

label splashscreen:
    scene black with dissolve

    show text "{size=+10}두 날개는 녹슬지 않는다.{/size}" with dissolve
    pause 3.

    scene black with dissolve

    난설 "Canary Yellow의 2024년 여름 워크샵 게임입니다."
    나 "눈을 떠 보니 대저택 안뜰이다."
    난설 "똑똑."
    아비게일 "뿌지직."
    난설 "지금부터 게임이 시작됩니다."

    return

# 여기에서부터 게임이 시작합니다.
label start:

    아비게일 "홍차 마셔."
    아비게일 "나는 햇빛에 약해."
    난설 "선짓국 좋아해?"
    아비게일 "응."
    나 "얘 흡혈귀 아니야?"
    나 "집 안을 조사해 보자."

label explore:
    $ moveDirection = None
    call screen exploreMap

    if _return == "Finished!!":
        jump continueStory

    $ foundObject = _return
    $ objectFound(foundObject)
    call screen exploreFound(foundObject)

    show screen exploreBase
    call expression foundObject + "_found"

    if objects:
        jump explore

label continueStory:
    if objects:
        난설 "못 찾은게 있는 듯 한데."
    else:
        난설 "전부 찾았어요."

    hide screen explore
    난설 "두번째 이야기를 시작해 볼까요?"

    menu:
        "당신은 누구십니까?"

        "소네트29!":
            난설 "환영해요, 스토리작가님."
        "命":
            아비게일 "그림작가님이시군요."
        "달납줄개":
            난설 "프로그래머다!"

    아비게일 "우리들에게 생명을 불어넣어 줘."
    아비게일 "세번째 이야기로 들어가 보자."

    난설 "끝!"

    return
