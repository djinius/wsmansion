define page2Text = """
어느 날 ■■■는 예고도 없이 그의 집에 찾아왔다. 어느 날 그녀는 같은 방식으로 떠났다.
그녀는 묵직한 트렁크를 들고 왔다. 그리고 다시 묵직한 트렁크를 들고 떠났다.
그는 음식값을 치르고 레스토랑을 나와서 더욱더 감미로워지는 우울에 빠져 거리를 산책했다.
■■■와 함께 산 칠 년이라는 세월은 이제 과거의 일이다.
그런데 돌이켜 보니 이미 추억이 된 그 시절이 당시에 느꼈던 것보다 훨씬 아름답게 느껴졌다.
그와 ■■■의 사랑은 분명 아름다웠지만 피곤하기도 했다.
항상 뭔가 숨기고, 감추고, 위장하고, 보완하고, 그녀에게 용기를 주고, 위로하고,
그녀를 사랑한다는 사실을 끊임없이 증명하고, 질투심과 고통과 꿈에서 비롯된 비난을 감수하고,
죄의식을 느끼고, 자신을 정당화하고, 용서를 구해야만 했다.
이제 피곤은 사라지고 아름다움만 남았다.
"""

define clockMemoText = """
난쟁이와 꺽다리가 서로 만나기로 했다.
난쟁이가 말했다.
"우리 OO시부터 OX시 사이에 만나는 건 어때?"
그러자 꺽다리가 핀잔을 주며 말했다.
"이 바보야, 우린 그 사이에 못 만나는 거 몰라? 
난쟁이가 다시 말했다.
"그럼 OX시부터 OU시에 만나던가. 식사도 할 겸."
"그때도 못 만나잖아, 에휴, 그냥 오후 U시에 만나."
꺽다리가 말했다.
"""

default fragmentFoundCount = 0
default isMemoFound = False
default isBedroomUnlocked = False
default isMirrorComplete = False

image darkblue = Solid("#006")

define 독자1 = Character('???', color="#C5CAB6", ctc = "ctc icon", ctc_position = 'nestled-close', what_prefix="“", what_suffix="”")
define 독자2 = Character('??!?', color="#C5CAB6", ctc = "ctc icon", ctc_position = 'nestled-close', what_prefix="“", what_suffix="”")
define 독자3 = Character('？⑤＄', color="#C5CAB6", ctc = "ctc icon", ctc_position = 'nestled-close', what_prefix="“", what_suffix="”")
define 독자4 = Character('ⓞ●◐', color="#C5CAB6", ctc = "ctc icon", ctc_position = 'nestled-close', what_prefix="“", what_suffix="”")
define 독자5 = Character('＠', color="#C5CAB6", ctc = "ctc icon", ctc_position = 'nestled-close', what_prefix="“", what_suffix="”")
define fragmentPositions = [(1073, 926), (374, 925), (868, 850), (405, 754), (387, 960)]

label page2Found:
    $ addFoundHistory("찢어진 책장", "page2")
    $ objectFound("page2")
    play sound "audio/sfx/paper.mp3"
    call screen exploreFound("page2", (531, 802))

    독백 "오래된 책의 일부처럼 보인다."

    call screen pageContents(page2Text)

    if ("page1" in myInventory) and ("tornbook" in myInventory):
        call bookCompleted
        독백 "드디어 내용이 완성되었다!"
    elif ("tornbook" in myInventory):
        독백 "아직 한 페이지가 부족해 보인다…."
    elif ("page1" in myInventory):
        독백 "이제 원본만 찾으면 된다."
    else:
        독백 "이것만 가지고서는 의미가 없어보인다. 더 찾아보자."

    call bookStory
    
    return

label lockFound:

    $ addFoundHistory("자물쇠", "lock")

    독백 "자물쇠다. 이걸 열어야 이 방 안으로 들어갈 수 있다."
    call screen lockPuzzle

    if not isBedroomUnlocked:
        return

    $ objectRemove("lock")

    show text "자물쇠를 클릭하여 침실에 입장할 수 있습니다." at truecenter
    pause
    scene black with dissolve

label lockStory:
    # 배경: street2
    hide screen explore with dissolve
    scene street2 with dissolve

    play music tranquil2

    독백 "나에게 있어 세상은 빈 도화지이다."
    독백 "텅 비어 있기에 무엇이든 채울 수 있는 도화지는,\n이미 전부 남들의 어둡고 질척한 물감으로 물들어 있었다."
    독백 "소심하고 유약했던 나에게 그런 세상은 너무나도 무서웠다."
    독백 "그래서, 아무도 신경 쓰지 않는 세상의 배경 한구석,"
    독백 "작지만 투명한 도화지 한 바닥에 나만의 색을 채워넣기 시작했다."

    # 배경: fairytale1
    scene fairytale1 with dissolve

    독백 "이야기를 썼다."
    독백 "비련의 공주님과 멋진 왕자님이 나오는, 유치하고 뻔한 이야기."
    독백 "동시에 그곳은, 무엇과도 맞바꿀 수 없는 나만의 도피처였다."

    # 배경: fairytale1_2
    scene fairytale1_2 with dissolve

    독백 "나는 이야기의 주인공처럼, 빛을 받는 무용수처럼 마음껏 춤을 추었다."
    독백 "두 다리 대신 펜과 키보드를 아무도 보지 않는 것처럼 놀려대었다."
    독백 "몇몇은 배경에 불과했던 나를 알아보기 시작했다."
    독백 "가끔 어리숙한 부분을 지적받았지만, \n풋풋한 로맨스 작가로서 미래가 기대된다는 칭찬도 종종 들었다."
    독백 "무엇보다 중요한 건,"
    독백 "나만을 위해 만들어진 세상에서 나는 완벽히 자유로울 수 있었다."

    stop music
    # 배경: fairytale2
    scene fairytale2 with dissolve

    play sound "audio/sfx/crack.mp3" noloop
    독백 "그런데."

    play music pain1
    # 배경: classroom
    # 효과음: 계속해서 고조되는 노이즈, 유리 깨지는 소리

    독자1 "저기, 이 공책 주웠는데… 설마! 너 ◎◎야?"
    독백 "그만."

    독자1 "솔직히 맨날 교실 뒤쪽에 음침하게 있는 줄만 알았는데,\n다시 봤다. 인기 작가님?"
    독자2 "진짜, 나 완전 팬이잖아… 다음 전개 뭐야? 알려 줘!"

    독백 "그만 해."

    독자3 "요즘 너무 밋밋한데… 야 사이다 없냐, 사이다?"
    독자4 "여주 감정선을 이렇게까지 길게 가져갈 필요가 있는 거야?\n그, 좋아하는 캐릭터인건 알겠는데…. 이것도 독자 의견이니……."

    독백 "여기서도 날 배경 취급하려 드는 거야?"

    독자5 "나 이 작가 글 더는 못 봐주겠다, 문장력부터 필체에 현실반영이지겹고감정선이\n고구마먹다암세포걸려뒤지겠네작가새끼뇌세포가살아있는건지상차하자가나다"

    # 배경: 검은 화면
    # 효과음: 정적 – 빗소리 페이드 인

    독백 "세상은 빈 캔버스다."
    독백 "세상은 아무것도"
    독백 "들어있지 않은 컵이고"
    독백 "나는 피사체를 돋보이게 할 뿐인 배경이며"
    독백 "이 모든 것에는 아무런 의미도 없다."
    독백 "……."
    독백 "도망칠까."
    독백 "{i}영원히.{/i}"

    stop music

    scene black with dissolve
    # 효과음: 빗소리 페이드 아웃

    return

label clockFound:

    if isMemoFound is False:
        $ isMemoFound = True
        $ addFoundHistory("시계", "clock")
        
        독백 "시계 한구석에 메모지가 끼워져 있네."

    play sound "audio/sfx/clock.mp3"
    call screen clockPuzzle

    return

label fragFound(no):

    if "gloves" in myInventory:
        $ objectFound("frag" + str(no))
        play sound "audio/sfx/alarm.mp3"
        call screen mirrorFragmentFound("frag" + str(no), fragmentPositions[no])

        if True not in fragmentsFound:
            $ addFoundHistory("유리 파편", "frag" + str(no))
            독백 "날카로운 유리 거울의 파편이다."

        $ fragmentsFound[no] = True
    else:
        독백 "날카로운 유리 거울의 파편. 그냥 줍자니 너무 위험해 보인다……."

    return

label frag0Found:
    call fragFound(0)
    return

label frag1Found:
    call fragFound(1)
    return

label frag2Found:
    call fragFound(2)
    return

label frag3Found:
    call fragFound(3)
    return

label frag4Found:
    call fragFound(4)
    return

label balletFound:
    $ addFoundHistory("발레리나 인형", "ballet")

    # [발레리나 인형(침실, 이스터 에그) 발견 시 대사]

    scene black with dissolve
    show ballet_large:
        align (.5, .5) zoom .5
    with dissolve

    독백 "발레리나 모양을 한 인형이다."
    독백 "엘리도 아직은 이런 걸 가지고 놀 나이인가 -"

    # (효과음:break, 목 위쪽 레이어가 사라짐.)
    play sound "audio/sfx/break.mp3"
    scene black
    show balletbroken:
        align (.5, .5) zoom .5
    pause 1.
    scene black
    show balletheadless:
        align (.5, .5) zoom .5
    with dissolve

    독백 "……."

    $ objectFound("ballet")
    call screen exploreFound("balletfound", (1176, 659))

    scene black

    return

label mirrorFound:
    if isMirrorFound is False:
        $ isMirrorFound = True
        $ addFoundHistory("거울", "mirror")

        독백 "유리가 깨진 거울이다. 맞춰야만 할 것 같은 강한 위화감이 든다."

        if True not in fragmentsFound:
            독백 "나머지 조각들은 어디 떨어져 있는지 보이지 않는다."
            return
        else:
            독백 "깨진 파편들을 맞추고 싶은 강한 충동이 든다."
            독백 "가장 중요한 비밀도 드러날 것이다, 확신할 수 있다."

    # 유리 맞추기
    # 다 맞추지 못했으면 return

    call mirrorPuzzle
    if isMirrorComplete:
        call mirrorComplete

    return

label mirrorPuzzle:
    scene black
    $ config.mouse_displayable.add("pressed_default", "gui/cursors/drag.png", 1, 63)
    call screen mirrorMiniGame
    $ config.mouse_displayable.add("pressed_default", "pressed_say", 1, 63)
    return

label mirrorComplete:
    hide screen explore

    play sound "audio/sfx/bell.mp3" noloop
    독백 "유리처럼 선명해지는 기억에 가슴팍이 욱신거린다."

    # 배경: 검은 화면

    play music mystery2
    scene black
    # 엘리 (scg x)
    엘리 "함부로 나가면 안 돼요. 큰일 난다구요."

    # ‘나’ 
    나 "닥쳐."

    # 배경: garden
    scene garden with dissolve

    독백 "저택에 오고 난 뒤로 느껴졌던 모든 위화감이 한데 모여,\n마지막으로 내가 본 광경과 함께 소름끼치는 추측을 뒷받침해주고 있었다."

    # 엘리 등장
    # 배경: 검은 화면 + 엘리 (보통, 웃음, 무표정, 반투명)
    scene black
    show 엘리 눈썹보통 눈웃음 입무표정:
        pos (.5, .05) anchor (.5, .0)
        alpha .75
        zoom .5
    with dissolve

    독백 "나에게서 무언가 감추는 듯한 엘리의 행동거지."

    # 배경: sculpt_bnw
    scene sculpt_bnw with dissolve

    독백 "하나같이 우리를 등진 채 도망치려는 듯한 조각상들."

    scene home with dissolve

    독백 "대한민국에, 이런 곳에 있을 리 없는 괴담 속 저택까지."
    독백 "결정적으로 내가 방금 주운, 이 새 조각상들은."

    # 배경: garden
    scene garden with dissolve
    # ‘나’ 
    나 "날개 뒤쪽으로는 아직 꿈틀대고 있어… 누가 앞 부분만 굳힌 것처럼."

    # 엘리 등장
    # 엘리 (보통, 실눈, 무표정)
    show 엘리 눈썹보통 눈실눈웃음1 입미소:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    엘리 "그러게요, 대체 누가 그랬을까요?"

    독백 "아직도 그로테스크하게 꿈틀대는 새의 뒷다리를 보고도 실실 웃는 엘리."
    독백 "그 다음 엘리의 입에서 나온 말은 일체의 변명도 아닌,\n엘리가 내게서 감추고 있던 저택의 기이한 정체였다."

    엘리 "뭐, 별건 아니고 저택의 기현상을 이용한 취미 생활이에요. 예쁘게 굳었죠?" 
    엘리 "당신께도 보여드리고 싶단 생각은 했지만… 제 예상보다 빨리 찾아내셨네요."

    # ‘나’ 
    나 "그럼 저 괴상한 포즈의 조각상들은?" 
    나 "죄 없는 사람들을 죄다 돌로 만들어놓는 것도 네 취미라고?"
    나 "제대로 설명하는 게 좋을 거야. \n이 저택은 다 뭐고, 저 조각상, 아니, 사람들은…" 
    나 "그리고 나는…… 나는 어떻게 할 셈이지?"

    # 엘리 (보통, 웃음, 무표정)

    엘리 눈썹침울 눈웃음 입무표정 "……하아."
    엘리 "우선, 전 사람을 조각상으로 만들기 위해 가지고 놀 정도로 영악하진 않아요."
    엘리 눈썹보통 눈실눈웃음2 "애초에 조각상이 된 모든 이들이, 죄가 없다고 어떻게 확신하는 거죠?"

    # '나'
    나 "말장난 하지 마."

    # 엘리
    엘리 "말장난 아니에요." 
    엘리 눈썹행복 눈웃음 "저택 지하에서 무언가 불경한 일이 벌어지고 있었던 건 확실하거든요."
    엘리 "엘리엇 가문이 세일럼, 매사추세츠에서 쫓겨나\n이곳으로 거처를 옮긴 이유와도 관련 있을 터죠."
    엘리 "정확히 무슨 일이었는지는 저도 몰라요.\n관심도 없거니와, 당시 어렸던 저만 빼고 암암리에 진행되던 일이었으니."
    엘리 눈썹보통 "그렇게 저에게는 따가운 햇살을 피해 달아난 평화로운 일요일 오후,\n가족들에겐 비밀스런 집회의 끔찍한 실패와 참상이 교차하자,"
    엘리 "아버지, 어머니, 숙부님과 숙모님들, 언니에 몇몇 지인들까지.\n모두가 공포에 질려 도망치는 가운데, 저는 영문도 모른 채 홀로 남겨졌어요."

    # 엘리 (보통, 눈 감음, 무표정)
    엘리 눈실눈웃음1 "아, 아니죠. 크흠. 정정할게요."

    # 엘리 (보통, 사백안, 무표정)
    엘리 눈사백안 "…이 저주받을 저택과 {i}함께{/i} 말이야."

    독백 "저택의 비밀이 밝혀짐과 동시에 적막이 감돌았다."
    독백 "물러서려 했지만 안뜰을 함부로 넘어간 이들과 같은 최후를 맞고 싶지 않았다."
    독백 "엘리는 그걸 잘 안다는 듯 내 앞으로 한 걸음씩 다가오기 시작했다."

    # 엘리 (행복, 사백안, 무표정)
    엘리 눈썹행복 "몇십 년을 지내다 보니 싫어도 깨닫게 되더군요,\n이 저택 안에서는 시간이 흐르지 않는다는 걸 말이에요."
    엘리 "음, 흐르지 않는다, 는 것과는 조금 다를까요. 여러모로 뒤죽박죽이죠."

    # 엘리 (보통, 눈 감음, 무표정)
    엘리 눈썹보통 눈실눈웃음2 "째깍, 째깍, 시계바늘은 쉼 없이 움직이지만,\n감아놓은 태엽은 완전히 풀리지 않더군요."
    엘리 "냉장고 속 먹거리들을 비워 놔도, 정신을 차려보면 다시 가득 차 있고요."
    엘리 "늘 이 시간대예요, 아침 해가 뜨거나, 밤이 오는 법도 전혀 없죠."

    독백 "생각해보니 여기에 온 첫날 빼고 저녁놀이 진 것을 본 적이 없다."
    독백 "굳게 쳐진 커튼들 때문에 눈치챌 겨를도 없었다."
    독백 "그렇다면 이 저택에서 얼마나 오래 지난 거지? 돌아가는 방법은?"

    # 엘리 (행복, 눈 감음, 미소)
    엘리 "제 유년기가 어땠는지, 가족들의 모습은 어땠는지,\n이젠 아무리 애써도 기억나지 않는 지경까지 왔어요."
    엘리 "그대로 몇십 년 정도 지나니 굳이 떠올려내고 싶지도 않아지더군요."
    엘리 "가끔 길을 잃은 몇몇 이들이 기웃거리긴 했지만,\n저택 겉만 가볍게 둘러보고 사라지는 걸 반복했죠."
    엘리 "그렇게 얼마나 지났을까, 저택에 처음으로 추적추적 비가 내리던 날."

    # 엘리 (행복, 눈웃음, 미소)
    엘리 눈썹행복 눈웃음 입미소 "사고 이후 처음으로 손님을 들이기로 했어요."

    독백 "설마 그 손님은."

    # 엘리 (행복, 실눈 웃음, 미소)
    엘리 눈실눈웃음1 "사실 그리 내키진 않았지만, 모든 희망을 내려놓은 눈빛이 마음에 들었거든요." 
    엘리 "본의 아니게 저택에 영영 갇혀버린 어느 소녀처럼 말이죠."
    엘리 "그런데 어째서일까, 당신과 함께하는 실없는 순간순간이 반복될수록,"

    # 엘리 (행복, 실눈 웃음2, 미소)
    엘리 눈실눈웃음2 "적어도, 적어도 저한테는 시간이 다시 흐르는 느낌이었어요."

    # 엘리 (행복, 웃음, 미소)
    엘리 눈웃음 "당신이 있었기에 제가 여기 존재할 이유를 다시 찾아낼 수 있었어요."

    # 엘리 (행복, 웃음, 미소, 눈물)
    엘리 눈물 "전부 당신 덕분이에요. 내 삶에 따스한 빛깔을 더해 줘서."
    엘리 "정말로 고마워요. 말로 다 표현할 수 없을 만큼요."

    독백 "엘리는 나의 현재와 미래를 담보로 본인만의 영원을 손에 넣은 것이었다."
    독백 "우수에 젖어 저택을 찾아왔던 건 나였지만, 그런 나를 잘도 속이고서는\n내가 집으로 돌아간다는 가능성 자체를 없애 버린 셈이다."
    독백 "내가 엘리 본인만을 위한, 꿈 같은 저택 속 일부가 되는 것을 지켜보기 위해서."

    # 엘리 (행복, 사백안, 미소, 눈물)
    엘리 "그러니 굳이 다시 떠날 필요도 없어요."
    엘리 눈실눈웃음1 "유치한 동화 속 왕자님과 공주님처럼,\n여기서라면 영원히 둘이 행복하게 살 수 있으니까요."
    엘리 "이 새들도 그걸 기념하기 위해 만든 거예요."
    엘리 눈사백안 "우리의 새로운 시작과, 앞으로도 계속될 저택에서의 나날들을 위해서."

    독백 "{i}아니,{/i} 마음 같아서는 저 영악한 마녀를 끓는 솥에다 담가버리고 싶었다."
    독백 "채 날개를 펴지도 못한 채 굳어버린 새들의 \n날카로운 마지막 숨결이 머릿속에서 메아리쳤다."
    독백 "미래를 볼 수 있다는 까마귀들의 울음소리처럼,\n그 메아리는 내게 닥칠 끔찍한 미래를 예언하고 있었다."

    # 엘리 (행복, 실눈 웃음, 미소)
    엘리 눈웃음 눈물없음 "어때요, 정말 사랑스럽지 않나요?"
    엘리 눈웃음 "당신도 우중충한 바깥보단 늘 햇살이 비치는 이곳이 훨씬 좋지 않나요?"

    # 엘리 (난처, 실눈 웃음, 미소)
    엘리 눈실눈웃음 눈썹난처 "왜 그렇게 인상을 찌푸리세요, 무섭잖아요."

    # 엘리 (보통, 사백안, 무표정)
    엘리 눈썹보통 눈사백안 입무표정 "아니면 이런 저의 처지를 외면하시겠다는 건가요."
    엘리 "본인만 그 잘난 자유를 찾겠다고 하는 건가요. 어떻게 그리 잔혹한가요."

    독백 "그리고 엘리는, 모든 일의 원흉이 나라도 되는 듯 노려보기 시작했다."
    독백 "저건 내가 아는 엘리의 모습이 아니었다."
    독백 "나는 지금 외로움에 미친 나머지 자신만의 세상에 빠져,\n내게 배신당했다고 굳게 믿는 저택의 원령을 상대해야만 했다."

    # 엘리 (보통, 사백안, 무표정, 눈물) 
    엘리 눈물 음영있음 "가만히만 있지 말고, 입이 살았으면 뭐라도 말해 보란 말이에요…!"
     
    # 엘리 퇴장 
    hide 엘리 with dissolve

    독백 "분노한 엘리가 내 쪽으로 성큼성큼 다가오기 시작했다."
    독백 "눈앞이 아찔해졌다, 이번엔 진짜 마지막이라는 생각이 들었다."
    독백 "그러자 신기하게도 오히려 마음이 편안하고 침착해지는 것이었다."
    독백 "심호흡을 했다. 생각해 보니 나 또한 엘리에게 미처 전하지 못한 것들이 있었다." 
    독백 "아니, 전해야만 했다."

    stop music
    play music tranquil3
    # ‘나’ 
    나 "…실은 나도 엘리 네게 모든 걸 말하진 않았어."
    나 "사람들이 싫어서, 그냥 이 세상 사람들이 무서워서, 여기서 죽으려고 온 거였어."
    나 "죽을 땐 한없이 춥기만 할 줄 알았는데, \n누군가가 언제나 곁에 있다는 걸 아니까, 생각보다 따스했어." 
    나 "태양도 그렇고, 이 저택도 그렇고, 너도 그렇고."
    나 "무엇보다 엘리, 엘리 네가 있었기에 버티는 걸 넘어 행복할 수 있었어."

    # 엘리 등장
    # 엘리 (침울, 감은 눈, 미소)
    show 엘리 눈썹침울 눈실눈웃음1 입미소 음영없음:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    엘리 "그랬군요. 맞아요."  
    엘리 "우리는 서로 함께였기에, 그 사실을 확인하며 온기를 나누었어요."

    stop music
    # ‘나’ 
    나 "그래서 돌아가려는 거야."

    # 엘리 (놀람, 사백안, 무표정)
    엘리 눈썹놀람 눈사백안 입무표정 "에."
    
    play music strain
    # ‘나’ 
    나 "내가 줄곧 외면해왔던 세상의 빛깔들을 다시 한번 보고 싶어졌어."
    나 "다시 사람들에게 배척받고 실망하는 한이 있더라도. 이미 결심한 일이야."
    나 "몇십 년이나 지나버린 바깥 세상의 아름다운 색깔을 보여주지 못해서,\n곁에서 같이 보지 못해서 미안해, 정말로. 하지만…."

    # 엘리 (놀람, 사백안, 미소, 눈물 - 오열)
    엘리 눈썹놀람 눈사백안 입미소 눈물 음영있음 "그, 그럼 적어도, 적어도 다시 돌아와 주겠다고 약속만 해 줘요.\n네? 문은 언제든지 열려 있어요."
    # 엘리 (침울, 사백안, 무표정, 눈물 - 오열)
    엘리 눈썹침울 입무표정 "이렇게 부탁할게요. 절 여기다가 혼자 두고 간다고만 말하지 말아줘요.\n잊히기 싫어요. 세상에서도, 당, 당신에게서도."
    엘리 "다시 못, 아니, 안 돌아와도 괜찮아요, 빈말만이라도 해, 해, 해 줘요."

    # ‘나’ 
    나 "그런 약속 못 하겠어. 엘리처럼 소중한 사람한테, 빈말로는 더 못해."

    독백 "내가 고개를 젓자, 쩍쩍 갈라지는 나무처럼 목소리가 일그러지던 엘리는\n자리에 그대로 무너지고 말았다."

    # 엘리 퇴장
    hide 엘리 with dissolve
    # ‘나’ 
    나 "마지막으로 이거 하나만 확실히 하자. 이 저택도, 너와의 추억도, 모두 소중해."
    나 "하지만 난 너만을 위한 장난감도, 오래된 가족사진 속 배경도 아니라고."
    나 "그러니까 제발 날 이 망할 저택에서 나가게 해 달란 말이야!"

    독백 "나는 악을 쓰며 소리쳤다."
    독백 "이제는 빨리 나가고 싶다기보단,\n엘리와의 마지막 작별에서도 후회를 남기고 싶지 않다는 마음이었다."
    독백 "그리고 그런 나의 진심은 이제 아무 상관 없다는 듯이,\n철판을 긁어대는 것 같은 웃음소리가 들려왔다."
    독백 "소름 끼치는 감촉이 내 손에 닿았다."

    stop music

    # 배경: 검은 화면
    play music fear
    scene black with dissolve

    # 엘리 (scg x)
    엘리 "끄흑,"
    엘리 "끅, 끄흐흑, 끼히히히히히히힛."

    # ECG 3 – 엘리의 절규

    scene thirdEvent with dissolve

    # 엘리 
    엘리 "…아뇨, 하나도, 하나도 이해가 가지 않아요."
    엘리 "혼자서 버티는 이 영원은 저에게 있어 쓰라린 고통이었어요."
    엘리 "하지만, 당신이 있었기에 그렇지 않았어요."
    엘리 "저주와도 같은 이 영원함은, 고통이 아니라 행복 속에서 다시 피어났죠."
    엘리 "그 행복은 단조로우면서도 푸근한 일상이 아니라, 오직 서로에게서만 얻을 수 있다는 걸 너무나도 늦게 깨닫고 말았어요. 당신과 저, 오직 둘이서."
    엘리 "당신도 그 행복을 느꼈잖아요, 그렇다면 대체 왜 돌아가시려는 거예요? "
    엘리 "{font=Danjo-bold-Regular.otf}우리는 한 쌍처럼 완벽했는데, 왜 우리 모두 무너져야만 하냐고요!{/font}"

    독백 "엘리의 웃음은 울음으로, 절규로, 그리고 쩍쩍 갈라지는 괴성으로 변했다."
    독백 "눈에 초점이 없었다. 나를 잃는다는 두려움에 말이 통하지 않아 보였다."
    독백 "말이 통하지 않으면 행동으로 보여줄 수밖엔 없다."

    # 배경: 살구색 화면, 블러 이펙트, scg x
    
    scene apricot
    show layer master at bgblur(30.)

    독백 "엘리의 멱살을 잡으러 손을 뻗었다."
    독백 "바로 그 순간, 내 몸이 힘을 잃으며 뒤로 고꾸라졌고"
    독백 "둔탁한 충격이 가해지며 난,"
    독백 "난…."
    독백 "……."

    stop music

    # 배경: 살구색 화면
    scene apricot

    # (화면 중앙 텍스트, 흰색)
    show text "{size=+40}{color=#700}거짓말쟁이{/color}{/size}" at text5Seconds:
        align (.5, .5)

    독백 "그것이 내가 어이없게 쓰러지기 전 기억하는 마지막 말이었다."
    독백 "단어는 기억나는데, 당최 누가 누구에게 말했던 건지 흐릿하다."
    독백 "내가 엘리에게? 엘리가 나에게?"
    독백 "나는 진심을 토했다고 생각하는데, 이젠 막상 누가 거짓말쟁이인지 헷갈린다."
    독백 "그리고 엘리는, 과거 내 팔을 잡은 순간의 모습 그대로 내 앞에 서 있었다."

    # 엘리 등장
    # 엘리 (보통, 웃음, 무표정)
    scene apricot
    show 엘리 눈썹보통 눈웃음 입무표정:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve
    엘리 "…어디까지 기억나셨나요."

    return

label ellyPart2:
    scene black
    show 엘리 눈썹난처 눈웃음 입미소:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    독백 "탐정이라도 된 듯 저택 안을 샅샅이 뒤지고 있는 엘리."
    독백 "보고 있자니 흐뭇하지만, 나도 내 일을 해야겠지."

    scene black with dissolve

    return
