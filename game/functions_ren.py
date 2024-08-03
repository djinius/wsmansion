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

    return quick_menu and (persistent.showQuickMenu > 0) and (renpy.get_screen("exploreMap") is None) and (renpy.get_screen("exploreFound") is None) and (renpy.get_screen("cameraMinigame") is None) and (renpy.get_screen("mirrorMiniGame") is None)

class quickShowHelper(renpy.Displayable):
    def __init__(self, **kwargs):
        super(quickShowHelper, self).__init__(**kwargs)

    def render(self, width, height, st, at):
        # Get the size of the child.
        # self.width, self.height = child_render.get_size()
        # Create the render we will return.
        render = renpy.Render(0, 0)
        # Return the render.
        return render

    def event(self, ev, x, y, st):
        cs = renpy.get_screen("quick_menu")

        if cs is None:
            return

        aval = cs.scope["autoHide"]
        if ev.type == pygame.MOUSEMOTION:
            (xp, yp) = pygame.mouse.get_pos()

            # 마우스가 퀵메뉴 위치에 올라와 있음
            if (xp >= 1380) and (yp >= 1020):
                if aval == 0:
                    cs.scope["autoHide"] = 1
                    renpy.restart_interaction()
                elif aval==3:
                    cs.scope["autoHide"] = 2
                    renpy.restart_interaction()
            # 마우스가 퀵메뉴 위치에서 떨어져 있음
            else:
                if aval == 2:
                    cs.scope["autoHide"] = 3
                    renpy.restart_interaction()
