init -1 python:
    # 화면 흔들기 클래스
    class Shaker(object):
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }

        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child

        def __call__(self, t, sizes):
            # Float to integer… turns floating point numbers to
            # integers.
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor

            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move, time, child, add_sizes=True, **properties)

    Shake = renpy.curry(_Shake)


define whiteNoise = ImageDissolve("gui/transitions/whitenoise.png", .5)
define whiteNoiseSlow = ImageDissolve("gui/transitions/whitenoise.png", 5.)
define fadeoutin = Fade(.5, .0, .5, color="#000")

transform bgblur(radius=1.5):
    blur radius

transform timedblur(radius1=1.5, radius2=1., duration=.5):
    blur radius1
    linear duration blur radius2

transform text5Seconds:
    alpha .0
    easein .5 alpha 1.
    pause 5.
    easein .5 alpha .0

label effectsExample:
    scene black

    scene garden
    show 엘리:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with dissolve

    엘리 "show ... with dissolve"

    hide 엘리 with dissolve
    엘리 "hide 엘리 with dissolve"

    scene living
    show 엘리:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with fade
    엘리 "show ... with fade"

    scene home
    show 엘리:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with whiteNoise
    엘리 "show ... with whiteNoise"

    scene living
    show 엘리:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with pixellate
    엘리 "show ... with pixellate"

    scene bedroom
    show 엘리:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with wipeleft
    엘리 "show ... with wipeleft"

    scene study2
    show 엘리:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with slideleft
    엘리 "show ... with slideleft"

    scene study1
    show 엘리:
        pos (.5, .05) anchor (.5, .0)
        zoom .5
    with blinds
    엘리 "show ... with blinds"

    엘리 "with Shake" with Shake((0, 0, 0, 0), .5, dist=20)

    엘리 "더 많은 효과는 {a=https://www.renpy.org/doc/html/transitions.html}{color=#FF0}여기{/color}{/a}를 참고하세요."

    scene black with irisin
    엘리 "그럼 irisin과 함께 안녕~"

    return
