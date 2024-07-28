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

