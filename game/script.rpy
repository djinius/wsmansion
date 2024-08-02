# 이 파일에 게임 스크립트를 입력합니다.
init python:
    import copy

default persistent.replayPrologue = True

# 여기에서부터 게임이 시작합니다.
label start:

    $ addPartHistory("파트 1.")
    call part1
    scene black with dissolve

label explorePart1Prepare:
    # 탐색 1에서 찾아야 할 물품들을 리스트에 복사
    $ addPartHistory("탐색 1.")
    $ objects = copy.deepcopy(objectsPart1)
    $ explorePhase = 1

label explorePart1:

    $ moveDirection = None
    $ config.mouse_displayable.add("pressed_default", "gui/cursors/default.png", 1, 63)
    call screen exploreMap
    $ config.mouse_displayable.add("pressed_default", "pressed_say", 1, 63)

    if _return == "Finished!!":
        jump storyPart2

    $ foundObject = _return
    $ objectFound(foundObject)
    call screen exploreFound(foundObject)

    show screen exploreBase
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
    $ objects = copy.deepcopy(objectsPart2)
    if "gloves" in myInventory:
        $ objects.pop(0)
    $ explorePhase = 2

label explorePart2:
    $ moveDirection = None
    $ config.mouse_displayable.add("pressed_default", "gui/cursors/default.png", 1, 63)
    call screen exploreMap
    $ config.mouse_displayable.add("pressed_default", "pressed_say", 1, 63)

    $ foundObject = _return
    if foundObject == "gloves":
        $ objectFound(foundObject)
        call screen exploreFound(foundObject)

    show screen exploreBase
    call expression foundObject + "Found"

    if isMirrorComplete:
        jump storyEnding

    if objects:
        jump explorePart2

label storyEnding:
    menu:
        "엔딩을 갈리는 부분이 명확하게 합의되지 않았기 때문에 일단 선택지로 넣습니다."
        "트루엔딩":
            call trueEnding
        "굿엔딩":
            call goodEnding

    return
