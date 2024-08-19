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

initMusicRoom()
