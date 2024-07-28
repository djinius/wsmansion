default spriteDirection = "down"
default moveDirection = None
default positionX = 18
default positionY = 6

default objects = [("gloves", 3, 1), ("tarotbook", 28, 2), ("tornbook", 5, 11), ("page1", 15, 0), ("sketchbook", 21, 7), ("camera", 29, 6)]
default myInventory = []

image photoFound:
    "images/minigame/photo_large.png"
    "images/minigame/photo_dark.png" with Dissolve(1.)

transform fromRightAppear:
    xoffset 106
    easein .5 xoffset 6

transform foundTransform:
    pos (.5, .5) anchor (.5, .5)
    pause 2.75
    parallel:
        linear .75 xpos 1. xanchor 1. xoffset -6
    parallel:
        easein .75 ypos .0 yanchor .0 yoffset 6
    parallel:
        easeout .75 zoom .2 alpha .0

screen exploreBase(dim = False):
    tag explore
    default direction = None

    frame:
        xysize (1., 1.)
        background "images/minigame/map01.jpg"

        for (s, x, y) in objects:
            add "images/minigame/" + s + "_idle.png":
                pos getMapPosition(x, y) anchor (.5, .5)

        add getProSprite() pos getMapPosition(positionX, positionY) anchor (.5, .5)

        hbox:
            align (1., .0)
            if dim:
                at fromRightAppear
            else:
                xoffset 6
            for (n, o) in enumerate(myInventory):
                imagebutton:
                    auto "images/minigame/" + o + "_%s.png"
                    action NullAction()

    add "images/minigame/elly_idle.png":
        pos getMapPosition(19, 12) anchor (.5, .5)

screen exploreMap():
    tag explore

    modal True

    use exploreBase

    imagebutton:
        auto "images/minigame/elly_%s.png"
        pos getMapPosition(19, 12) anchor (.5, .5)
        action Return("Finished!!")

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
    tag explore

    default confirmed = False
    modal True

    use exploreBase(True)

    add "images/minigame/" + object + "_large_idle.png":
        at foundTransform

    timer 3.5 action Return()
    key "mouseup_1" action Return()

screen explorePhotoFound():
    tag explore

    modal True

    use exploreBase(True)

    add "photo_dark" at foundTransform

    timer 3.5 action Return()
    key "mouseup_1" action Return()

transform disappearExplain():
    alpha 1
    pause 2.5
    easeout 1.5 alpha .0

screen cameraMinigame:
    tag explore

    default blurry = 5.
    default saturation = 0.
    default rotateLeft = 60
    default rotateRight = 330
    default toRotate = None
    default rotating = None

    modal True

    use exploreBase(True)
    add Solid("#0004")

    frame:
        xysize (588, 800) align (.5, .5)
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
            idle "images/minigame/photo_large.png"
            align (.1, .5)
            action Return()

    elif blurry == 0.:
        add im.MatrixColor("images/minigame/photo_upside.png", im.matrix.saturation(saturation)) align (.1, .5)
    else:
        add im.MatrixColor(im.Blur("images/minigame/photo_upside.png", blurry), im.matrix.saturation(saturation)) align (.1, .5)

    add rotateHelper() xysize (0, 0) pos(0, 0)

    key "repeat_K_LEFT"    action NullAction()
    key "repeat_K_RIGHT"   action NullAction()
    key "repeat_K_UP"      action NullAction()
    key "repeat_K_DOWN"    action NullAction()

