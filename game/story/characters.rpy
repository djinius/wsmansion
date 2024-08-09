# CTC
image ctc icon:
    Text("{color=#0000}▷{/color}")
    pause .5
    Text("▷")
    pause .5
    repeat


# 게임에서 사용할 캐릭터를 정의합니다.
define 독백 = Character(None, ctc = "ctc icon", ctc_position = 'nestled-close')
define 나 = Character('나', color="#C5CAB6", ctc = "ctc icon", ctc_position = 'nestled-close', who_prefix="‘", who_suffix="’", what_prefix="“", what_suffix="”")
define 엘리 = Character('엘리', color="#FFDF01", image="엘리", ctc = "ctc icon", ctc_position = 'nestled-close')
define 아비게일 = Character('아비게일 F. 엘리엇', color="#FFDF01", image="아비게일", ctc = "ctc icon", ctc_position = 'nestled-close')
define 아비게일처음 = Character('???', color="#FFDF01", image="아비게일처음", ctc = "ctc icon", ctc_position = 'nestled-close')

# 눈물, 음영 - 780, 183
# 눈썹 - 830, 299
# 눈 - 845, 297
# 입 - 904, 625

layeredimage 엘리:
    group 신체:
        attribute 드레스 default:
            "images/standings/elly/body.png"

    group 눈썹:
        pos (830, 299)

        attribute 눈썹보통 default:
            "images/standings/elly/eyebrows_normal.png"
        attribute 눈썹행복:
            "images/standings/elly/eyebrows_happy.png"
        attribute 눈썹침울:
            "images/standings/elly/eyebrows_timid.png"
        attribute 눈썹놀람:
            "images/standings/elly/eyebrows_surprised.png"
        attribute 눈썹난처:
            "images/standings/elly/eyebrows_embarrassed.png"

    group 눈:
        pos (845, 297)
        
        attribute 눈보통 default:
            Null()
        attribute 눈웃음:
            "images/standings/elly/eyes_laugh.png"
        attribute 눈실눈웃음1:
            "images/standings/elly/eyes_laughclosed.png"
        attribute 눈실눈웃음2:
            "images/standings/elly/eyes_laughhalfclosed.png"
        attribute 눈미카웃음:
            "images/standings/elly/eyes_mikalaugh.png"
        attribute 눈미카놀람:
            "images/standings/elly/eyes_mikasurprised.png"
        attribute 눈침울:
            "images/standings/elly/eyes_timid.png"
        attribute 눈사백안:
            "images/standings/elly/eyes_wideopen.png"

    group 입:
        pos (904, 625)
        
        attribute 입무표정 default:
            "images/standings/elly/mouth_wooden.png"
        attribute 입미소:
            "images/standings/elly/mouth_smile.png"
        attribute 입웃음:
            "images/standings/elly/mouth_laugh.png"
        attribute 입놀람:
            "images/standings/elly/mouth_surprised.png"


    group 눈물:
        pos (780, 183)

        attribute 눈물없음 default:
            Null()
        attribute 눈물:
            "images/standings/elly/tears_openeyes.png"
        attribute 눈물실눈:
            "images/standings/elly/tears_closedeyes.png"

    group 음영:
        pos (780, 183)

        attribute 음영없음 default:
            Null()
        attribute 음영있음:
            "images/standings/elly/darkface.png"

#image side 엘리 = LayeredImageProxy("엘리", Transform(crop=(0, 0, 2000, 2000), zoom=.2))
#image side 엘리 투명 = Null()

image 아비게일 = LayeredImageProxy("엘리")
#image side 아비게일 = LayeredImageProxy("엘리", Transform(crop=(0, 0, 2000, 2000), zoom=.2))
#image side 아비게일 투명 = Null()

image 아비게일처음 = LayeredImageProxy("아비게일")
#image side 아비게일처음 = LayeredImageProxy("아비게일", Transform(crop=(0, 0, 2000, 2000), zoom=.2))
#image side 아비게일처음 투명 = Null()

