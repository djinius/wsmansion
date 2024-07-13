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

default objects = [("ring", 3, 1), ("snowball", 28, 5), ("angel", 5, 11), ("monkey", 30, 0), ("maria", 21, 7)]
default found = []

transform fromRightAppear:
    xoffset 106
    pause 3.
    easein .5 xoffset 6

transform foundTransform:
    pos (.5, .5) anchor (.5, .5)
    pause 2.
    parallel:
        linear 1. xpos 1. xanchor 1. xoffset -6
    parallel:
        easein 1. ypos .0 yanchor .0 yoffset 6
    parallel:
        easeout 1. zoom .2 alpha .0

screen exploreBase(dim = False):
    frame:
        xysize (1., 1.)
        background "images/minigame/map01.jpg"

        for (s, x, y) in objects:
            imagebutton:
                pos getMapPosition(x, y) anchor (.5, .5)
                auto "images/minigame/" + s + "_%s.png"
                action NullAction()

        add getProSprite() pos getMapPosition(positionX, positionY) anchor (.5, .5)

        hbox:
            align (1., .0)
            if dim:
                at fromRightAppear
            else:
                xoffset 6
            for (n, o) in enumerate(found):
                add "images/minigame/" + o + "_idle.png"
            

screen exploreMap():
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
    modal True

    use exploreBase(True)

    add "images/minigame/" + object + "_large.png":
        at foundTransform

    timer 3.5 action Return()
    key "mouseup_1" action Return()
