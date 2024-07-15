init python:
    def getProSprite():
        global moveDirection
        return "nanseol walk " + moveDirection

    def moveUp():
        global positionX
        global positionY
        global moveDirection

        if positionY > 0:
            positionY -= 1
        moveDirection = "up"

        return explorePosition(positionX, positionY)

    def moveDown():
        global positionX
        global positionY
        global moveDirection

        if positionY < 12:
            positionY += 1
        moveDirection = "down"

        return explorePosition(positionX, positionY)

    def moveLeft():
        global positionX
        global positionY
        global moveDirection

        if positionX > 0:
            positionX -= 1
        moveDirection = "left"

        return explorePosition(positionX, positionY)

    def moveRight():
        global positionX
        global positionY
        global moveDirection

        if positionX < 37:
            positionX += 1
        moveDirection = "right"

        return explorePosition(positionX, positionY)

    def explorePosition(xp, yp):
        global objects

        for (s, x, y) in objects:
            if x == xp and y == yp:
                return s

    def getMapPosition(x, y):
        return (x * 50 + 20, y * 50 + 300)

    def objectFound(object):
        for k in objects:
            (s, x, y) = k
            if s == object:
                objects.remove(k)
                found.append(object)

default moveDirection = "down"
default positionX = 18
default positionY = 6

default objects = [("ring", 3, 1), ("snowball", 28, 2), ("angel", 5, 11), ("monkey", 15, 0), ("maria", 21, 7), ("camera", 29, 6)]
default found = []

transform fromRightAppear:
    xoffset 106
    easein .5 xoffset 6

transform foundTransform:
    pos (.5, .5) anchor (.5, .5)
    parallel:
        linear .75 xpos 1. xanchor 1. xoffset -6
    parallel:
        easein .75 ypos .0 yanchor .0 yoffset 6
    parallel:
        easeout .75 zoom .2 alpha .0

screen exploreBase(dim = False):
    tag explore

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
            for (n, o) in enumerate(found):
                imagebutton:
                    auto "images/minigame/" + o + "_%s.png"
                    action NullAction()
            

screen exploreMap():
    tag explore

    modal True

    use exploreBase

    key "K_LEFT"    action Function(moveLeft)
    key "K_RIGHT"   action Function(moveRight)
    key "K_UP"      action Function(moveUp)
    key "K_DOWN"    action Function(moveDown)

    textbutton "닫기":
        align (.05, 1.)
        action Return("Finished!!")

screen exploreFound(object):
    tag explore

    default confirmed = False
    modal True

    use exploreBase(True)

    if confirmed:
        add "images/minigame/" + object + "_large.png":
            at foundTransform

        timer 1. action Return()
        key "mouseup_1" action Return()

    else:
        imagebutton:
            idle "images/minigame/" + object + "_large.png"
            pos (.5, .5) anchor (.5, .5)
            action SetScreenVariable("confirmed", True)


screen cameraMinigame:
    tag explore

    default blurry = 5.
    default saturation = 0.

    modal True
    use exploreBase(True)
    add Solid("#0004")

    add "images/minigame/camera.png" align (.5, .5)
    if blurry == 0.:
        add im.MatrixColor("images/minigame/photo_upside.png", im.matrix.saturation(saturation)) align (.1, .5)
    else:
        add im.MatrixColor(im.Blur("images/minigame/photo_upside.png", blurry), im.matrix.saturation(saturation)) align (.1, .5)

    key "K_LEFT"    action If(blurry==0. and saturation==1., Return(), SetScreenVariable("blurry", max(0., blurry - .5)))
    key "K_RIGHT"   action If(blurry==0. and saturation==1., Return(), SetScreenVariable("blurry", blurry + .5))
    key "K_UP"      action If(blurry==0. and saturation==1., Return(), SetScreenVariable("saturation", max(0., saturation - .1)))
    key "K_DOWN"    action If(blurry==0. and saturation==1., Return(), SetScreenVariable("saturation", min(1., saturation + .1)))


