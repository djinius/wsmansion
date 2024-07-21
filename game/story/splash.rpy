image apricot = Solid("#FBCEB1")

label splashscreen:
    scene black with dissolve

    pause 1.5

    show text "{size=+10}HISTORY, WITH HER VOLUMES VAST,\nHATH BUT ONE PAGE.{/size}":
        align (.85, .85)
    with dissolve
    pause 2.
    scene black with dissolve
    pause 1.5

    scene apricot with dissolve
    나 "감은 눈 사이로 빛이 녹아든다."
    나 "따스하다. 왜 나는 이렇게 양지바른 곳에 누워 있는 걸까."

    scene black
    show text "조각상 이미지":
        align (.5, .5)
    with dissolve

    나 "막 눈을 뜬 내 이목을 끈, 제각기 영동적인 포즈를 취하며 석양빛을 은은하게 반사하는 조각상들."
    나 "벌써 시간이 이렇게 됐나. 너무 어두워지기 전에 빨리 집으로 -"
    나 "･･････어디로 가야 했더라?"
    나 "애초에, 내 집이 어디지?"

    # 배경: 조각상 -> 조각상 (블러)
    scene black
    show text "조각상 이미지 블러":
        align (.5, .5)
    with dissolve

    나 "나는 누구고?"
    나 "정신없이 주머니를 뒤적였지만 전화기는 물론이고, 내 이름이 써진 물건 하나조차 없었다."
    나 "나는 모든 기억을 잃어버린 채, 조각상들이 흐드러진 들판에 누워있었다."
    나 "당황한 채 고개를 두리번거리던 나는, 주위에서 거대한 저택을 발견했다."

    # 배경: 조각상 (블러) -> 저택 외부 (노랗고 빈티지한 필터)
    scene black
    show text "저택 외부":
        align (.5, .5)
    with dissolve

    나 "딱 봐도 오래된 저택이다, 어느 부잣집 소유 별장인가."
    나 "사유지라는 사실이 마음에 걸리긴 했지만, 안에 사람이 있다면 적어도 도움은 받을 수 있을 터다."

    # 배경: 저택 외부 이미지에서 문(입구) 부분 확대
    scene black
    show text "저택 문 줌인":
        align (.5, .5)
    with dissolve

    나 "･･･초인종은 고장났고, 문을 아무리 두드려 봐도 인기척이 없다."
    나 "포기하려던 찰나 문틈 사이가 살짝 벌어져 있는 것을 발견했다."
    나 "이건 긴급 상황이니까. 나는 속으로 되뇌이며 조심히 문을 열고 들어갔다."

    # ( 끼이익- 하는 사운드 이펙트 )
    # 배경: 저택 문 -> 저택 응접실
    scene black
    show text "응접실":
        align (.5, .5)
    with dissolve

    나 "역시나 아무도 없었다."
    나 "하나 기이한 점은, 분명 오래된 가구들과 장식품들임에도 저택 내부가 새것 처럼 깔끔하다는 것이다."
    나 "웬만한 골동품 가게에서도 보기 힘든 물건들인데도 말이다."
    나 "청소 업체가 다녀가면서 문단속을 깜박했나? 모두 완벽하게 해 놓고서 그런 실수라니."
    나 "도와줄 사람을 찾으러 나는 다시 현관으로 발걸음을 옮겼다."

    # ( ‘턱’ 하는 사운드 이펙트 )
    scene black with dissolve
    # 배경: 저택 응접실 -> 검은 화면 (빠르게)
    아비게일처음 "정말, 그렇게 함부로 돌아다니면 못 쓴다니까요."
    나 "그러자 누군가 나의 옷깃을 잡았다."
    # 배경: 검은 화면 -> 타이틀 화면 CG
    scene black
    show text "대충 타이틀화면":
        align (.5, .5)
    with dissolve

    나 "신비한 저택에서, 홀로 살고 있는 소녀가."

    # 타이틀 화면으로 완전 전환 후 게임 시작

    return

