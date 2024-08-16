## History 스크린 #################################################################
##
## 지난 대사록을 출력합니다. _history_list 에 저장된 대사 기록을 확인합니다.
##
## https://www.renpy.org/doc/html/history.html

define whoIdleColors = {
    "‘나’": "#4a4f5a",
    "엘리": "#666333",
    "아비게일 F. 엘리엇": "#666333",
    "???": "#666333"}

screen history():

    tag menu

    ## 이 스크린은 내용이 아주 많을 수 있으므로 prediction을 끕니다.
    predict False

    use game_menu(_("대사록"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            button:
                action Confirm("이 지점으로 되돌아가시겠습니까?", RollbackToIdentifier(h.rollback_identifier))
                sensitive (not _in_replay) and (renpy.get_identifier_checkpoints(h.rollback_identifier)) and (h.kind not in ['part', 'found'])
                has frame
                xysize (1., 1.)
                # xfill True yfill True
                idle_background None
                hover_background Solid("#0048")
                insensitive_background None

                ## history_height 이 None일 경우 레이아웃이 틀어지지 않게 합니다.
                has fixed:
                    yfit True

                if h.kind == 'part':
                    text h.partText:
                        align (.5, .5) size 40
                        min_width 1.

                elif h.kind == 'found':
                    add "gui/minigame/" + h.foundImage + "_hover.png":
                        xpos gui.history_name_xpos
                        xanchor gui.history_name_xalign
                        ypos gui.history_name_ypos
                    text h.foundText yalign 1. yoffset -40

                elif h.kind == 'menu':
                    vbox:
                        for mi in h.menuItems.keys():
                            text mi:
                                xalign .5
                                text_align .5
                                if h.menuItems[mi]:
                                    idle_color "#FF4400"
                                    hover_color "#FFCC00"
                                    insensitive_color "#000000"
                                else:
                                    idle_color "#000000"
                                    hover_color "#FFEFEE"
                                    insensitive_color "#000000"

                else:
                    if h.who:
                        text h.who:
                            style "history_name"
                            substitute False

                            ## 화자 Character에 화자 색깔이 지정되어 있으면 불러옵니
                            ## 다.
                            # if "color" in h.who_args:
                            if h.who in whoIdleColors:
                                idle_color whoIdleColors[h.who] #"#666333" # h.who_args["color"]
                                hover_color "#FFFCCC" # h.who_args["color"]
                                insensitive_color whoIdleColors[h.who] #"#666333" # h.who_args["color"]
                            else:
                                idle_color "#88888888" #"#666333" # h.who_args["color"]
                                hover_color "#88888888" # h.who_args["color"]
                                insensitive_color "#88888888" #"#666333" # h.who_args["color"]

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False
                        idle_color "#000000"
                        hover_color "#FFFFFF"
                        insensitive_color "#000000"


        if not _history_list:
            label _("대사가 없습니다.")


## 이것은 대사록 화면에 표시할 수 있는 태그를 결정합니다.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text:
    color "#000000"

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_button:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    font "GowunBatang-Bold.ttf" # FontGroup().add("Danjo-bold-Regular.otf", 0, 127).add("NEXON Lv2 Gothic Medium.ttf", 128, 0xABFF).add("Danjo-bold-Regular.otf", 0xAC00, 0xD7A3).add("NEXON Lv2 Gothic Medium.ttf", 0xD7A4, 0xFFFF)

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    font "GowunBatang-Bold.ttf" # FontGroup().add("Danjo-bold-Regular.otf", 0, 127).add("NEXON Lv2 Gothic Medium.ttf", 128, 0xABFF).add("Danjo-bold-Regular.otf", 0xAC00, 0xD7A3).add("NEXON Lv2 Gothic Medium.ttf", 0xD7A4, 0xFFFF)

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


