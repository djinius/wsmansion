label ring_found:
    나 "반지를 찾았다!"
    return

label snowball_found:
    나 "눈 장식품을 찾았다!"
    return

label angel_found:
    나 "천사 조각상이다."
    return

label monkey_found:
    나 "원숭이상이다. 기괴하게 생겼네."
    return

label maria_found:
    나 "성모상이다. 성호경을 그어야 하나?"
    return

label camera_found:
    나 "옛날 방식 카메라인가?"
    나 "바닥에 뭔가 흐릿한 그림이 있네."
    나 "선명하게 볼 방법이 없을까?"

    call screen cameraMinigame
    $ found.append("photo")
    call screen exploreFound("photo")
    show screen exploreBase
    나 "사진이 한 장 나왔다. 엘리라는 그 애를 찍은 사진 같다."

    return