screen recollections():

    tag menu

    default startPlaying = False

    on "replace" action Stop("music")
    on "replaced" action Play("music", audio.titleMusic)

    use game_menu(_("추억하기")):

        hbox:
            style_prefix "recollections"
            xfill True

            vbox:
                label "다시보기"

                grid 2 6:
                    textbutton "도입부" action Replay("splashReplay")
                    null

                    textbutton "1장" action Replay("part1")
                    textbutton "2장" action Replay("part2")

                    textbutton "카메라" action Replay("cameraStory")
                    textbutton "이야기 짓기" action Replay("makeUpStory")
                    textbutton "양복 입기" action Replay("suitFitStory")
                    textbutton "모이주기" action Replay("birdFeedStory")
                    textbutton "자물쇠" action Replay("lockStory")
                    textbutton "거울" action Replay("mirrorComplete")

                    textbutton "트루엔딩" action Replay("trueEnding")
                    textbutton "굿 엔딩" action Replay("goodEnding")

            vbox:
                vbox:
                    label "화랑"
                    grid 2 2:
                        for (n, il) in enumerate(galleryNames):
                            add g.make_button(il[0], unlocked=il[1], idle_border="gui/recollections/g" + str(n) + "_idle.png", hover_border="gui/recollections/g" + str(n) + "_hover.png", xalign=.5, yalign=.5)

                vbox:
                    style_prefix "musicroom"
                    label "음악실"

                    frame:
                        background Frame("gui/musicroomframe.png", 50, 46, 77, 37)
                        xsize 700
                        padding (50, 50)

                        imagemap:
                            align (.5, .5)

                            if startPlaying and renpy.music.is_playing():
                                auto "gui/recollections/playing_%s.png"
                            else:
                                auto "gui/recollections/stopped_%s.png"

                            for (n, f) in enumerate(musicRoomResource):
                                hotspot (15 + (n % 5) * 60, 20 + (n // 5) * 50, 60, 50):
                                    action [SetScreenVariable("startPlaying", True),
                                            mr.Play(f)]
                                    selected (startPlaying and renpy.music.get_playing() == f)

                            hotbar (14, 224, 572, 17) value AudioPositionValue(update_interval=.5)
                            hotspot (45 + 60 * 0, 245, 60, 60) action [SetScreenVariable("startPlaying", True), mr.Previous()] selected False
                            hotspot (45 + 60 * 1, 245, 60, 60) action [SetScreenVariable("startPlaying", True), mr.Play()] selected (startPlaying and renpy.music.is_playing())
                            hotspot (45 + 60 * 2, 245, 60, 60) action mr.TogglePause()
                            hotspot (45 + 60 * 3, 245, 60, 60) action mr.Stop()
                            hotspot (45 + 60 * 4, 245, 60, 60) action [SetScreenVariable("startPlaying", True), mr.Next()] selected False
                            hotspot (45 + 60 * 5, 245, 60, 60) action mr.ToggleLoop()
                            hotspot (45 + 60 * 6, 245, 60, 60) action mr.ToggleSingleTrack()
                            hotspot (45 + 60 * 7, 245, 60, 60) action mr.ToggleShuffle()
                            hotspot (45 + 60 * 8, 245, 60, 60):
                                action OpenURL(getMusicURL())
                                sensitive (startPlaying and renpy.music.is_playing())

                        if startPlaying and renpy.music.get_playing():
                            text getMusicTitle() pos (20, 205) anchor (.0, 1.)
                            text getMusicAuthor() pos (584, 205) anchor (1., 1.) style "musicroom_author_text"
                            add DynamicDisplayable(getMusicPosition) pos (20, 230) anchor (.0, 1.)
                            add DynamicDisplayable(getMusicDuration) pos (584, 230) anchor (1., 1.)
                        else:
                            text "\n\n" pos (20, 225) anchor (.0, 1.)
                            text "" pos (584, 225) anchor (1., 1.) style "musicroom_author_text"

    # textbutton "effectsExample" action Replay("effectsExample", locked=False) align (1., 1.)

style recollections_vbox:
    spacing 20

style recollections_hbox:
    spacing 10

style recollections_grid:
    spacing 5

style recollections_button:
    xysize (180, 71)
    xalign .5
    idle_background "gui/recollections/replay_idle.png"
    hover_background "gui/recollections/replay_hover.png"
    insensitive_background "gui/recollections/replay_insensitive.png"

style recollections_button_text is button_text:
    size 25
    align (.5, .5)
    idle_color "#001040"
    hover_color "#2040FF"
    insensitive_color "#0000"

style recollections_label:
    xalign .5

style musicroom_button:
    xysize (650, 45)
    xalign .5
    idle_background Frame("gui/recollections/replay_idle.png", 30, 5)
    hover_background Frame("gui/recollections/replay_hover.png", 30, 5)
    insensitive_background Frame("gui/recollections/replay_insensitive.png", 30, 5)

style musicroom_button_text is recollection_button_text:
    size 20
    xalign .5

style musicroom_label is recollections_label

style musicroom_text:
    font "NEXON Lv2 Gothic Medium.ttf"
    color "#FFDF01"
    size 20

style musicroom_author_text:
    font "NEXON Lv2 Gothic Medium.ttf"
    color "#FFDF01"
    size 16

screen _gallery(locked, displayables, index, count, gallery, **properties):

    if locked:
        add "#000"
        text _("Image [index] of [count] locked.") align (0.5, 0.5)
    else:
        for d in displayables:
            viewport id "vp":
                draggable True
                mousewheel True
                xinitial 0. yinitial 0.

                add d

    if gallery.slideshow:
        timer gallery.slideshow_delay action Return("next") repeat True

    key "game_menu" action gallery.Return()

    if gallery.navigation:
        use gallery_navigation(gallery=gallery)

screen gallery_navigation(gallery):
    hbox:
        spacing 20

        style_group "gallery"
        align (.98, .98)

        textbutton _("prev") action gallery.Previous(unlocked=gallery.unlocked_advance)
        textbutton _("next") action gallery.Next(unlocked=gallery.unlocked_advance)
        textbutton _("slideshow") action gallery.ToggleSlideshow()
        textbutton _("return") action gallery.Return()

