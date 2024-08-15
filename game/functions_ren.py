"""renpy
init python:
"""

# 메뉴 호출시 나타나는 함수
def menu(items, **add_input):
    """Overwrites the default menu handler, thus allowing us to log the
    choice made by the player.
    The default menu handler is set to renpy.display_menu(), as seen in
    renpy/defaultstore.py.
    Implementation of this is based on delta's readback module."""
    rv = renpy.display_menu(items, **add_input)

    hiEntry = {}

    for item_text, choice_obj in items:
        if rv == choice_obj.value:
            hiEntry[item_text] = True
        else:
            hiEntry[item_text] = False
            
    addMenuHistory(hiEntry)

    return rv    

def addMenuHistory(items):
    # 선택지를 히스토리 항목에 추가
    history = renpy.store._history_list # type: ignore

    h = renpy.character.HistoryEntry()
    h.kind = 'menu'
    h.menuItems = items

    if renpy.game.context().rollback:
        h.rollback_identifier = renpy.game.log.current.identifier # type: ignore
    else:
        h.rollback_identifier = None # type: ignore

    history.append(h)

    while len(history) > renpy.config.history_length:
        history.pop(0)

    return

def addPartHistory(partText):
    # 선택지를 히스토리 항목에 추가
    history = renpy.store._history_list # type: ignore

    h = renpy.character.HistoryEntry()
    h.kind = 'part'
    h.partText = partText

    if renpy.game.context().rollback:
        h.rollback_identifier = renpy.game.log.current.identifier # type: ignore
    else:
        h.rollback_identifier = None # type: ignore

    history.append(h)

    while len(history) > renpy.config.history_length:
        history.pop(0)

    return

def addFoundHistory(foundText, foundImage):
    # 선택지를 히스토리 항목에 추가
    history = renpy.store._history_list # type: ignore

    h = renpy.character.HistoryEntry()
    h.kind = 'found'
    h.foundText = foundText
    h.foundImage = foundImage

    if renpy.game.context().rollback:
        h.rollback_identifier = renpy.game.log.current.identifier # type: ignore
    else:
        h.rollback_identifier = None # type: ignore

    history.append(h)

    while len(history) > renpy.config.history_length:
        history.pop(0)

    return

# 퀵메뉴 관련 함수들
def isQuickVisible():
    global quick_menu

    return quick_menu and (persistent.showQuickMenu > 0) and (renpy.get_screen("puzzle") is None)

def isQuickExploring():
    return (renpy.get_screen("exploreRooms") is not None) or (renpy.get_screen("exploreFound") is not None) 

class quickShowHelper(renpy.Displayable):
    def __init__(self, w = 540, h = 60, **kwargs):
        super(quickShowHelper, self).__init__(**kwargs)
        self.w = 1920 - w
        self.h = 1080 - h

    def render(self, width, height, st, at):
        # Get the size of the child.
        # self.width, self.height = child_render.get_size()
        # Create the render we will return.
        render = renpy.Render(0, 0)
        # Return the render.
        return render

    def event(self, ev, x, y, st):
        global quickMenuAutoHide

        if ev.type == pygame.MOUSEMOTION:
            (xp, yp) = pygame.mouse.get_pos()
            (xs, ys) = renpy.get_physical_size()
            xr = xp / xs
            yr = yp / ys

            # 마우스가 퀵메뉴 위치에 올라와 있음
            if (xr >= (self.w / 1920)) and (yr >= (self.h / 1080)):
                if quickMenuAutoHide == 0:
                    quickMenuAutoHide = 1
                    renpy.restart_interaction()
                elif quickMenuAutoHide == 3:
                    quickMenuAutoHide = 4
                    renpy.restart_interaction()
            # 마우스가 퀵메뉴 위치에서 떨어져 있음
            else:
                # 마우스가 다시 돌아옴
                if quickMenuAutoHide == 2:
                    quickMenuAutoHide = 3
                    renpy.restart_interaction()


# 책과 1쪽, 2쪽 찾은 개수
def bookPartCount():
    global myInventory

    bookPart = 0
    if "tornbook" in myInventory:
        bookPart += 1
    if "page1" in myInventory:
        bookPart += 1
    if "page2" in myInventory:
        bookPart += 1

    return bookPart

# 거울 미니게임 파편 위치
def getMirrorFragmentPosition():
    xp = renpy.random.random()
    if xp < .5:
        xp = xp * .4 + .1
    else:
        xp = (xp - .5) * .4 + .7

    return (xp, renpy.random.random())