# 게임에서 사용할 캐릭터를 정의합니다.
define 나 = Character(None)
define 난설 = Character('난설', color="#C5CAB6")
define 엘리 = Character('엘리', color="#FFDF01", image="엘리")
define 아비게일 = Character('아비게일 F. 엘리엣', color="#FFDF01", image="아비게일")
define 아비게일처음 = Character('??', color="#FFDF01", image="아비게일처음")

layeredimage 엘리:
    group body:
        attribute 드레스 default:
            "images/standings/elly_body.png"

    group 얼굴:
        attribute 보통 default:
            Text("{size=150}보통{/size}")
        attribute 미소:
            Text("{size=150}미소{/size}")
        attribute 난처:
            Text("{size=150}난처{/size}")
        attribute 침울:
            Text("{size=150}침울{/size}")
        attribute 행복:
            Text("{size=150}행복{/size}")
        attribute 궁금:
            Text("{size=150}궁금{/size}")
        attribute 놀람:
            Text("{size=150}놀람{/size}")
        attribute 당혹:
            Text("{size=150}당혹{/size}")
        attribute 무표정:
            Text("{size=150}무표정{/size}")
        attribute 입벌림:
            Text("{size=150}입벌림{/size}")
        attribute 사백안:
            Text("{size=150}사백안{/size}")
        attribute 장난스러움:
            Text("{size=150}장난스러움{/size}")

image side 엘리 = LayeredImageProxy("엘리", Transform(crop=(0, 0, 2000, 2000), zoom=.2))
image side 엘리 투명 = Null()

image 아비게일처음 = LayeredImageProxy("엘리")
image side 아비게일처음 = LayeredImageProxy("엘리", Transform(crop=(0, 0, 2000, 2000), zoom=.2))
image side 아비게일처음 투명 = Null()

image 아비게일 = LayeredImageProxy("엘리")
image side 아비게일 = LayeredImageProxy("엘리", Transform(crop=(0, 0, 2000, 2000), zoom=.2))
image side 아비게일 투명 = Null()

