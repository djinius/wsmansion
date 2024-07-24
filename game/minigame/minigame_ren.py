"""renpy
init python:
"""

import pygame
import math

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


## Rotate dials
class rotateHelper(renpy.Displayable):
    def __init__(self, **kwargs):
        super(rotateHelper, self).__init__(**kwargs)
        self.rotating = False
        self.beginx = None
        self.beginy = None
        self.beginAngle = 0
        self.firstAngle = 0

    def render(self, width, height, st, at):
        # Get the size of the child.
        # self.width, self.height = child_render.get_size()
        # Create the render we will return.
        render = renpy.Render(0, 0)
        # Return the render.
        return render

    def event(self, ev, x, y, st):
        cs = renpy.current_screen()

        if ev.type == pygame.MOUSEMOTION:
            (xp, yp) = pygame.mouse.get_pos()

            if cs.scope["rotating"] is None:
                distanceLeft = (xp - 768) * (xp - 768) + (yp - 578) * (yp - 578)
                distanceRight = (xp - 1022) * (xp - 1022) + (yp - 582) * (yp - 582)
                if (distanceLeft > (10 * 10)) and (distanceLeft < (27 * 27)):
                    cs.scope["toRotate"] = "Left"
                    renpy.restart_interaction()
                elif (distanceRight > (10 * 10)) and (distanceRight < (27 * 27)):
                    cs.scope["toRotate"] = "Right"
                    renpy.restart_interaction()
                else:
                    cs.scope["toRotate"] = None
                    renpy.restart_interaction()
            elif cs.scope["rotating"] == "Left":
                newAngle = math.atan2(xp - 768, yp - 578)
                rotatedAngle = self.beginAngle - newAngle
                rotatedAngle = rotatedAngle / math.pi * 180
                newAngle = (self.firstAngle + rotatedAngle) % 360

                if newAngle < 30 or newAngle > 330:
                    cs.scope["rotateLeft"] = 0
                else:
                    cs.scope["rotateLeft"] = newAngle

                newAngle = cs.scope["rotateLeft"]
                if newAngle > 180:
                    blurry = (360 - newAngle) / 36
                else:
                    blurry = newAngle / 36

                cs.scope["blurry"] = blurry

                renpy.restart_interaction()

            elif cs.scope["rotating"] == "Right":
                newAngle = math.atan2(xp - 1022, yp - 582)
                rotatedAngle = self.beginAngle - newAngle
                rotatedAngle = rotatedAngle / math.pi * 180
                newAngle = (self.firstAngle + rotatedAngle) % 360

                if newAngle < 30 or newAngle > 330:
                    cs.scope["rotateRight"] = 0
                else:
                    cs.scope["rotateRight"] = newAngle

                newAngle = cs.scope["rotateRight"]

                if newAngle > 180:
                    saturation = (360 - newAngle) / 180
                else:
                    saturation = newAngle / 180
                saturation = 1 - saturation
                
                cs.scope["saturation"] = saturation

                renpy.restart_interaction()

        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button==1:
            (xp, yp) = pygame.mouse.get_pos()
            cs.scope["rotating"] = cs.scope["toRotate"]

            if cs.scope["rotating"] == "Left":
                self.beginx = xp
                self.beginy = yp
                self.firstAngle = cs.scope["rotateLeft"]
                self.beginAngle = math.atan2(self.beginx - 768, self.beginy - 578)
            elif cs.scope["rotating"] == "Right":
                self.beginx = xp
                self.beginy = yp
                self.firstAngle = cs.scope["rotateRight"]
                self.beginAngle = math.atan2(self.beginx - 1022, self.beginy - 582)

            renpy.restart_interaction()
            
        elif ev.type == pygame.MOUSEBUTTONUP:
            cs.scope["rotating"] = None
            renpy.restart_interaction()

        return None

