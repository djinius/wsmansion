# 이 파일에 게임 스크립트를 입력합니다.
init python:
    import copy

default persistent.replayPrologue = True
default persistent.skyBackground = False
default persistent.myName = None

# 여기에서부터 게임이 시작합니다.
label start:
    $ splashPhase = False

    $ addPartHistory("파트 1.")
    call part1
    scene black with dissolve

label explorePart1Prepare:
    # 탐색 1에서 찾아야 할 물품들을 리스트에 복사
    $ addPartHistory("탐색 1.")
    $ objects = copy.deepcopy(objectsPart1)
    $ explorePhase = 1

label explorePart1:

    $ renpy.choice_for_skipping()
    $ moveDirection = None
    $ config.mouse_displayable.add("pressed_default", "gui/cursors/default.png", 1, 63)
    call screen exploreRooms
    $ renpy.choice_for_skipping()
    $ config.mouse_displayable.add("pressed_default", "pressed_say", 1, 63)

    # 엘리 클릭
    if _return == "elly!!":
        call ellyPart1

        if _return == "Finished!!":
            jump storyPart2

    else:
        $ foundObject = _return
        call expression foundObject + "Found"

    if objects:
        jump explorePart1

label storyPart2:
    hide screen explore

    $ addPartHistory("파트 2.")
    call part2

label explorePart2Prepare:
    # 탐색 1에서 찾아야 할 물품들을 리스트에 복사
    $ addPartHistory("탐색 2.")
    $ objects.extend(objectsPart2)
    $ explorePhase = 2

label explorePart2:

    $ renpy.choice_for_skipping()
    $ moveDirection = None
    $ config.mouse_displayable.add("pressed_default", "gui/cursors/default.png", 1, 63)
    call screen exploreRooms
    $ renpy.choice_for_skipping()
    $ config.mouse_displayable.add("pressed_default", "pressed_say", 1, 63)

    if _return == "elly!!":
        call ellyPart2

    else:
        $ foundObject = _return
        call expression foundObject + "Found"

    if isMirrorComplete:
        jump storyEnding

    if objects:
        jump explorePart2

label storyEnding:

    if 'completeBook' in myInventory:
        call goodEnding
    else:
        call trueEnding

    return
