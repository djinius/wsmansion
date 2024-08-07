screen replay():

    tag menu

    use game_menu(_("다시보기")):
        hbox:
            vbox:
                label "도입부"
                textbutton "도입부" action Replay("splashReplay", locked=False)
                null height(10)

                label "1부"
                textbutton "1장" action Replay("part1", locked=False)

                null height(10)

                label "2부"
                textbutton "2장" action Replay("part2", locked=False)

                label "과거 이야기"
                textbutton "카메라" action Replay("cameraStory", locked=False)
                textbutton "이야기 짓기" action Replay("makeUpStory", locked=False)
                textbutton "양복 입기" action Replay("suitFitStory", locked=False)
                textbutton "모이주기" action Replay("birdFeedStory", locked=False)
                textbutton "거울" action Replay("mirrorComplete", locked=False)

                null height(10)

                label "엔딩"
                textbutton "트루엔딩" action Replay("trueEnding", locked=False)
                textbutton "굿 엔딩" action Replay("goodEnding", locked=False)
