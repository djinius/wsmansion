screen recollections():

    tag menu

    use game_menu(_("추억하기")):
        vbox:
            style_prefix "recollections"
            grid 3 1:
                vbox:
                    label "도입부"
                    textbutton "도입부" action Replay("splashReplay", locked=False)

                vbox:
                    label "지금의 이야기"
                    grid 2 2:
                        textbutton "1장" action Replay("part1", locked=False)
                        textbutton "2장" action Replay("part2", locked=False)
                        textbutton "트루엔딩" action Replay("trueEnding", locked=False)
                        textbutton "굿 엔딩" action Replay("goodEnding", locked=False)

                vbox:
                    label "과거 이야기"
                    grid 2 3:
                        textbutton "카메라" action Replay("cameraStory", locked=False)
                        textbutton "이야기 짓기" action Replay("makeUpStory", locked=False)
                        textbutton "양복 입기" action Replay("suitFitStory", locked=False)
                        textbutton "모이주기" action Replay("birdFeedStory", locked=False)
                        textbutton "거울" action Replay("mirrorComplete", locked=False)

            vbox:
                label "갤러리"
                text "언젠간 넣겠지."

style recollections_vbox:
    spacing 20

style recollections_hbox:
    spacing 10

style recollections_grid:
    spacing 5

style recollections_button:
    xalign .5

style recollections_label:
    xalign .1