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

    def moveDown():
        global positionX
        global positionY
        global moveDirection

        if positionY < 12:
            positionY += 1
        moveDirection = "down"

    def moveLeft():
        global positionX
        global positionY
        global moveDirection

        if positionX > 0:
            positionX -= 1
        moveDirection = "left"

    def moveRight():
        global positionX
        global positionY
        global moveDirection

        if positionX < 37:
            positionX += 1
        moveDirection = "right"

    def getProPosition():
        global positionX
        global positionY
        return (positionX * 50 + 20, positionY * 50 + 300)

default moveDirection = "down"
default positionX = 18
default positionY = 6

screen explore01:
    modal True
    frame:
        xysize (1., 1.)
        background "images/minigame/map01.jpg"
        add getProSprite() pos getProPosition() anchor (.5, .5)

    key "K_LEFT"    action Function(moveLeft)
    key "K_RIGHT"   action Function(moveRight)
    key "K_UP"      action Function(moveUp)
    key "K_DOWN"    action Function(moveDown)

    textbutton "닫기":
        align (.05, 1.)
        action Return()
