# 이 파일에 게임 스크립트를 입력합니다.

default persistent.replayPrologue = True

# 여기에서부터 게임이 시작합니다.
label start:

    call part1

label explorePart1:
    $ moveDirection = None
    call screen exploreMap

    if _return == "Finished!!":
        jump continueStory

    $ foundObject = _return
    $ objectFound(foundObject)
    call screen exploreFound(foundObject)

    show screen exploreBase
    call expression foundObject + "Found"

    if objects:
        jump explorePart1

label continueStory:
    hide screen explore
    call part2

    "엔딩"

    return
