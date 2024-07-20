"""renpy
init python:
"""

import pygame

###############################################################################
# 이동용 CDD
###############################################################################
class moveHelper(renpy.Displayable):
    def __init__(self, **kwargs):
        super(moveHelper, self).__init__(**kwargs)

    def render(self, width, height, st, at):
        # Get the size of the child.
        # self.width, self.height = child_render.get_size()
        # Create the render we will return.
        render = renpy.Render(0, 0)
        # Return the render.
        return render

    def event(self, ev, x, y, st):
        global moveDirection
        global spriteDirection

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT:
                moveDirection = "left"
            if ev.key == pygame.K_RIGHT:
                moveDirection = "right"
            if ev.key == pygame.K_UP:
                moveDirection = "up"
            if ev.key == pygame.K_DOWN:
                moveDirection = "down"

        elif ev.type == pygame.KEYUP:
            moveDirection = None

        return None

def getProSprite():
    global spriteDirection
    return "nanseol walk " + spriteDirection

def movePos(xp = 0, yp = 0):
    global positionX
    global positionY
    global moveDirection
    global spriteDirection

    print(moveDirection)

    if (xp == 0) and (yp == 0):
        if moveDirection == "up":
            yp = -1
        elif moveDirection == "down":
            yp = 1
        elif moveDirection == "left":
            xp = -1
        elif moveDirection == "right":
            xp = 1

    if moveDirection is not None:
        spriteDirection = moveDirection

    newx = positionX + xp
    newy = positionY + yp

    if (newx < 0) or (newx > 37) or (newy < 0) or (newy > 12) or (newx < 0):
        pass
    elif (newx == 19) and (newy == 11 or newy == 12):
        pass
    else:
        positionX = newx
        positionY = newy

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


