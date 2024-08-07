define page1Text = """
…바람은 여전히 우리 배의 선미루에 머물고 있다.
배에 수많은 돛이 올려져 있기 때문에 이따금
선체가 바닷물 위로 들어 올려지기도 한다.
오, 무시무시하고도 또 무시무시하구나!
빙벽이 갑자기 오른쪽으로 열리고, 이어 다시 왼쪽으로 열린다.
그리고 우리는 거대한 동심원을 그리며 현기증 나는 속도로
거대한 원형극장의 가장자리를 선회한다.
그 원형극장의 벽은 꼭대기가 너무 높아 어둠 속에 잠긴 채 보이지 않는다.
다가올 내 운명에 대해 심사숙고할 시간이 별로 남지 않은 것 같다.
원이 급속도로 작아진다.
우리의 배는 소용돌이의 손아귀 안으로 미치광이 같은 기세로 내동댕이쳐진다.
배는 고함을 지르고 우르릉대며 천둥 번개를 울려 대는
대양과 폭풍의 한가운데에서 선체를 떨고 있다.
오, 주여! 우린 추락하고 있다.
"""

default cameraTried = False

screen pageContents(textContent):
    modal True

    frame:
        align (.5, .5)
        padding (50, 20)
        background Frame("images/etc/paper.jpg")

        text textContent:
            align (.5, .5)
            text_align .5
            color "#000"
            font "GowunBatang-Regular.ttf"

    key "mouseup_1" action Return()
 

label glovesFound:
    $ addFoundHistory("장갑", "gloves")
    $ objectFound("gloves")
    call screen exploreFound("gloves")

    독백 "검은색 장갑이 떨어져 있다. 혹시 모르니 일단 챙겨두자."
    return

label page1Found:
    $ addFoundHistory("찢어진 책장", "page1")
    $ objectFound("page1")
    call screen exploreFound("page1")
    독백 "오래된 책의 일부 같다."
    독백 "영어라 읽기도 힘들뿐더러 한 장만으로는 의미가 없어 보인다."

    call screen pageContents(page1Text)
    call bookStory

    return

label tornbookFound:
    $ addFoundHistory("페이지가 뜯겨나간 책", "tornbook")
    $ objectFound("tornbook")
    call screen exploreFound("tornbook")
    독백 "오래된 책이다. 페이지가 두 장 뜯겨나간 것 같다."
    독백 "영어라 읽을 수는 없지만 이렇게 미완성으로 놔두기에도 어딘가 불편하다."

    call bookStory

    return

label cameraFound:

    if cameraTried is False:
        $ cameraTried = True
        $ addFoundHistory("카메라", "camera")
        독백 "옛날 방식 카메라인가?"
        독백 "바닥에 뭔가 흐릿한 그림이 있네."
        독백 "선명하게 볼 방법이 없을까?"

    call screen cameraMinigame

    if _return != 'complete':
        return

    $ objectFound('camera')
    $ myInventory.append("photo")
    call screen explorePhotoFound
    hide screen exploreBase

label cameraStory:
    # 배경: 길거리 사진, 흑백에 블러 처리
    scene black
    show text "길거리":
        align (.0, .0)
    with dissolve

    # 효과음: 인공적인 백색 소음

    독백 "나에게 있어 세상은 빈 도화지이다."
    독백 "사람들은 컵에 물이 절반밖에 없다고 슬퍼하면 안 된다고 한다."
    독백 "그 시간에, 컵에 물이 절반이나 남았다고 기뻐해야 한다고 한다."
    독백 "나는 기뻐하지도, 슬퍼하지도 않는다."
    독백 "세상은 아무것도 들어있지 않은 컵이고"
    독백 "텅 빈 도화지이며"
    독백 "아무 의미도 없는, 단체 사진 속 배경일 뿐이다."
    독백 "나에게 있어 세상이 그렇듯이, 세상도 나를 배경 취급했기에."
    독백 "사진에서 도려내도 아무런 상관없는 배경."
    독백 "어쩌면 나는 애초부터 이 세상에 속하지 않았을지도 모른다."
    독백 "피사체를 돋보이게 할 뿐인 배경이 얼마나 뿌옇든 누가 신경이나 쓰던가."

    # 배경: 검은 화면, 빠르게 전환
    scene black

    독백 "그렇다면, 다른 세상이 있다면, 나는 또렷한 하나의 피사체가 될 수 있었을까?"
    독백 "무채색의 흐릿한 배경 따위가 아니라?"

    # 효과음: 인공적인 백색 소음에서 빗소리로 전환
    # 배경: 저택 (흑백 필터, 블러 약간)
    scene black
    show text "저택":
        align (.0, .0)
    with dissolve

    독백 "빗줄기를 맞아가며 숲속을 헤매다 보니, 괴담과 소문만 무성했던 대저택이 드러났다."
    독백 "아마 여기서 영원히 돌아가지 못할 수도 있겠지. {i}그럴 생각이었다.{/i}"

    # 엘리 (놀람, 놀람, 무표정)
    엘리 "……누구시죠."
    독백 "그러자 불쾌함을 감추지 않은 채 문을 열어주는 장발의 소녀."
    독백 "예상치 못한 상황에 당황한 나는 대답 대신 멋쩍게 웃어 보였다."

    # 엘리 (난처, 원망, 무표정)
    엘리 "이만 돌아가세요. 당신 같은 사람이 있을 곳이 아니에요."
    독백 "빗소리가 깔린 긴 침묵 속,"
    독백 "서로를 마주한 채 나와 소녀는 제 자리를 오도카니 지켰다."
    독백 "소녀의 작은 한숨 소리를 신호로, 나는 내 마지막을 함께할 저택에 발을 디뎠다."

    return