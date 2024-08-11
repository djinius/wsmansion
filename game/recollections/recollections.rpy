screen recollections():

    tag menu

    use game_menu(_("추억하기")):
        grid 3 1:
            style_prefix "recollections"
            xfill True

            grid 1 3:

                vbox:
                    label "다시보기"

                    grid 2 6:
                        textbutton "도입부" action Replay("splashReplay", locked=False)
                        null

                        textbutton "1장" action Replay("part1", locked=False)
                        textbutton "2장" action Replay("part2", locked=False)

                        textbutton "카메라" action Replay("cameraStory", locked=False)
                        textbutton "이야기 짓기" action Replay("makeUpStory", locked=False)
                        textbutton "양복 입기" action Replay("suitFitStory", locked=False)
                        textbutton "모이주기" action Replay("birdFeedStory", locked=False)
                        textbutton "거울" action Replay("mirrorComplete", locked=False)
                        null

                        textbutton "트루엔딩" action Replay("trueEnding", locked=False)
                        textbutton "굿 엔딩" action Replay("goodEnding", locked=False)

            vbox:
                label "화랑"
                grid 1 4:
                    for (n, il) in enumerate(galleryNames):
                        add g.make_button(il[0], unlocked=il[1], idle_border="gui/gallery/g" + str(n) + "_idle.png", hover_border="gui/gallery/g" + str(n) + "_hover.png", xalign=.5, yalign=.5)

            vbox:
                label "음악실"
                textbutton "아싸라비야" action NullAction()
                textbutton "콜롬비아" action NullAction()
                textbutton "호이호이" action NullAction()

style recollections_vbox:
    spacing 20

style recollections_hbox:
    spacing 10

style recollections_grid:
    spacing 5

style recollections_button:
    xalign .5

style recollections_label:
    xalign .5

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

