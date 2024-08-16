define bookStoryLabels = ["birdFeedStory", "makeUpStory", "suitFitStory", "birdFeedStory"]

transform pageMerge(bp, lp, beginPos, endPos=(.5, .6)):
    xysize (50, 50) pos (1920 - 50 * (lp - bp - 1), 0) anchor (1., .0) alpha .0
    pause .5
    block:
        easein .5 alpha 1.
        easeout .75 xysize (175, 175) pos beginPos anchor (.5, .5)
    pause .5
    easeout .75 pos endPos alpha .0

transform bookMorphDisappear(bp, lp):
    xysize (50, 50) pos (1920 - 50 * (lp - bp - 1), 0) anchor (1., .0) alpha .0
    pause .75
    block:
        easein .5 alpha 1.
        easeout .75 xysize (500, 500) pos (.5, .6) anchor (.5, .5)
    pause .75
    easeout .5 alpha .0

transform bookMorphAppear(beginAlpha=.0, endAlpha=1., delay=2.25):
    alpha beginAlpha
    pause delay
    easeout .5 alpha endAlpha

screen bookCompletion():
    use exploreBase

    add "images/minigame/page1.png":
        at pageMerge(myInventory.index("page1"), len(myInventory), (.25, .4))
    add "images/minigame/page2.png":
        at pageMerge(myInventory.index("page2"), len(myInventory), (.75, .4))

    add "images/minigame/tornbook.png" at bookMorphDisappear(myInventory.index("tornbook"), len(myInventory))
    add "images/minigame/completebook.png" pos (.5, .6) anchor (.5, .5) at bookMorphAppear()

    timer 3.25 action Return()

screen bookFound():
    use exploreBase(1)
    add "images/minigame/completebook.png" at foundTransform((.5, .6), (.5, .5))
    timer 1.35 action Return()
    key "mouseup_1" action Return()

label bookStory:

    $ label2Call = bookStoryLabels[bookPartCount()]
    call expression label2Call
    
    return

label makeUpStory:

    hide screen exploreBase
    scene black with dissolve

    #배경: study1

    scene study1
    show 엘리 눈썹보통 눈실눈웃음1 입무표정:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    # ‘나’ 
    나 "……가슴을 쥐어뜯는 왕자님을 본 공주님이 걱정스러운 표정으로 물었습니다."

    독백 "커튼을 굳게 친 서재 안, 나는 분위기도 풀 겸 장기를 살려 이야기꾼을 자처했다."
    독백 "하필 서재에 원서밖에 없는데, 내가 영어는 자신이 없는지라 삽화만을 가지고 어떻게든 이야기를 각색하는 게 한계였지만."
 
    # 엘리 등장
    # 엘리 (침울, 침울, 무표정)
    엘리 눈썹난처 눈침울 입무표정 "그쯤 하시고 책 이리 넘기시죠."

    #‘나’ 
    나 "이렇게 혼자 아무것도 안 하고 있으면 심심하잖아."
 
    # 엘리 (침울, 침울, 무표정)
    엘리 "심심한 건 제가 아니라 당신이겠죠."

    독백 "흐르는 식은땀을 애써 숨기며 나는 다시 머릿속 줄거리에 집중했다."

    # ‘나’ 
    나 "참을 수 없는 고통에 신음하는 왕자님을 본 공주님은…."

    #엘리 (난처, 침울, 무표정)
    엘리 눈썹난처 "‘사랑의 키스로 왕자님의 병을 낫게 했다’, 뭐 그런 내용이 아닐까 싶습니다만."

    독백 "식은땀이 한번 더 흘렀다."

    # 엘리 (난처, 침울, 무표정)
    엘리 "제 수준을 얕잡아보는 데도 정도가 있죠."
    엘리 "<파르지팔> 원문이랑 백만 광년은 떨어진 내용에, 그마저도 유치하기 그지없어요."
    엘리 "그리고, 지금 펴신 부분, 책의 중간부가 아니던가요? 보통 주인공과 여주인공의 키스는 아무리 못해도 절정 부분에 다다라서야 나오지 않던가요?"

    독백 "연이어 정곡을 찔린 나. 전문 문학 평론가라고 해도 믿을 정도였다."
    독백 "어려 보이는 외모만 보고 일부러 수준을 낮췄는데, 부잣집 영애답게 만만히 볼 상대는 아니었던 모양이다."

    # 엘리 (보통, 웃음, 무표정)
    엘리 눈썹보통 눈웃음 입무표정 "…그래도 얼마 만일까요, 누군가가 제게 직접 책을 읽어준 것도."

    # ‘나’ 
    나 "응? 뭐라고 했어?"
 
    # 엘리 (침울, 실눈2, 무표정)
    엘리 눈썹침울 눈실눈웃음2 입무표정 "아무것도 아니에요."

    # 엘리 퇴장
 
    독백 "본인은 대충 얼버무렸지만, 난 그 쓸쓸한 미소를 다신 잊지 못할 것 같았다."

    scene black with dissolve

    return

label suitFitStory:

    hide screen exploreBase
    scene black with dissolve
    pause 1.25
    show text "To Whom; Who art thou?":
        align (.5, .5) rotate 180
    with dissolve
    pause 2.5
    hide text with dissolve
    pause 1.24

    scene black

    # 배경: 검은 화면
    # 효과음: 심장 소리 한 번

    독백 "답답하다, 숨이 막히고 가슴이 조여온다."
    독백 "하필이면 저택에 이런 게 있었을 줄이야, 당황스럽기 그지없다."
    
    # 효과음: 고조되는 심장 박동과 방문을 불규칙적으로 두드리는 소리
 
    독백 "처음 느껴보는 압박에 몸도 마음대로 움직여지지 않는다."
    독백 "도무지 벗어날 수가 없는데, 바깥에서는 협박조로 방문을 두드리고 있다."
    독백 "내가 옴짝달싹 못 하는 사이, 결국 참다 못해 방문을 제치고 들어온 누군가."

    # 엘리 (scg x, 텍스트만)
    엘리 "…퍽 잘 어울리시네요. 안에서 계속 우는 소리를 내시던 것 치고는 말이죠."

    # ECG 2 – 정장을 착용한 ‘난설’

    나 "…크읏, 어울리긴 무슨……. 이게 뭐야, 불편하기만 하고!"

    # 엘리 (scg x, 텍스트만)
    엘리 "어머, 제 자택에서 그만한 예복을 갖추기로 한 건 그쪽이 아니던가요?"
    엘리 "사이즈가 안 맞으니 제 드레스를 빌려드릴 순 없고, 그렇다고 비에 적신 그 후줄근한 옷을 계속 입고 있을 수도 없으니."
    엘리 "급한 대로 숙부님의 정장이라도 갖추셔야 마땅하지요."
 
    나 "그게 문제가 아니라, 내가 양복을 입어봤을 리도 없고! 나한테 사이즈도 하나도 안… 맞고……."

    독백 "체구만 쓸데없이 크다는 소리를 듣고 살던 나에게 이 흰색 양복은 너무 작았다."
    독백 "남성용 양복이라 그런지 가슴 부위가 특히 답답하고 조였다. 이유는 모르겠지만 인상을 더 찌푸리며 혀를 차는 엘리는 덤이었다."

    # 엘리 (scg x, 텍스트만)
    엘리 "…초대받지 않은 손님 주제에 쓸데없이 큰 탓이에요."
    엘리 "곧 식사 시간이니까 알아서 식당으로 내려오세요."
 
    # ‘나’ 
    나 "잠깐만, 아무리 그래도 같은 여자로서 조금이라도 도와줘야지! 야!"

    # 배경: bedroom

    scene bedroom
    show 엘리 눈썹침울 눈실눈웃음2 입무표정:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    # 엘리 (침울, 실눈2, 무표정)
    엘리 "당신과 같은 저급한 취급 마세요."

    # 엘리 (보통, 웃음, 무표정)
    엘리 눈썹보통 눈웃음 "그리고 아비게일, 아비게일 F. 엘리엇이예요, 아비든 애비든, 맘대로 부르시죠."
    hide 엘리 with dissolve

    # 엘리 퇴장

    독백 "소녀, 그러니까 아비게일은 내 외침도 무시한 채 다시 복도로 사라졌다."
    독백 "어울리지도 않는 양복을 반쯤 껴입은 채 방에 덩그러니 남겨진 나."
    독백 "…아무리 그래도 애비는 그러니까, 성씨를 따서 엘리라고 불러야겠다."

    scene black with dissolve

    return

label birdFeedStory:

    hide screen exploreBase

    scene black
    show text "마당 + 콜라 엘리":
        align (.0, .0)
    show 엘리 눈썹행복 눈웃음 입미소:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    독백 "한가롭게 저택 테라스에서 마당을 바라본다."
    독백 "석양이 진 하늘이 운치 있다. 노을빛이 조각상들을 하나하나 감싼다."
    # 엘리 (행복, 실눈웃음, 미소)
    독백 "그리고 내 옆에서는 엘리가 콜라를 쪽쪽 빨며 앉아 있다."
    독백 "미운 정도 고운 정이라고, 계속 지내다 보니 날 대하는 태도가 확실히 둥글어졌다."

    # 엘리 (행복, 웃음, 미소)
    엘리 "무슨 생각 해요?"
    # ‘나’ 
    나 "너 생각."
    # 엘리 (난처, 실눈 웃음, 미소)
    엘리 눈썹난처 눈실눈웃음1 "정말 실없는 소리만 하신다니까요. 이젠 그것도 마냥 싫지만은 않지만요."
 
    독백 "웃음도 많아진 엘리, 이젠 그냥 말괄량이 아가씨로밖에 안 보인다."
    독백 "끝을 찾아서 온 저택에 아련함과 행복함이 감돌았다. 나는 나지막이 입을 열었다."

    # ‘나’ 
    나 "음, 그냥."
    나 "이렇게 석양을 보다 보니 슬슬 집 생각이 나기도 해서."

    # 엘리 (행복, 웃음, 미소)
    엘리 눈썹행복 눈웃음 "아, 역시{nw}"
    # (본 대사가 출력되는 와중 - ‘두근두근 문예부’처럼 – 0.2초간 빠르게 
    # 엘리 scg: ‘놀람, 놀람(사백안), 무표정’
    # 대사: 어째서 (크고 붉은 글씨), 점프스케어 연출로 나타났다 사라짐.)
    # show 엘리 사백안
    show text "{color=#F00}{size=75}어째서{/size}{/color}":
        align (.5, .75)
    extend 눈썹놀람 눈사백안 입무표정 " {nw}{w=.2}"
    hide text
    extend 눈썹행복 눈웃음 입미소 "그러시겠죠."

    # 엘리 (침울, 실눈 웃음, 미소)
    엘리 눈썹침울 눈실눈웃음1 입미소 "언제까지고 이곳에 머무르기도 마땅찮은 노릇일 테니까요."
    독백 "홀로 저택을 지켜왔을 엘리를 보니 잠깐 미안한 감정이 들었다."
    독백 "일상에서 남들과 계속되는 불협화음과는 달리, 이곳에서는 편안하게 나 자신이 되어, 물감이 되어 한 폭의 그림에 섞일 수 있었다."
    독백 "동시에 알 수 있었다. 과거에서 바로 날아온 것 같은 이 저택에서 나는 엘리와는 다르게 어울리지 않는다는 사실을."
    독백 "이곳은 집처럼 편안하지만, 그럼에도 내 {i}집{/i}은 아니라는 생각을 떨쳐낼 수 없었다."
    독백 "여행을 떠나는 것처럼 팔을 활짝 벌린 조각상들을 보며, 문득 {i}사람은 여행을 떠나야만 집의 소중함을 알게 된다{/i}는 어느 오랜 경구가 떠올랐다."

    # 엘리 (행복, 웃음, 미소)
    엘리 눈썹행복 눈웃음 "……."
    엘리 "잠시 과일을 몇 개 깎아서 가져올게요. 새들이 좋아하거든요."

    독백 "나른해진 내가 감상에 도취된 사이 엘리는 새들에게 줄 과일을 가지러 일어섰다."
    독백 "단아하고 고급스러운 흰색 원단이 석양을 받아 발그레 물들었다."
    독백 "의자에 가만히 누워, 저택 안으로 사라지는 엘리의 뒷모습을 계속 바라보았다."

    scene black with dissolve

    return