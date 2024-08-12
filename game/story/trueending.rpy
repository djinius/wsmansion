label trueEnding:

    scene garden with dissolve
    독백 "{i}내가 네 멱살을 쥐려고 들 때,{/i} 나는 대답했다."

    # 엘리 등장
    # 엘리 (음영 on, 놀람, 웃음, 미소)
    show 엘리 눈썹놀람 눈웃음 입미소 눈물 음영있음:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve
    엘리 "아아, 그렇군요."

    # 엘리 (음영 on, 보통, 실눈 웃음, 미소, 눈물)
    엘리 눈썹보통 눈실눈웃음1 "…다행이에요. 정말 다행이야."

    독백 "영문 모를 반응의 엘리."

    # 엘리 (놀람, 실눈 웃음, 미소)
    엘리 눈썹놀람 입미소 음영제거 "실은 이번엔 저도 당신을 돕고 싶었답니다."

    # 엘리 (행복, 웃음, 미소)
    엘리 눈썹행복 눈웃음 입미소 "그땐 고집을 조금 부렸지만, {i}no place like home{/i}, 집만한 곳은 없잖아요?"

    독백 "이해가 가지 않는다."
    독백 "본인의 행복 운운하며 나를 이 저택에 잡아두려던 게 아니었나?"

    # 엘리 (행복, 웃음, 미소)
    엘리 "거짓말 아니랍니다."
    엘리 "저도 이젠 어리광에서 졸업할 나이라는 걸 깨달았어요."
    엘리 "뭐, 이 저택에서 '나이'의 의미가 있는지는 둘째치고서라도…."

    # 엘리 (행복, 실눈 웃음, 미소)
    엘리 눈썹행복 눈실눈웃음 입미소 "결국엔, 이것도 전부 당신 덕분이겠죠."
    엘리 "그리고 몸이 조각상이 되는 불상사는 없을 거랍니다. 제 가족들과는 다르게 말이에요."

    # 엘리 (행복, 웃음, 미소)
    엘리 눈썹행복 눈웃음 입미소 "이미 당신도 저처럼 저택과 동화된 지 오래라, 무리만 하지 않으신다면 그 새들처럼 굳지는 않을 거에요, 후훗."

    # 엘리 (음영 on, 보통, 사백안, 무표정)
    엘리 음영 눈썹보통 눈사백안 입무표정 "{font=Danjo-bold-Regular.otf}그러니까 빨리 제 눈앞에서 꺼져버리세요. 제 마음이 변하기 전에.{/font}"

    독백 "소름 끼치는 엘리의 모습은 그렇다 치더라도, 내 기억과 상충되는 엘리의 태도에 떨떠름함을 감출 수 없었다."
    독백 "동시에, 내게 이 기회가 두 번 다시 찾아오지 않으리라는 것도 잘 알고 있었다."
    
    # 엘리 퇴장
    # 배경: 조각상
    scene black
    show text "조각상":
        align (.0, .0)
    with dissolve

    독백 "마지막으로 엘리와 악수를 나눈 뒤, 난 그대로 조각상들이 있는 곳을 향했다."
    독백 "엘리의 말대로 몸이 굳는 일은 일어나지 않았다."

    # 배경: forest1
    scene forest1 with dissolve

    독백 "저만치에 울창한 나무들이 겹쳐 만들어진 길이 나타났다."
    독백 "심히 불길했지만, 저곳 외에는 나가는 길이 보이지 않았다."

    # 배경: forest2_1
    scene forest2_1 with dissolve
    독백 "갑자기 피로가 몰려오는 몸을 이끌고 어두운 숲 속으로 들어갔다."

    # 배경: forest2_2
    scene forest2_2 with dissolve
    독백 "나뭇잎 밟히는 소리가 귀를 간질였다."

    # 배경: forest2_3
    scene forest2_3 with dissolve
    독백 "몸이 너무나도 무거웠다, 같은 길을 빙빙 도는 느낌, 이 길이 맞기는 한 걸까."

    # 배경: forest2_4
    scene forest2_4 with dissolve
    독백 "그럴 일은 절대 없겠지만, 다시 저택으로 돌아가기에도 너무나 멀리 와 버렸다."
    독백 "한치 앞도 보이지 않는 풀숲 위에 쓰러지며 나는 물었다."

    # 배경: 검은색 배경
    scene black with dissolve

    독백 "{i}내가 누구였지?{/i}"

    # 배경: 살구색 배경, NVL
    scene apricot with dissolve

    # 배경: home
    nvl clear
    엘리NVL "…경애하는 그대에게,"
    엘리NVL "이 말을 듣지는 못하시겠지만, 꼭 전하고 싶었어요."
    엘리NVL "말썽꾸러기에 거짓말쟁이라 정말 미안했다고요."
    엘리NVL "석양을 가리는 구름이 떨리고, 수풀이 떨리는 기척이 느껴질 때마다 알 수 있었어요."
    엘리NVL "저와 이 저택에 관한 이야기가 몇몇 이들에 의해 세상에 퍼진 지 꽤 되었고, 일부는 직접 찾아오기도 했으며,"
    엘리NVL "특별히 멍청한 이들은 돌이 되어버렸다는 걸요."
    엘리NVL "그러거나 말거나 전 신경도 쓰지 않았답니다."
    엘리NVL "저는 금방 잊히고 말 시시한 괴담 속 유령이자, 세상이라는 한 연극 속 조연일 뿐."
    엘리NVL "누군가 구해줄 거란 희망은, 희뿌예지는 과거의 기억과 함께 버린 지 오래였어요."

    # 배경: rain
    nvl clear
    scene rain with dissolve
    엘리NVL "60년 만에 처음으로 저택에 비가 내리던 그 날을 제외하고 말이에요."
    엘리NVL "제 앞에서 억지로 미소 짓는, 금방이라도 무너질 듯한 당신의 두 눈을 보았을 때."
    엘리NVL "모든 것이 흐려진 제 마음에 무언가 다시 피어나는 것을 느꼈어요."
    엘리NVL "낡고 해진 종이 위로, 다시 펜을 들어 이야기를 써 내려가기 시작한 거예요."

    #배경: study1
    nvl clear
    scene study1 with dissolve
    엘리NVL "제가 처음에 툴툴댔던 거, 기억나요?"
    엘리NVL "너무 오랜만에 어리광을 부리다 보니 익숙하지 않기도 했지만, 일부러 모질게 군 것도 없잖아 있었어요."
    엘리NVL "정원에 핀 꽃들이 아침 햇살을 향해 목을 뻗듯, 당신의 온화함에 몸과 마음을 모두 내어줄까 봐."
    엘리NVL "당신이 다가올 때마다 저는 제가 꺾이기라도 할 듯 가시를 세웠어요."
    엘리NVL "사실은 제 목이 꺾이더라도 누군가 제개 와주길 바랬으면서, 참 제멋대로죠."

    #배경: flowers
    nvl clear
    scene flowers with dissolve
    엘리NVL "그래요, 저는 진즉에 알고 있었는지도 몰라요."
    엘리NVL "언젠가 당신이 절 떠날 순간이 온다는 사실을 말이에요."
    엘리NVL "그렇게 되면 전 다시 홀로 남겨지고, 제 남은 기억과 존재 모두 잊히고 말겠죠."
    엘리NVL "사라지는 것과 다름없는 일이겠죠."
    엘리NVL "그게 너무나도 두려웠어요. 너무나."

    # 배경: living
    # 엘리 (음영 on, 사백안, 웃음, 미소)
    scene living
    show 엘리 눈썹놀람 눈웃음 입미소 눈물 음영있음:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    엘리 눈썹웃음 눈사백안 입미소 음영있음 "…그래서, 일부러 당신을 죽였어요."
    엘리 "적어도 당신의 영혼은 이곳에 남아 떠돌 수 있게 말이에요."
    엘리 "이곳에 오래 살다 보니, 기억을 되살리진 못해도 어느 정도 잠재우는 법도 알아낸 참이었고요."
    엘리 "그걸 반복하고, 또 반복하며, 몸도 영혼도 저택과 하나가 되는 거에요."
    엘리 "우리가 함께 잠들 수 있으면 좋겠어요. 영원히 행복한 둘만의 꿈속에서."

    # 효과음: 노크 소리와 끼이익- 하는 문소리
    # 엘리 등장
    # 엘리 (음영 off, 행복, 웃음, 미소)
    엘리 눈썹행복 눈웃음 입미소 "아, 마침 다시 오셨나 봐요."

    # 엘리 (음영 off, 행복, 실눈 웃음, 미소)
    엘리 눈썹행복 눈실눈웃음 입미소 "늘 똑같지만, 가장 기대되는 순간도 언제나 지금이라니까요."

    # 엘리 퇴장
    # 배경: 검은 화면
    scene black with dissolve

    # 엘리 (scg x)
    엘리 "그러니 당신도 정말, {i}그렇게 함부로 돌아다니면 못 쓴다니까요?{/i}"

    # 타이틀 화면으로 복귀
    $ persistent.skyBackground = False

    return
