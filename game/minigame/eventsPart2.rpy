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

label page2Found:
    $ addFoundHistory("찢어진 책장", "page2")
    $ objectFound("page2")
    call screen exploreFound("page2")
    show screen exploreBase

    나 "오래된 책의 일부처럼 보인다. 어딘가 낯이 익은데."

    call screen pageContents(page2Text)

    if ("page1" in myInventory) and ("tornbook" in myInventory):
        나 "드디어 내용이 완성되었다."
    elif ("tornbook" in myInventory):
        나 "아직 한 페이지가 부족해 보인다."
        return
    elif ("page1" in myInventory):
        나 "어디서 뜯겨져 나온 페이지일까, 원본이 있을까?"
        return
    else:
        나 "이것만 가지고는 아무것도 떠오르지 않는다."
        나 "원본을 찾아보면 어떨까."
        return

label page2Story:
    # 배경: 어두운 청색 배경
    scene darkblue with dissolve

    나 "나에게 있어 세상은 빈 도화지이다."
    나 "텅 비어 있기에 무엇이든 채울 수 있는 도화지는, 이미 전부 남들의 어둡고 질척한 물감으로 물들어 있었다."
    나 "소심하고 유약했던 나에게 그런 세상은 너무나도 무서웠다."
    나 "그래서, 아무도 신경 쓰지 않는 세상의 배경 한구석,"
    나 "작지만 투명한 도화지 한 바닥에 나만의 색을 채워넣기 시작했다."

    # 배경: 별이 빛나는 하늘과 왕자님과 공주님의 실루엣이 그려짐

    나 "이야기를 썼다."
    나 "비련의 공주님과 멋진 왕자님이 나오는, 유치하고 뻔한 이야기."
    나 "동시에 그곳은, 무엇과도 맞바꿀 수 없는 나만의 도피처였다."

    # 배경: 뒤집힌 유리잔 모양 스포트라이트 불빛
    나 "나는 이야기의 주인공처럼, 빛을 받는 무용수처럼 마음껏 춤을 추었다."
    나 "두 다리 대신 펜과 키보드를 아무도 보지 않는 것처럼 놀려대었다."
    나 "몇몇은 배경에 불과했던 나를 알아보기 시작했다. 가끔 어리숙한 부분을 지적받았지만, 풋풋한 로맨스 작가로서 미래가 기대된다는 칭찬도 종종 들었다."
    나 "무엇보다 중요한 건, 나만을 위해 만들어진 세상에서 나는 완벽히 자유로울 수 있었다."
    나 "그런데."

    # 배경: 금이 간 조명 (유리잔), 그리고 드러나는 흑백 교실
    # 효과음: 계속해서 고조되는 노이즈, 유리 깨지는 소리

    "저기, 이 공책 주웠는데… 설마! 너 ■■야?"
    나 "그만."

    "솔직히 맨날 교실 뒤쪽에 음침하게 있는 줄만 알았는데, 다시 봤다. 인기 작가님?"
    "진짜, 나 완전 팬이잖아… 다음 전개 뭐야? 알려 줘!"

    나 "그만 해."

    "요즘 너무 밋밋한데… 야 사이다 없냐, 사이다?"
    "여주 감정선을 이렇게까지 길게 가져갈 필요가 있는 거야? 그, 좋아하는 캐릭터인건 알겠는데…. 이것도 독자 의견이니……."

    나 "여기서도 날 배경 취급하려 드는 거야?"

    "나 이 작가 글 더는 못 봐주겠다, 문장력부터 필체에 현실반영이지겹고감정선이고구마먹다암세포걸려뒤지겠네작가새끼뇌세포가살아있는건지상차하자를⧯㋆⧔⧂⧁⡠▊▛⥣⥙⤩⤗⤅⤓⧖⧏Ⱘ⭆⮜⭖⯃⮾⯑⭀ⱱⱠⰴ↤Ω№‴⁂⇕ᶓᶑ᥸ᥳ᧹ᤔᤵᜳᝣᎵᏖᐦᐔᑣᑼ຦ລඓශ༦༖ٷؕɵʧǶȣгӔµ¥◔◧☵☸☻♿⚇♽♿⛩⛕⛄⛢⛳⛲⛽⛼❤❖➉➌✚✊➲⟒⟔"

    # 배경: 검은 화면
    # 효과음: 정적 – 빗소리 페이드 인

    나 "세상은 빈 캔버스다."
    나 "세상은 아무것도"
    나 "들어있지 않은 컵이고"
    나 "나는 피사체를 돋보이게 할 뿐인 배경이며"
    나 "이 모든 것에는 아무런 의미도 없다."
    나 "……."
    나 "도망칠까."
    나 "영원히."

    # 효과음: 빗소리 페이드 아웃

    return

label lockFound:
    $ addFoundHistory("자물쇠", "lock")
    # $ objectFound("earring")
    # call screen exploreFound("earring")
    # show screen exploreBase

    나 "자물쇠다. 이걸 열어야 이 방 안으로 들어갈 수 있다."
    call screen lockPuzzle

    if isBedroomUnlocked:
        $ objectRemove("lock")

    return

label earringStory:
    # 배경: 검은 화면
    # 효과음: 심장 소리 한 번

    나 "답답하다, 숨이 막히고 가슴이 조여온다."
    나 "하필이면 저택에 이런 게 있었을 줄이야, 당황스럽기 그지없다."
    
    # 효과음: 고조되는 심장 박동과 방문을 불규칙적으로 두드리는 소리
 
    나 "처음 느껴보는 압박에 몸도 마음대로 움직여지지 않는다."
    나 "도무지 벗어날 수가 없는데, 바깥에서는 협박조로 방문을 두드리고 있다."
    나 "내가 옴짝달싹 못 하는 사이, 누군가 결국 참다못해 강제로 방문을 열고 들어왔다."

    # 엘리 (scg x, 텍스트만)
    엘리 "…퍽 잘 어울리시네요. 안에서 계속 우는 소리를 내시던 것 치고는 말이죠."

    # ECG 2 – 정장을 착용한 ‘난설’

    난설 "…크읏, 어울리긴 무슨……. 이게 뭐야, 불편하기만 하고!"

    # 엘리 (scg x, 텍스트만)
    엘리 "어머, 제 자택에서 그만한 예복을 갖추기로 한 건 그쪽이 아니던가요?"
    엘리 "사이즈가 안 맞으니 제 드레스를 빌려드릴 순 없고, 그렇다고 비에 적신 그 후줄근한 옷을 계속 입고 있을 수도 없으니."
    엘리 "급한 대로 숙부님의 정장이라도 갖추셔야 마땅하지요."
 
    난설 "그게 문제가 아니라, 내가 양복을 입어봤을 리도 없고! 나한테 사이즈도 하나도 안… 맞고……."

    나 "체구만 쓸데없이 크다는 소리를 듣고 살던 나에게 이 흰색 양복은 너무 작았다."
    나 "남성용 양복이라 그런지 가슴 부위가 특히 답답하고 조였다."
    나 "어째서인지 제 인상을 더 찌푸리며 혀를 차는 엘리는 덤이었다."

    # 엘리 (scg x, 텍스트만)
    엘리 "…초대받지 않은 손님 주제에 쓸데없이 큰 탓이에요."
    엘리 "곧 식사 시간이니까 알아서 식당으로 내려오세요."
 
    # ‘나’ 
    난설 "잠깐만, 아무리 그래도 같은 여자로서 조금이라도 도와줘야지! 야!"

    # 배경: 침실

    # 엘리 (회상, 난처, 원망, 무표정)
    엘리 "당신과 같은 저급한 취급 마세요."

    # 엘리 (회상, 보통, 눈 감음, 무표정)
    엘리 "그리고 아비게일, 아비게일 F. 엘리엇이에요, 아비든 애비든, 맘대로 부르시죠."

    나 "소녀, 그러니까 아비게일은 내 외침도 무시한 채 다시 복도로 사라졌다."
    나 "어울리지도 않는 양복을 반쯤 껴입은 채 방에 덩그러니 남겨진 나."
    나 "…아무리 그래도 애비는 그러니까, 성씨를 따서 엘리라고 불러야겠다."

    return

label deathFound:
    $ addFoundHistory("죽음 카드", "death")
    $ objectFound("death")
    call screen exploreFound("death")

    return

label clockFound:
    $ addFoundHistory("시계", "clock")
    # $ objectFound("knife")
    # call screen exploreFound("knife")
    # show screen exploreBase

    나 "뻐꾹."
    call screen clockPuzzle

    return

label fragFound(no):

    if "gloves" in myInventory:
        $ objectRemove("frag" + str(no))
        call screen mirrorFragmentFound("frag" + str(no))
        show screen exploreBase

        if True not in fragmentsFound:
            $ addFoundHistory("유리 파편", "frag" + str(no))
            나 "날카로운 유리 거울의 파편이다."

        $ fragmentsFound[no] = True
    else:
        나 "날카로운 유리 거울의 파편. 그냥 줍자니 너무 위험해 보인다……."

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

label mirrorFound:
    if isMirrorFound is False:
        $ isMirrorFound = True
        $ addFoundHistory("거울", "mirror")

        나 "유리가 깨진 거울이다. 맞춰야만 할 것 같은 강한 위화감이 든다."

        if True not in fragmentsFound:
            나 "나머지 조각들은 어디 떨어져 있는지 보이지 않는다."
            return
        else:
            나 "깨진 파편들을 맞추고 싶은 강한 충동이 든다."
            나 "가장 중요한 비밀도 드러날 것이다, 확신할 수 있다."

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

    나 "유리처럼 선명해지는 기억에 가슴팍이 욱신거린다."

    # 배경: 검은 화면

    # 엘리 (scg x)
    엘리 "함부로 나가면 안 돼요. 큰일 난다구요."

    # ‘나’ 
    난설 "닥쳐."

    # 배경: 마당

    나 "나는 내 손에 들린 조각상들을 엘리에게 보여주었다."
    나 "날개를 편 채 돌처럼 굳어버린 작은 새 모양 조각상들."
    나 "뾰족한 두 주둥이 사이엔 엘리가 잘라 놓은 사과 조각들이 박혀 있었다."
    나 "저택에 오고 난 뒤로 느껴졌던 그 모든 이상한 점들이 모여, 매우 소름 끼치는 추측과 함께 맞아떨어지기 시작했다."

    # 배경: 검은 화면 + 엘리 (회상, 보통, 웃음, 무표정, 반투명)

    나 "어딘가 수상한 엘리의 행동거지."

    # 배경: 조각상

    나 "하나같이 우리를 등진 조각상들."
    나 "배경: 저택 외관"
    나 "무엇보다 대한민국에, 이런 곳에 있을 리 없는 괴담 속 대저택까지."

    # 배경: 마당

    # ‘나’ 
    난설 "어떻게 된 건지 제대로 설명하는 게 좋을 거야."

    # 엘리 (회상, 보통, 눈 감음, 무표정)
    엘리 "정말 유감입니다만, 그럴 순 없어요."

    # ‘나’ 
    난설 "죄 없는 사람들을 죄다 돌로 만들어놓고?"

    # 엘리 (회상, 보통, 웃음, 무표정)
    엘리 "조각상이 된 모든 이들이, 죄가 없다고 어떻게 확신하는 거죠?"
    엘리 "저들은 죽어 마땅한 죄를 지었고, 그 여파로 저택에서는 모종의 사고가 일어났죠."
    엘리 "정확히 무슨 일이었는지는 저도 몰라요. 저만 빼고 암암리에 진행되던 일이었으니."
    엘리 "아버지, 어머니, 숙부님과 숙모님들, 언니에 몇몇 지인들까지. 모두가 공포에 질려 도망치는 가운데, 저는 영문도 모른 채 홀로 남겨졌어요."

    # 엘리 (회상, 보통, 눈 감음, 무표정)
    엘리 "아, 아니죠. 크흠. 정정할게요."

    # 엘리 (회상, 보통, 사백안, 무표정)
    엘리 "…이 저주받을 저택과 함께 말이야."

    나 "저택의 비밀이 밝혀짐과 동시에 적막이 감돌았다."
    나 "뒤로 물러서려 했지만, 안뜰을 함부로 넘어간 이들과 같은 최후를 맞고 싶지 않았다."
    나 "그리고 엘리는 그걸 잘 안다는 듯 내 앞으로 한 걸음씩 다가오기 시작했다."

    # 엘리 (회상, 행복, 사백안, 무표정)
    엘리 "몇십 년을 지내다 보니 싫어도 깨닫게 되더군요, 이 저택 안에서는 시간이 흐르지 않는다는 걸 말이에요."
    엘리 "흐르지 않는다, 는 것과는 조금 다를까요. 여러모로 뒤죽박죽이죠."

    # 엘리 (회상, 보통, 눈 감음, 무표정)
    엘리 "째깍, 째깍, 시계바늘은 쉼 없이 움직이지만, 감아놓은 태엽은 완전히 풀리지 않더군요."
    엘리 "냉장고 속 먹거리들을 비워 놔도, 정신을 차려보면 다시 가득 차 있고요."
    엘리 "늘상 이 시간대예요, 아침 해가 뜨거나, 밤이 오는 법도 전혀 없죠."

    나 "그러고 보니 여기에 온 첫날 빼고 저녁놀이 진 것을 본 적이 없다."
    나 "굳게 쳐진 커튼들 때문에 눈치챌 겨를도 없었다."
    나 "그렇다면 이 저택에서 얼마나 오래 지난 거지? 돌아가는 방법은?"

    # 엘리 (회상, 행복, 눈 감음, 미소)
    엘리 "제 유년기가 어땠는지, 가족들의 모습은 어땠는지, 이젠 아무리 애써도 기억나지 않아요."
    엘리 "몇십 년 정도 지나니 굳이 떠올려내고 싶지도 않아지더군요."
    엘리 "가끔 길을 잃은 몇몇 이들이 기웃거리긴 했지만, 저택 겉만 가볍게 둘러보고 사라지더군요."
    엘리 "그렇게 얼마나 지났을까, 저택에 처음으로 추적추적 비가 내리던 날."

    # 엘리 (회상, 행복, 웃음, 미소)
    엘리 "사고 이후 처음으로 손님을 들이기로 했어요."

    나 "설마."

    # 엘리 (회상, 행복, 실눈 웃음, 미소)
    엘리 "사실 그리 내키진 않았지만, 모든 희망을 내려놓은 눈빛이 마음에 들었거든요. 본의 아니게 저택에 영영 갇혀버린 어느 소녀처럼 말이죠."
    엘리 "그런데 어째서일까, 당신과 함께하는 실없는 순간순간이 반복될수록,"
    엘리 "적어도, 적어도 저한테는 시간이 다시 흐르는 느낌이었어요."

    # 엘리 (회상, 행복, 웃음, 미소)
    엘리 "당신이 있었기에 제가 여기 존재할 이유를 다시 찾아낼 수 있었어요."

    # 엘리 (회상, 행복, 웃음, 미소, 눈물)
    엘리 "전부 당신 덕분이에요. 내 삶에 따스한 빛깔을 더해 줘서."
    엘리 "정말, 정말로 고마워요."

    나 "엘리는 나의 현재와 미래를 담보로 본인만의 영원을 손에 넣은 것이었다."
    나 "우수에 젖어 저택을 찾아왔던 건 나였지만, 그런 나를 잘도 속이고서는 내가 집으로 돌아간다는 가능성 자체를 없애 버린 셈이다."
    나 "내가 엘리 본인만을 위한, 꿈 같은 저택 속 일부가 되는 것을 지켜보기 위해서."

    # 엘리 (회상, 행복, 사백안, 미소, 눈물)
    엘리 "그러니 굳이 다시 떠날 필요도 없어요."
    엘리 "유치한 동화 속 왕자님과 공주님처럼, 여기서라면 영원히 둘이 행복하게 살 수 있으니까요."

    나 "아니."
    나 "마음 같아서는 저 영악한 마녀를 끓는 솥에다 담가버리고 싶었다."

    # 엘리 (회상, 행복, 실눈 웃음, 미소)
    엘리 "당신도 비 오는 날씨보단 늘 햇살이 비치는 편이 훨씬 좋지 않나요?"

    # 엘리 (회상, 난처, 실눈 웃음, 미소)
    엘리 "왜 그렇게 인상을 찌푸리세요, 무섭잖아요."

    # 엘리 (회상, 보통, 사백안, 무표정, 눈물)
    엘리 "아니면 이런 저의 처지를 외면하시겠다는 건가요."
    엘리 "본인만 그 잘난 자유를 찾겠다고 하는 건가요. 어떻게 그리 잔혹한가요."

    나 "그리고 엘리는, 모든 일의 원흉이 나라도 되는 듯 노려보기 시작했다."
    나 "심호흡을 했다."
    나 "엘리를 속이지도 않았고, 오히려 속아온 나이지만, 동시에 전하지 못한 것들이 있었다."

    # ‘나’ 
    난설 "…실은 나도 엘리 네게 모든 걸 말하진 않았어."
    난설 "사람들이 싫어서, 그냥 이 세상 사람들이 무서워서, 여기서 죽으려고 온 거였어."
    난설 "죽을 땐 한없이 춥기만 할 줄 알았는데, 곁에 있다는 걸 아니까 생각보다 따스했어, 태양도 그렇고, 이 저택도 그렇고, 너도 그렇고."

    # 엘리 (회상, 침울, 감은 눈, 미소)
    엘리 "그랬군요. 맞아요, 우리는 서로 함께였기에 온기를 나누었어요."

    # ‘나’ 
    난설 "그래, 하지만 너에게도 집이 있듯이, 나에게도 돌아갈 곳이 있어."
    난설 "왜냐면 난 네 망할 장난감이 아니니까."
    난설 "그러니까 이 염병할 저택에서 제발 나가게 해 달란 말이야!"

    # 배경에 블러 이펙트

    나 "나는 악을 쓰며 소리쳤다."
    나 "마음만 먹으면 엘리를 한 대 칠 기세였다."
    나 "힘을 쓴다고 나갈 방법을 알려줄지는 미지수였지만, 적어도 나는 그만큼 절실했다."
    나 "그리고 나의 간절함을 비웃듯이, 철판을 긁어대는 것 같은 웃음소리가 들려왔다."
    나 "소름 끼치는 감촉이 내 손에 닿았다. 엘리였다."

    # 배경: 검은 화면

    # 엘리 (scg x)
    엘리 "끄흑,"
    엘리 "끅, 끄흐흑, 끼히히히히히히힛."

    # ECG 3 – 엘리의 절규

    # 엘리 
    엘리 "…아뇨, 하나도, 하나도 이해가 가지 않아요."
    엘리 "혼자서 버티는 이 영원은 저에게 있어 쓰라린 고통이었어요."
    엘리 "하지만, 당신이 있었기에 그렇지 않았어요."
    엘리 "저주와도 같은 이 영원함은, 고통이 아니라 행복 속에서 다시 피어났죠."
    엘리 "돌아가신다면 저는 저택과 함께 잊히고, 당신도 남들에게 핍박받을 테죠."
    엘리 "당신도 행복했잖아요, 그렇다면 대체 왜 돌아가시려는 거예요?"
    엘리 "우리는 한 쌍처럼 완벽했는데, 왜 우리 모두 무너져야만 하냐고요!"

    나 "엘리의 웃음은 절규로, 그리고 쩍쩍 갈라지는 괴성으로 변했다."
    나 "눈에 초점이 없었다. 나를 잃는다는 두려움에 말이 통하지 않아 보였다."
    나 "말이 통하지 않으면 행동으로 보여줄 수밖엔 없다."

    # 배경: 살구색 화면, 블러 이펙트, scg x

    나 "엘리의 멱살을 잡으러 손을 뻗었다."
    나 "바로 그 순간, 내 몸이 힘을 잃으며 뒤로 고꾸라졌고"
    나 "내 앞의 시야가 희미해졌다."
    나 "머리에 둔탁한 충격이 가해지며 난,"
    나 "난…."
    나 "……."

    # 배경: 살구색 화면

    # (화면 중앙 텍스트, 흰색)
    show text "거짓말쟁이" at truecenter

    나 "그것이 내가 어이없게 쓰러지기 전 기억하는 마지막 말이었다."
    나 "단어는 기억나는데, 당최 누가 누구에게 말했던 건지 흐릿하다."
    나 "내가 엘리에게? 엘리가 나에게?"
    나 "누가 진짜 거짓말쟁이란 말인가."
    나 "그리고 엘리는, 과거 내 팔을 잡은 순간의 모습 그대로 내 앞에 서 있었다."

    # 엘리 (음영 off, 놀람, 사백안, 무표정)

    엘리 "…어디까지 기억나셨나요."

    return

