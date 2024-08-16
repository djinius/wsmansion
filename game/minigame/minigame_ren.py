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
    global explorePhase
    global isMirrorFound
    global isBedroomUnlocked

    print (positionX, positionY)

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

    if (newx < 0) or (newx >= 34) or (newy < 0) or (newy >= 22):
        pass
    elif (isBedroomUnlocked is False) and (((newx >= 10) and (newx <= 13) and (newy >= 10) and (newy <= 15)) or ((newx == 9) and (newy >= 13) and (newy <= 15))):
        # 침실이 잠겨 있음
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
    return (x * 72 + 36, y * 72 + 18)

def getMapOffset():
    global positionX
    global positionY
    
    xo = (1920 - 2448) / 2
    yo = (1080 - 1584) / 2

    x = positionX
    y = positionY

    xd = 960 / 72
    yd = 540 / 72

    xol = x * 72
    xor = 2448 - (x * 72)
    yol = y * 72
    yor = 1584 - (y * 72)

    if xol < 960:
        xo = 0
    elif xor < 960:
        xo = -(2448 - 1920)
    else:
        ## 주인공을 중앙에 배치함
        xo = -(xol - 960)

    if yol < 540:
        yo = 0
    elif yor < 540:
        yo = -(1584 - 1080)
    else:
        ## 주인공을 중앙에 배치함
        yo = -(yol - 540)

    return (xo, yo)

def objectFound(object):
    objectRemove(object)
    myInventory.append(object)

def objectRemove(object):
    objects.remove(object)

def isFragmentSensitive(fragNo):
    global explorePhase
    global myInventory
    global mirrorFragMatchs

    return (explorePhase == 2) and ("frag" + str(fragNo) not in myInventory) and (mirrorFragMatches[fragNo] is False)

def fragmentDropped(drags, drop):
    global mirrorFragMatchs
    global isMirrorComplete

    if drop:
        n1 = drags[0].drag_name
        n2 = drop.drag_name

        if n1 == n2:
            mirrorFragMatches[n1] = True
            myInventory.remove("frag" + str(n1))
            renpy.restart_interaction()

            if False in mirrorFragMatches:
                return
            else:
                isMirrorComplete = True
                return "complete"

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
        leftCenterX = 1102
        leftCenterY = 580
        rightCenterX = 1357
        rightCenterY = 584

        cs = renpy.current_screen()

        if ev.type == pygame.MOUSEMOTION:
            (xp, yp) = pygame.mouse.get_pos()
            (xs, ys) = renpy.get_physical_size()
            xr = xp / xs * 1920
            yr = yp / ys * 1080

            if cs.scope["rotating"] is None:
                distanceLeft = math.sqrt((xr - leftCenterX) * (xr - leftCenterX) + (yr - leftCenterY) * (yr - leftCenterY))
                distanceRight = math.sqrt((xr - rightCenterX) * (xr - rightCenterX) + (yr - rightCenterY) * (yr - rightCenterY))
                print (xp, yp, xr, yr, distanceLeft, distanceRight )
                if (distanceLeft > (10)) and (distanceLeft < (30)):
                    cs.scope["toRotate"] = "Left"
                    renpy.restart_interaction()
                elif (distanceRight > (10)) and (distanceRight < (30)):
                    cs.scope["toRotate"] = "Right"
                    renpy.restart_interaction()
                else:
                    cs.scope["toRotate"] = None
                    renpy.restart_interaction()
            elif cs.scope["rotating"] == "Left":
                newAngle = math.atan2(xr - leftCenterX, yr - leftCenterY)
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
                newAngle = math.atan2(xr - rightCenterX, yr - rightCenterY)
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
                self.beginAngle = math.atan2(self.beginx - leftCenterX, self.beginy - leftCenterY)
            elif cs.scope["rotating"] == "Right":
                self.beginx = xp
                self.beginy = yp
                self.firstAngle = cs.scope["rotateRight"]
                self.beginAngle = math.atan2(self.beginx - rightCenterX, self.beginy - rightCenterY)

            renpy.restart_interaction()
            
        elif ev.type == pygame.MOUSEBUTTONUP:
            cs.scope["rotating"] = None
            renpy.restart_interaction()

        return None

