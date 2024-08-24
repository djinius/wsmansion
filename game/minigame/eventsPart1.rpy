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
            font "OGRenaissanceSecret.ttf"
            size 45

    key "mouseup_1" action Return()
 

label glovesFound:
    $ addFoundHistory("장갑", "gloves")
    $ objectFound("gloves")
    play sound "audio/sfx/paper.mp3"
    call screen exploreFound("gloves", (914, 247))

    독백 "검은색 장갑이 놓여 있다. 혹시 모르니 일단 챙겨두자."
    return

label bookCompleted:
    play sound "audio/sfx/paper.mp3"
    call screen bookCompletion
    $ myInventory.remove("page1")
    $ myInventory.remove("page2")
    $ myInventory.remove("tornbook")
    $ objectFound("completeBook")
    play sound "audio/sfx/oldbook.mp3"
    call screen bookFound

    return

label page1Found:
    $ addFoundHistory("찢어진 책장", "page1")
    $ objectFound("page1")
    play sound "audio/sfx/paper.mp3"
    call screen exploreFound("page1", (795, 883))
    독백 "오래된 책의 일부 같다."

    if ("page2" in myInventory) and ("tornbook" in myInventory):
        call bookCompleted
        독백 "드디어 내용이 완성되었다!"
    elif ("tornbook" in myInventory):
        독백 "아직 한 페이지가 부족해 보인다…."
    elif ("page2" in myInventory):
        독백 "두 페이지 모두가 떨어져나온 원본이 있을 것이다."
    else:
        독백 "이것만 가지고서는 의미가 없어보인다. 더 찾아보자."

    call screen pageContents(page1Text)
    call bookStory

    return

label tornbookFound:
    $ addFoundHistory("페이지가 뜯겨나간 책", "tornbook")
    $ objectFound("tornbook")
    play sound "audio/sfx/oldbook.mp3"
    call screen exploreFound("tornbook", (549, 833))
    독백 "오래된 책이다. 페이지가 두 장 뜯겨나간 것 같다."

    if ("page1" in myInventory) and ("page2" in myInventory):
        call bookCompleted
        독백 "드디어 내용이 완성되었다."
    elif ("page1" in myInventory):
        독백 "아직 한 페이지가 부족해 보인다……."
    elif ("page2" in myInventory):
        독백 "아직 한 페이지가 부족해 보인다……."
    else:
        독백 "영어라 읽을 수는 없지만 이렇게 미완성으로 놔두기에도 어딘가 불편하다."

    call bookStory

    return

label cameraFound:

    if cameraTried is False:
        $ cameraTried = True
        $ addFoundHistory("카메라", "camera")
        독백 "오래된 카메라다. 무언가 보이는데 상이 흐릿하다……."

    play sound "audio/sfx/clock.mp3"
    call screen cameraMinigame

    if _return != 'complete':
        return

    $ objectRemove('camera')
    $ myInventory.append("photo")

    play sound "audio/sfx/alarm.mp3"
    call screen explorePhotoFound
    hide screen explore

label cameraStory:
    play music pain2
    # 배경: street1
    scene street1 with dissolve

    # 효과음: 인공적인 백색 소음

    독백 "나에게 있어 세상은 빈 도화지이다."
    독백 "사람들은 컵에 물이 절반밖에 없다고 슬퍼하면 안 된다고."
    독백 "그 시간에, 컵에 물이 절반이나 남았다고 기뻐해야 한다고 한다."
    독백 "나는 기뻐하지도, 슬퍼하지도 않는다."

    # 배경: street2
    독백 "세상은 아무것도 들어있지 않은 컵이고"
    독백 "텅 빈 도화지이며"
    독백 "아무 의미도 없는, 단체 사진 속 배경일 뿐이다."
    독백 "나에게 있어 세상이 그렇듯이, 세상도 나를 배경 취급했다."
    독백 "어쩌면 나는 애초부터 이 세상에 속하지 않았을지도 모른다."

    # 배경: 검은 화면, 빠르게 전환
    play music raining fadein 1.
    scene black

    독백 "사진에서 도려내도 아무런 상관없는 배경이니 말이다."
    독백 "오직 피사체를, 사진의 주인공을 돋보이게 하기 위해 존재할 뿐인."
    독백 "난 이런 삶을 포기할 작정이었고, 그에 걸맞는 배경은 내가 고르고 싶었다."

    # 효과음: 인공적인 백색 소음에서 빗소리로 전환
    # 배경: home_bnw
    scene home_bnw with dissolve

    독백 "빗줄기를 맞아가며 숲속을 헤매다 보니 오래된 저택이 드러났다."
    독백 "안개 자욱한 날, 학교 뒷산 숲에서 간간히 나타난다는 소문만 들었던 저택이다."
    독백 "아마 여기서 영원히 돌아가지 못할 수도 있겠다고 생각했다. 완벽했다."

    # 엘리 (보통, 미카놀람, 무표정)
    show 엘리 눈썹보통 눈미카놀람 입무표정:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    play sound "audio/sfx/dooropen.mp3"

    엘리 "……누구시죠."
    
    독백 "…불쾌함을 감추지 않은 채 저택 내부에서 문을 열어주는 장발의 소녀."
    독백 "예상치 못한 등장에 당황한 나는 대답 대신 멋쩍게 웃어 보였다."
    독백 "유령이 나온다는 말은 듣지 못했다. 유령치고는 너무 실체감 있기도 하고…."

    # 엘리 (보통, 침울, 무표정)
    엘리 눈썹보통 눈침울 입무표정 "이만 돌아가세요. 당신 같은 사람이 있을 곳이 아니에요."
    독백 "빗소리가 깔린 긴 침묵 속, 서로를 마주한 채 제 자리를 오도카니 지키던 두 사람."

    stop music
    
    독백 "소녀의 작은 한숨 소리를 신호로, 나는 내 마지막을 함께할 저택에 발을 디뎠다."

    scene black with dissolve

    return

label ellyPart1:
    $ toReturn = None
    hide screen explore

    if "photo" in myInventory:
        scene black
        show 엘리 눈썹보통 눈웃음 입미소:
            pos (.5, .05) anchor (.5, .0)
            zoom .5
        with dissolve

        menu:
            "엘리를 부르기 전, 조금 더 살펴볼까?"

            "그러자":
                pass

            "이만하면 충분한 것 같다.":
                $ toReturn = "Finished!!"

    else:
        scene black
        show 엘리 눈썹보통 눈웃음 입미소:
            pos (.5, .05) anchor (.5, .0)
            zoom .5
        with dissolve

        엘리 "무슨 일이시죠? 제가 도와드릴 일이 있나요?"
        독백 "엘리는 아직 미덥지 못하다. 조금만, 조금만 더 혼자서 살펴보자."
        엘리 눈실눈웃음1 "무언가 필요하시다면 언제든 부르세요!"

    scene black with dissolve

    return toReturn
