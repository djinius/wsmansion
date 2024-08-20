"""renpy
init -1 python:
"""

mr = MusicRoom(fadeout = 1.)

def initMusicRoom():
    global mr
    global musicRoomResource

    for f in musicRoomResource:
        mr.add(f)

def getMusicURL():
    global musicRoomResource

    f = renpy.music.get_playing()

    if f is None:
        return ""
    else:
        return musicRoomResource[f][0]

def getMusicTitle():
    global musicRoomResource

    f = renpy.music.get_playing()

    if f is None:
        return ""
    else:
        return musicRoomResource[f][1]

def getMusicAuthor():
    global musicRoomResource

    f = renpy.music.get_playing()

    if f is None:
        return ""
    else:
        return musicRoomResource[f][2]

def getMusicPosition(st, at):
    cur = renpy.music.get_pos()
    ret = ""

    if cur is None:
        ret = "0:00"
    else:
        cur = int(cur)
        ret = "%1d:%02d" % (cur // 60, cur % 60)

    return Text(ret, font="repet___.ttf", size=20, color="#FFDF01"), .1

def getMusicDuration(st, at):
    cur = renpy.music.get_duration()
    ret = ""

    if cur is None:
        ret = ""
    else:
        cur = int(cur)
        ret = "%1d:%02d" % (cur // 60, cur % 60)

    return Text(ret, font="repet___.ttf", size=20, color="#FFDF01"), .1

initMusicRoom()
