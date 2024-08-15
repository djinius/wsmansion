default spriteDirection = "down"
default moveDirection = None
default positionX = 18
default positionY = 6
default explorePhase = 0
default mirrorBegin = False
default fragmentsFound = [False, False, False, False, False]
default isMirrorFound = False

# 탐색 오브젝트
# 파트 2 귀걸이 => 시계, 칼 => 자물쇠
default objectsPart1 = [("gloves", 27, 9), ("tornbook", 28, 5), ("page1", 25, 7), ("camera", 13, 6)]
default objectsPart2 = [("clock", 18, 5), ("page2", 10, 11), ("lock", 14, 14), ("mirror", 12, 9), ("frag0", 5, 5), ("frag1", 1, 1), ("frag2", 2, 2), ("frag3", 3, 3), ("frag4", 4, 4)]
default objects = []
default myInventory = []


image photoFound:
    "images/minigame/photo_large_idle.png"
    "images/minigame/photo_dark.png" with Dissolve(1.)

transform fromRightAppear(count):
    xoffset (100 * count + 6)
    easein (.5*count) xoffset 6

transform foundTransform(xp=.5):
    pos (xp, .5) anchor (.5, .5)
    pause 2.75
    parallel:
        linear .75 xpos 1. xanchor 1. xoffset -6
    parallel:
        easein .75 ypos .0 yanchor .0 yoffset 6
    parallel:
        easeout .75 zoom .2 alpha .0

screen exploreBase(dim = 0):
    tag explore

    transclude

    hbox:
        align (1., .0)
        at fromRightAppear(dim)

        for (n, o) in enumerate(myInventory):
            imagebutton:
                auto "images/minigame/" + o + "_%s.png"
                action NullAction()


## TODO: 이동에 따라 맵 위치 같이 옮겨주기
screen exploreMap():
    tag explore

    modal True

    use exploreBase():
        imagebutton:
            auto "images/minigame/elly_%s.png"
            pos getMapPosition(14, 8) anchor (.5, .5)
            action Return("elly!!")

    key "K_LEFT"    action Function(movePos, xp = -1, yp = 0)
    key "K_RIGHT"   action Function(movePos, xp = 1, yp = 0)
    key "K_UP"      action Function(movePos, xp = 0, yp = -1)
    key "K_DOWN"    action Function(movePos, xp = 0, yp = 1)

    key "repeat_K_LEFT"    action NullAction()
    key "repeat_K_RIGHT"   action NullAction()
    key "repeat_K_UP"      action NullAction()
    key "repeat_K_DOWN"    action NullAction()

    add moveHelper() xysize (0, 0) pos(0, 0)

    if moveDirection is not None:
        timer .2 repeat True action Function(movePos)

screen exploreFound(object):

    default confirmed = False
    modal True

    use exploreBase(1)

    add "images/minigame/" + object + "_large_idle.png":
        at foundTransform

    timer 3.5 action Return()
    key "mouseup_1" action Return()

screen explorePhotoFound():
    tag explore

    modal True

    use exploreBase(2)

    add "images/minigame/camera_large_idle.png" at foundTransform(.35)
    add "photoFound" zoom .6 at foundTransform(.65)

    timer 3.5 action Return()
    key "mouseup_1" action Return()

screen mirrorFragmentFound(object):
    tag explore

    default confirmed = False
    modal True

    use exploreBase(False)

    add "images/minigame/" + object + "_large_idle.png":
        at foundTransform

    timer 3.5 action Return()
    key "mouseup_1" action Return()

transform disappearExplain():
    alpha 1
    pause 2.5
    easeout 1.5 alpha .0

screen cameraMinigame:
    tag puzzle

    default blurry = 5.
    default saturation = 0.
    default rotateLeft = 60
    default rotateRight = 330
    default toRotate = None
    default rotating = None

    modal True

    add Solid("#0004")

    frame:
        xysize (588, 800) align (.75, .5)
        padding (0, 0)
        background "images/minigame/camera_minigame.png"

        frame:
            xysize (320, 197)
            padding (2, 2, 2, 50)
            pos (74, 400) anchor (.0, 1.)
            background "images/minigame/biexplainballoon.png"
            text "다이얼을 돌려서\n사진을 선명하게 만들어 보세요." color "#000" size 22 align (.5, .5) text_align .5
            at disappearExplain

        imagebutton:
            pos (104, 439) anchor (.5, .5)
            insensitive "images/minigame/camera_leftdial_idle.png"
            idle Transform("images/minigame/camera_leftdial_idle.png", rotate=rotateLeft)
            if toRotate == "Left":
                hover Transform("images/minigame/camera_leftdial_hover.png", rotate=rotateLeft)
            selected_idle Transform("images/minigame/camera_leftdial_selected.png", rotate=rotateLeft)
            selected_hover Transform("images/minigame/camera_leftdial_selected.png", rotate=rotateLeft)
            selected (rotating == "Left")
            action NullAction()

        imagebutton:
            pos (358, 442) anchor (.5, .5)
            insensitive "images/minigame/camera_rightdial_idle.png"
            idle Transform("images/minigame/camera_rightdial_idle.png", rotate=rotateRight)
            if toRotate == "Right":
                hover Transform("images/minigame/camera_rightdial_hover.png", rotate=rotateRight)
            selected_idle Transform("images/minigame/camera_rightdial_selected.png", rotate=rotateRight)
            selected_hover Transform("images/minigame/camera_rightdial_selected.png", rotate=rotateRight)
            selected (rotating == "Right")
            action NullAction()

    if blurry == 0. and saturation == 1.:
        imagebutton:
            auto "images/minigame/photo_large_%s.png"
            align (.1, .5)
            action Return('complete')

    elif blurry == 0.:
        add im.MatrixColor("images/minigame/photo_upside.png", im.matrix.saturation(saturation)) align (.1, .5)
    else:
        add im.MatrixColor(im.Blur("images/minigame/photo_upside.png", blurry), im.matrix.saturation(saturation)) align (.1, .5)

    add rotateHelper() xysize (0, 0) pos(0, 0)
    textbutton "다른 곳을 탐색한다":
        align (1., 1.)
        action Return()

    key "repeat_K_LEFT"    action NullAction()
    key "repeat_K_RIGHT"   action NullAction()
    key "repeat_K_UP"      action NullAction()
    key "repeat_K_DOWN"    action NullAction()

define mirrorFragDropPoses = [
    (670+131, 564),
    (670+131, 429),
    (670+227, 429),
    (670+312, 463),
    (670+131, 570)]

define mirrorDragPoses = [getMirrorFragmentPosition(), getMirrorFragmentPosition(), getMirrorFragmentPosition(), getMirrorFragmentPosition(), getMirrorFragmentPosition()]

default mirrorFragMatches = [False, False, False, False, False]

# 거울 미니게임
screen mirrorMiniGame():
    tag puzzle
    modal True

    add Solid("#000")

    frame:
        xysize (1., 1.)
        align (.5, .5)
        padding (0, 0)
        background None

        has draggroup

        drag:
            idle_child "images/minigame/mirror/mirror_empty.png"
            align (.5, .5)
            draggable False
            droppable False

        for (n, t) in enumerate(fragmentsFound):
            if t and (mirrorFragMatches[n] is False):
                drag:
                    drag_name n
                    align mirrorDragPoses[n]

                    draggable True
                    droppable False
                    dragged fragmentDropped

                    has imagebutton
                    idle "images/minigame/mirror/frag"+str(n)+"_large_idle.png"
                    hover "images/minigame/mirror/frag"+str(n)+"_large_idle.png"
                    selected_idle "images/minigame/mirror/frag"+str(n)+"_large_idle.png"
                    selected_hover "images/minigame/mirror/frag"+str(n)+"_large_idle.png"
                    sensitive False
                    action NullAction()
                    mouse "drag"

        for (n, p) in enumerate(mirrorFragDropPoses):
            drag:
                drag_name n
                if (mirrorFragMatches[n] is False):
                    idle_child "images/minigame/mirror/frag"+str(n)+"_drop.png"
                else:
                    idle_child "images/minigame/mirror/frag"+str(n)+"_large_idle.png"

                hover_child "images/minigame/mirror/frag"+str(n)+"_drop.png"
                selected_child "images/minigame/mirror/frag"+str(n)+"_large_idle.png"
                selected_hover_child "images/minigame/mirror/frag"+str(n)+"_drop.png"
                pos p

                draggable False
                droppable (mirrorFragMatches[n] is False)

    textbutton "더 탐색해 본다":
        align (1., 1.)
        action Return()

# 시계 메모
screen clockPuzzle():
    tag puzzle

    frame:
        align (.5, .5)
        background "images/minigame/memo.png"
        xysize (711, 910)

        has vbox
        align (.5, .5)

        text "수수께끼" size 40 color "#000"
        null height(15)
        text clockMemoText size 25 color "#000"

    key "mousedown_1" action Return()

    textbutton "다른 곳을 탐색한다":
        align (1., 1.)
        action Return()

# 자물쇠 풀기
screen lockPuzzle():
    tag puzzle

    default lockNumber0 = 0
    default lockNumber1 = 0
    default lockNumber2 = 0
    default lockNumber3 = 0

    add Solid("#000C")

    hbox:
        style_prefix "lockPuzzle"
        align (.5, .5)
        grid 4 4:
            yalign .5

            text "O" xalign .5
            text "U" xalign .5
            text "O" xalign .5
            text "X" xalign .5

            textbutton "▲" action SetScreenVariable("lockNumber0", (lockNumber0 + 1) % 10) xalign .5
            textbutton "▲" action SetScreenVariable("lockNumber1", (lockNumber1 + 1) % 10) xalign .5
            textbutton "▲" action SetScreenVariable("lockNumber2", (lockNumber2 + 1) % 10) xalign .5
            textbutton "▲" action SetScreenVariable("lockNumber3", (lockNumber3 + 1) % 10) xalign .5

            text "%d"%lockNumber0 xalign .5
            text "%d"%lockNumber1 xalign .5
            text "%d"%lockNumber2 xalign .5
            text "%d"%lockNumber3 xalign .5

            textbutton "▼" action SetScreenVariable("lockNumber0", (lockNumber0 - 1) % 10) xalign .5
            textbutton "▼" action SetScreenVariable("lockNumber1", (lockNumber1 - 1) % 10) xalign .5
            textbutton "▼" action SetScreenVariable("lockNumber2", (lockNumber2 - 1) % 10) xalign .5
            textbutton "▼" action SetScreenVariable("lockNumber3", (lockNumber3 - 1) % 10) xalign .5

        null width(50)
        textbutton "열기":
            yalign .5
            action [SetVariable("isBedroomUnlocked", True), Return()]
            sensitive (lockNumber0 == 1) and (lockNumber1 == 3) and (lockNumber2 == 1) and (lockNumber3 == 2)

    textbutton "다른 곳을 탐색한다":
        align (1., 1.)
        action Return()

style lockPuzzle_text:
    size 100

style lockPuzzle_button_text is button_text:
    size 100

# 0: 침실
# 1: 침실 -> 거실
# 2: 거실 -> 침실
# 3: 거실
# 4: 거실 -> 서재
# 5: 서재 -> 거실
# 6: 서재
default explorePosition = 3

transform swipeRoom(frompos, topos):
    xoffset frompos
    easeout .5 xoffset (frompos + topos) / 2
    easein .5 xoffset topos

screen exploreRooms():
    tag explore

    hbox:
        pos (0, 0) anchor(0, 0) spacing 0

        # 침실
        imagemap:
            auto "images/minigame/bedroom_%s.png"
            # 거울조각 4
            hotspot (1606, 954, 156, 110):
                action Return("frag3")
                sensitive (explorePhase == 2) and ("frag3" not in myInventory)
            # 거울조각 3
            hotspot (499, 882, 112, 151):
                action Return("frag2")
                sensitive (explorePhase == 2) and ("frag2" not in myInventory)
            # 페이지 2
            hotspot (950, 687, 175, 175):
                action Return("page2")
                sensitive "page2" not in myInventory

        # 거실
        imagemap:
            auto "images/minigame/living_%s.png"
            # 거울조각 1
            hotspot (1021, 956, 142, 265):
                action Return("frag0")
                sensitive (explorePhase == 2) and ("frag0" not in myInventory)
            # 거울조각 2
            hotspot (367, 918, 154, 151):
                action Return("frag1")
                sensitive (explorePhase == 2) and ("frag1" not in myInventory)
            # 카메라
            hotspot (1549, 423, 135, 177):
                action Return("camera")
                sensitive "camera" not in myInventory
            # 시계
            hotspot (966, 107, 144, 277):
                action Return("clock")
                sensitive explorePhase == 2
            # 자물쇠
            hotspot (0, 535, 108, 195):
                action Return("lock")
                sensitive (explorePhase == 2) and (isBedroomUnlocked is False)
            # 엘리
            hotspot (1190, 267, 323, 719):
                action Return("elly!!")

        # 서재
        imagemap:
            auto "images/minigame/study_%s.png"
            # 찢어진 책
            hotspot (549, 833, 156, 91):
                action Return("tornbook")
                sensitive "tornbook" not in myInventory
            # 페이지 1
            hotspot (795, 883, 175, 175):
                action Return("page1")
                sensitive "page1" not in myInventory
            # 거울조각 5
            hotspot (390, 719, 106, 125):
                action Return("frag4")
                sensitive (explorePhase == 2) and ("frag4" not in myInventory)
            # 장갑
            hotspot (914, 247, 140, 140):
                action Return("gloves")
                sensitive "gloves" not in myInventory

        if explorePosition == 0:
            xoffset 0
        elif explorePosition == 1:
            at swipeRoom(0, -1920)
            timer 1. action SetVariable("explorePosition", 3)
        elif explorePosition == 2:
            at swipeRoom(-1920, 0)
            timer 1. action SetVariable("explorePosition", 0)
        elif explorePosition == 3:
            xoffset -1920
        elif explorePosition == 4:
            at swipeRoom(-1920, -3840)
            timer 1. action SetVariable("explorePosition", 6)
        elif explorePosition == 5:
            at swipeRoom(-3840, -1920)
            timer 1. action SetVariable("explorePosition", 3)
        elif explorePosition == 6:
            xoffset -3840

    if (explorePosition == 0) or (explorePosition == 3):
        key "K_RIGHT" action SetVariable("explorePosition", explorePosition + 1)
    else:
        key "K_RIGHT" action NullAction()

    if ((explorePosition == 3) and (isBedroomUnlocked is True)) or (explorePosition == 6):
        key "K_LEFT" action SetVariable("explorePosition", explorePosition - 1)
    else:
        key "K_LEFT" action NullAction()

    imagebutton:
        auto "images/minigame/prev_%s.png"
        align (.0, .5) xoffset 10
        action SetVariable("explorePosition", explorePosition - 1)
        sensitive ((explorePosition == 3) and (isBedroomUnlocked is True)) or (explorePosition == 6)

    imagebutton:
        auto "images/minigame/next_%s.png"
        align (1., .5) xoffset -10
        action SetVariable("explorePosition", explorePosition + 1)
        sensitive (explorePosition == 0) or (explorePosition == 3)

    key "K_UP" action NullAction()
    key "K_DOWN" action NullAction()
    key "repeat_K_LEFT"    action NullAction()
    key "repeat_K_RIGHT"   action NullAction()
    key "repeat_K_UP"      action NullAction()
    key "repeat_K_DOWN"    action NullAction()
