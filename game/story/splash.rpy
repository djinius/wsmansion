default persistent.splashPlayed = False
default splashPhase = False

label splashscreen:
    $ splashPhase = True

label splashReplay:
    scene black with dissolve

    if (not _in_replay) and (persistent.replayPrologue is False):
        return

    pause 1.5

    show text "{size=+10}HISTORY, WITH HER VOLUMES VAST,\nHATH BUT ONE PAGE.{/size}":
        align (.85, .85)
    with dissolve
    pause .2

    scene black with dissolve
    pause 1.5

    scene apricot with dissolve
    독백 "감은 눈 사이로 빛이 녹아들었다."
    독백 "나는 따사로운 햇살을 받으며 한껏 나른해진 몸을 일으켰다."

    scene sculpt with dissolve

    독백 "들판 이곳저곳에 서 있는 조각상들."
    독백 "그 조각상들의 표면을 타고 흐르는, 은은한 석양빛이 눈에 띄었다."
    독백 "벌써 시간이 이렇게 됐나 싶었다."
    독백 "그런데, 어디로 가야 했지?"
    독백 "잠깐."
    독백 "내 집이 어디였더라?"

    # 배경: sculpt -> sculpt_blur
    scene sculpt_blur with dissolve
    play music pain1

    독백 "나는 {i}누구{/i}고?"
    독백 "정신없이 주머니를 뒤적였지만, 전화기는커녕 내 이름이 써진 물건조차 없었다."

    # 배경: sculpt_blur -> sculpt_noise
    scene sculpt_noise

    독백 "조각상들이 흐드러진 들판 위, 나 자신을 증명해 줄 수 있는 건 아무것도 없었다."
    독백 "모든 기억을 잃어버렸다는 사실이 당황스러웠다. 숨이 막혔다."
    독백 "그러자 내게 보인 장엄하고 거대한 무언가."

    stop music

    # 배경: sculpt_noise -> home)
    scene home with dissolve

    독백 "허름하고 어딘가 음산한 기운까지 감도는 저택이다."
    독백 "내가 살던 집일 리가 없었다. 아무리 기억을 잃었다지만,\n그렇다 해도 분명 어느 부잣집 소유의 여름 별장일 터."
    독백 "사유지라는 사실이 마음에 걸리긴 했지만,"
    독백 "…안에 사람이 있다면 적어도 도움은 받을 수 있지 않을까."

    # 배경: door
    scene door with dissolve

    독백 "초인종은 고장난 것 같고, 문은 아무리 두드려도 인기척이 없다."
    독백 "포기하려던 찰나 문틈 사이가 살짝 벌어져 있는 것을 발견했다."
    독백 "들어가도 될까? 뭐라고 설명해야 하지? 긴급 상황이니까 이해해 주려나?"
   
    # ( 끼이익- 하는 사운드 이펙트 )
    # 배경: door -> living
    play sound "audio/sfx/dooropen.mp3"
    scene living with dissolve

    독백 "아무것도 안 하는 것보단 낫기에 들어왔는데, 역시나 아무도 없었다."
    독백 "저택의 외관처럼 가구들도, 장식품들도 오래된 것들 뿐이었다."
    독백 "동시에 이렇게까지 깔끔할 수 있다는 사실에 또 한 번 놀랐다."
    독백 "부잣집일 테니 청소 업체가 다녀가는 도중 문단속을 깜박했을까."
    독백 "아니, 전문적인 업체에서 애초에 그런 기본적인 실수를 저지를 리가 없었다."
    독백 "그렇게 생각하니 소름이 돋았다. 한시 빨리 이곳에서 빨리 나가고 싶어졌다."
    독백 "나는 다시 현관으로 발을 옮겼다 -"

    # ( ‘턱’ 하는 사운드 이펙트 )
    scene black with Dissolve(.1)
    # 배경: living -> 검은 화면 (빠르게)
    아비게일처음 "정말, 그렇게 함부로 돌아다니면 못 쓴다니까요."
    독백 "그 순간, 누군가 가냘픈 손으로 나를 잡아당겼다."

    # 배경: 검은 화면 -> 타이틀 화면 CG
    scene title with dissolve

    독백 "…신비한 저택에서 홀로 살고 있는 소녀가."

    # 타이틀 화면으로 완전 전환 후 게임 시작

label splashFinished:
    $ persistent.splashPlayed = True
    $ persistent.skyBackground = False

    return

