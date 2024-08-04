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
                textbutton "찢어진 책" action Replay("tornbookStory", locked=False)
                textbutton "타로 스케치북" action Replay("sketchookStory", locked=False)
                textbutton "카메라" action Replay("cameraStory", locked=False)

                null height(10)

                label "2부"
                textbutton "2장" action Replay("part2", locked=False)
                textbutton "찢어진 책 완성" action Replay("page2Story", locked=False)
                textbutton "귀걸이" action Replay("earringStory", locked=False)
                textbutton "거울" action Replay("mirrorComplete", locked=False)

                null height(10)

                label "엔딩"
                textbutton "트루엔딩" action Replay("trueEnding", locked=False)
                textbutton "굿 엔딩" action Replay("goodEnding", locked=False)
