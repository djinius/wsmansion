# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define 난설 = Character('난설', color="#c8ffc8")
define 아비게일 = Character('아비게일', color="#c8ffc8")


# 여기에서부터 게임이 시작합니다.
label start:

    난설 "Canary Yellow의 2024년 여름 워크샵 게임입니다.."

    아비게일 "아나까나 까나리 까니 끼퍼웨!"

    난설 "꺄아~"

    menu:
        "당신은 누구십니까?"

        "소네트29!":
            난설 "환영해요, 스토리작가님."
        "命":
            아비게일 "그림작가님이시군요."
        "달납줄개":
            난설 "프로그래머다!"

    아비게일 "저희들에게 생명을 불어넣어 주세요."

    return
