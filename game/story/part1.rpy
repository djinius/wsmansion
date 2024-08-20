transform partmagnify:
    align (.5, .5) zoom 1.
    linear .5 align (.5, .75) zoom 2.

transform partmagnifyrevert:
    align (.5, .75) zoom 2.
    linear .5 align (.5, .5) zoom 1.

label part1:

    play music tranquil1
    scene living with dissolve

    독백 "……."
    독백 "푹신한 소파에 앉아 주위를 둘러본다."
    독백 "아무리 생각해도 의문이다. 당장 이 저택부터 그렇다."
    독백 "바깥부터 내부까지, \n고풍스러운 걸 넘어 과거의 유물 같은 곳이다."
    독백 "가구는 물론 전등에 액자까지, 웬만한 골동품 가게에서도 보기 힘든 물건들로 빼곡하다."
    독백 "그런데도 먼지 몇 톨 떠다니는 걸 빼면 깔끔하다 못해 쾌적함이 느껴진다."
    독백 "여기 주인은 대체 뭐 하는 사람이고, 날 맞아준 저 소녀와는 무슨 관계일까?"

    # 엘리 등장
    # 소녀? (보통, 웃음, 미소)
    show 아비게일처음 눈썹보통 눈웃음 입미소:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve
    아비게일처음 "많이 기다리셨죠, 손님 응대는 정말 오랜만이라서요."

    독백 "소녀가 찻잔에 음료를 따라 가져왔다."
    독백 "목이 말랐던 나는 입을 데지 않게 내용물을 천천히, 부드럽게 들이켰다."
    독백 "그러자 내 목구멍을 때리는 홍차답지 않은 시원한 감각."
    독백 "달다 못해 아려오는 혀끝에 솨- 하고 올라오는 탄산까지."
    독백 "살면서 콜라를 찻잔에 담아 오는 사람은 처음 봤다. "
    독백 "일부러 날 골탕 먹일 셈이었던 건지, 연신 기침을 하는 날 보며 입을 가리고선 웃음을 참는 소녀."
    # 소녀? (난처, 실눈 웃음, 큰 웃음)
    아비게일처음 눈썹난처 눈실눈웃음1 입큰웃음 "푸후훗, 아, 죄송, 죄송해요. 그렇게까지 반응이 격할 줄은 몰라서."

    독백 "부잣집 아가씨치고는 참으로 맹랑한 태도에 헛웃음이 났다."
    독백 "초면이지만 어째서인지 미워할 수는 없었다. 귀여워서 그런가."
    독백 "그리고 이제 다시 보니, 소녀의 옷도 예스럽기 그지없다."

    # ( 소녀(엘리)의 scg 확대 - '옷 부분 위주로' )
    show layer master at partmagnify
    pause 1.

    독백 "고전 흑백 영화에서나 나올 법한 옷차림임에도 촌스러움과는 거리가 멀었다."
    독백 "어쩌면 이것이 상류층의 기품이란 걸지도."
    독백 "소녀는 잔 속의 콜라를 조심히 홀짝이고선 입을 열었다."

    show layer master at partmagnifyrevert
    pause 1.

    # 소녀? (보통, 웃음, 무표정, scg 다시 축소)
    아비게일처음 눈썹보통 눈웃음 입무표정 "그럼, 실례가 아니라면 무슨 용건이신지 설명을 부탁드려도 될까요."
    독백 "…대답할 길이 없었다."
    독백 "여기에 어떻게 왔는지, 심지어 내가 누군지 조차 모른다. \n너무 단순해서 설명할 수 없는 처지를 과연 누가 믿어주겠는가."
    # 소녀? (보통, 웃음, 미소)
    아비게일처음 입미소 "음…무언가 말로는 못 할 사정이 있으신 것 같은데, 맞나요?"
    독백 "그러자, 소녀는 내게 의심의 눈초리 대신 따스한 미소를 건네주었다."
    독백 "고개를 끄덕이자 소녀의 미소가 더욱 밝아졌다."
    # 소녀? (행복, 실눈 웃음, 큰 웃음)
    아비게일처음 눈썹행복 눈실눈웃음 입큰웃음 "후훗, 그래도 너무 걱정하지는 마세요. "
    아비게일처음 "여기가 산골 부근이라, 길을 잃은 등산객분들께서 가끔 찾아오시거든요."
 
    # 소녀? (침울, 슬픔, 무표정)
    아비게일처음 눈썹침울 눈침울 입무표정 "오히려 도와드릴 게 없어 죄송합니다."
    아비게일처음 "보시다시피 전부 구식이라 바깥과 연락할 수단도 시원찮고, \n비상 연락망도 마침 고장이라…. 면목 없네요."

    # 엘리 퇴장
    stop music
    hide 아비게일처음 with dissolve

    독백 "이해한다는 의미로 고개를 저었다."
    독백 "오히려 감사해야 할 쪽은 나였다, 의심받아도 모자랄 상황에 융숭한 대접이라니."
    독백 "…순간적으로 스치는 미심쩍은 느낌에 나는 다시 자리를 고쳐 앉았다."

    # 엘리 등장
    # 소녀? (난처, 놀람, 무표정)
    show 아비게일처음 눈썹난처 눈미카놀람 입무표정:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve
    아비게일처음 "무슨 일이시죠? 어디 다치기라도 하신 건가요?"
    
    # 엘리 퇴장
    hide 아비게일처음 with dissolve

    play music strain

    독백 "예로부터 모르는 사람의 이유 없는 환대에는 대부분 구린 이유가 있다."
    독백 "내가 기억을 잃었고, 그 이유조차 모르는 상황에서는 더더욱."
    독백 "지금 비상 연락망이 끊어진 건 그렇다 치자. 그럼 왜 먼저 그 이야기를 꺼냈을까? 전화기를 잃어버렸다는 걸 미리 알고 있었나?"
    독백 "또 ‘말 못할 상황’인건 어떻게 알고 있었지?"

    # 소녀? (행복, 실눈 웃음, 미소)
    show 아비게일처음 눈썹행복 눈실눈웃음1 입미소:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    아비게일처음 "……우후훗."
    # 소녀? (음영 on, 행복, 실눈 웃음, 미소)
    아비게일처음 눈썹행복 눈실눈웃음1 입미소 음영있음 "결국 들켜버렸나요. 그럼 자, 순순히 이리로 오세요…."

    독백 "소녀의 삐죽하고 날카로운 덧니가 반짝이고, \n빈 찻잔과 소녀의 모습이 눈앞에 아른거렸다."
    stop music

    # 배경: 검은 화면
    scene black
    독백 "이런 상황일수록 조심했어야 했는데,"

    # 소녀? 
    아비게일처음 "크왕!"
    scene living
    # 소녀? (놀람, 실눈 웃음, 큰 웃음)
    show 아비게일처음 눈썹놀람 눈실눈웃음1 입큰웃음:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    독백 "순간적으로 놀라 움츠러든 내 앞에 소녀가 크게 입을 벌리고 있었다."
    독백 "양팔을 벌리고, 모든 손가락을 맹수처럼 세우고서 말이다."
    # 소녀? (놀람, 놀람, 무표정)
    아비게일처음 눈썹놀람 눈미카놀람 입무표정 "예? 어라… 저만 그 생각 한 건가요?"
    # 소녀? (행복, 웃음, 무표정)
    아비게일처음 눈썹행복 눈웃음 입무표정 "흐음, 수상한 대저택에 홀로 사는 창백한 주인아씨에, 튀어나온 송곳니까지."
    # 소녀? (행복, 실눈 웃음, 큰 웃음)
    아비게일처음 눈실눈웃음1 입큰웃음 "상황이 딱 봐도 흡혈귀잖아요, 흡혈귀. 크와앙!"

    play music tranquil1
    독백 "나는 멋쩍게 웃어 보이는 걸로 대답을 대신했다."
    독백 "전혀 예상하지는 못했지만, 썩 귀여운 장난이었다."
    독백 "부끄러워 얼굴을 붉히는 기색도 없이 다시 신비로운 분위기로 돌아간 걸로 보아, 콜라도 그렇고 제 나이대에 맞게 장난을 좋아하는 편인가, 하고 생각했다."

    # 엘리 (행복, 웃음, 미소)
    아비게일처음 눈썹행복 눈웃음 입미소 "그럼 다시, 지금까지의 실례를 무릅쓰고."
    hide 아비게일처음
    show 아비게일 눈썹행복 눈웃음 입미소:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    아비게일 "처음 뵙겠습니다, 제 이름은 아비게일 F. 엘리엇."
    아비게일 "잠시 요양 중인 엘리엇 가의 차녀랍니다. 편하게 줄여서 ‘애비’라고 불러주세요."

    독백 "……."
    # 엘리 (난처, 실눈 웃음, 미소)
    hide 아비게일
    show 엘리 눈썹난처 눈실눈웃음1 입미소:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    엘리 "…역시 그건 좀 아니겠지요? 음, 엘리엇에서 따서, ‘엘리’가 좋겠어요."

    독백 "두 음절짜리 단어의 울림이 신기한 듯, 소녀는 몇 번이고 오물거렸다."

    #엘리 (행복, 웃음, 미소)
    엘리 눈썹행복 눈웃음 입미소 "엘리, 엘리. {i}엘리{/i}…. 후훗. 역시 마음에 들어요."
    엘리 "그럼 머무시는 동안이라도 집처럼 편하게 계세요."
    엘리 "아, 무슨 일 있으시면 저 부르시는 거, 잊지 마세요?"

    # 엘리 퇴장
    독백 "소녀, 아니 엘리는, 가볍게 고개를 숙인 뒤 종종걸음으로 사라졌다."
    독백 "자기소개도 끝마친 참이지만, 사실 미심쩍은 느낌이 모두 가신 건 아니었다."
    독백 "갈피가 잡히지 않는 상황, 조각상, 오래된 저택, 그리고 엘리…."
    독백 "무언가 실마리가 보일 듯하면서도 연결되지 않는다. 기억의 빈자리가 크다."
    독백 "날 도와줄 사람은 올 기미가 없고, 엘리를 100\% 신뢰하지 못하는 지금, 난 오로지 내 힘으로 이 저택에 얽힌 비밀을 풀어 집으로 돌아가야만 한다."
    독백 "감시당하고 있을 수 있으니 조심히 움직이자. 나는 먼저……."

    menu:
        "탁자 위를 조사한다":
            call investigateTable
        "냉장고 안을 조사한다":
            call investigateRefrigerator
        "찬장을 조사한다":
            call investigateCupboard

    stop music
    scene living with dissolve

    독백 "엘리와 별 시덥잖은 이야기만 나눈 것 같았지만, \n소득이 아예 없는 것도 아니었다."
    독백 "저택 이곳저곳을 지날 때마다 어렴풋이 무언가 떠오르는 것 같은 느낌을 받았다."
    독백 "그 장소들을 조사하다 보면 내 기억을 되찾으리라는 강한 확신이 들었다."
    독백 "다시 엘리가 떠난 걸 확인했으니, 이번엔 무언가, \n무언가 단서를 찾아야만 한다."

    return

label investigateTable:
    # 배경: living

    scene living with dissolve

    독백 "처음부터 너무 앞서 나갈 필요는 없다. 가까운 곳부터 살펴보자."

    # cg: 두꺼운 책
    독백 "책상 위에 두꺼운 영어책이 놓여있다. 아가씨답게 고상한 취미다."
    독백 "아무 페이지나 펼쳐 보았는데, 으극, 영어라 그런지 읽질 못하겠다."

    show moonbeam:
        align (.5, .5) zoom .25
    with dissolve
    # object: moonbeam
    독백 "그런데 내가 펼친 곳에서 무언가 나풀거리며 떨어졌다. 드라이 플라워인가?"

    # 엘리 등장
    # 엘리 (행복, 실눈 웃음, 미소)
    show moonbeam:
        easein .75 align (.15, .75) zoom .1
    show 엘리 눈썹행복 눈실눈웃음1 입미소 behind moonbeam:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    엘리 눈썹행복 눈실눈웃음1 입미소 "문빔으로 만들었어요! 정말 예쁘죠?"
    독백 "엘리에게 문빔이 무엇인지 물었다."
    # 엘리 (행복, 웃음, 미소)
    엘리 눈웃음 "아, 이 꽃 이름이에요. 달처럼 은은하게 빛난다고 해서 문빔이랍니다."
    엘리 "안뜰에 핀 걸 한 송이 따서 책갈피로 만들어 봤어요. 예쁘죠?"
    독백 "확실히 예쁘다. 정성스럽게 잘 만들어진 책갈피이다."

    # 엘리 (행복, 웃음, 미소)
    엘리 "생각해보니 혼자서 심심하셨겠어요, 서재에서 뭐라도 읽으실래요?"

    #엘리 퇴장
    hide 엘리 with dissolve
    독백 "나는 정중히 사양했다."

    return

label investigateRefrigerator:
    # 배경: living
    scene living with dissolve

    독백 "문득 엘리의 장난이 떠오른다. 흡혈귀, 흡혈귀라."
    독백 "영화 같은 데서도, 이런 식으로 자신의 정보를 은연중에 흘리지 않던가?"
    독백 "높은 확률로 엘리의 ‘희생자’들이 보관되어 있을 곳을 향했다."
    독백 "식은땀이 흐르는 손으로 오래된 냉장고 문을 열자 드러난 것은 {color=F00}새빨간{/color}{nw}{w=2.5}"
    extend " 콜라 라벨이 붙은 유리병들이었다! 그것도 아주 많이."
    # object: coke
    show coke:
        align (.5, .5) zoom .5
    with dissolve
    독백 "이놈의 흡혈귀는 피가 아니라 콜라를 먹고 사나, 싶을 정도로 콜라병들이 냉장고 안을 빽빽이 채우고 있었다."
    독백 "서늘한 기운이 감돌았다. 냉장고 탓인가."

    # 엘리 등장
    # 엘리 (음영 on, 난처, 실눈 웃음, 미소)
    scene living with dissolve
    show 엘리 눈썹난처 눈실눈웃음1 입미소 음영있음:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    엘리 "……지금 뭘 하고 계실까요?"
    엘리 "남의 집 냉장고를 함부로 뒤지면 안 된다고, 배우지 않으셨을까요?"
    #엘리 퇴장
    hide 엘리 with dissolve
    독백 "…아무래도 냉장고가 아니라, 화가 난 엘리 때문인 것 같았다."
 
    return

label investigateCupboard:

    scene living with dissolve

    독백 "무턱대고 발걸음을 옮기긴 했으나, 어디로 가야 할지 갈피가 안 잡힌다."
    # object: gum
    show gum:
        align (.5, .65) zoom .3
    with dissolve
    독백 "어느새 찬장 앞에 도달하긴 했는데, 들어있는 건, 풍선껌?"
    독백 "엘리의 눈치가 보이긴 했지만, 껌 하나를 입에 넣고 부드러워질 때까지 질겅질겅 씹었다."
    독백 "그리고 풍선을 불려고 했는데… 생각보다 잘 되지 않는다."
    # 엘리 등장
    # 엘리 (보통, 웃음, 무표정)

    scene living with dissolve
    show 엘리 눈썹보통 눈웃음 입무표정:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    독백 "언제 내 곁에 왔는지 모를, 풍선을 잘만 만드는 엘리와는 다르게 말이다."
    독백 "엘리가 내게 웃으며 풍선껌을 건넸다."
    # 엘리 (보통, 웃음, 미소)
    엘리 눈썹보통 눈웃음 입미소 "여기, 하나 더 시도해 보시겠어요?"
    독백 "풍선껌을 받아 입에 넣고서, 질겅, 질겅. 그리고 바람을 불면…."
    독백 "…또 실패했다. 엘리는 잘만 하는데."

    # 엘리 퇴장
    hide 엘리 with dissolve
    독백 "그렇게 우리는 찬장 속 풍선껌이 다 떨어질 때까지 껌을 씹고, 또 씹었다."

    return
