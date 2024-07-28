"""renpy
init python:
"""

# 매 게임마다 초기화하는 코드를 여기에 넣기
renpy.music.register_channel("sound2", "sfx")
renpy.music.register_channel("sound3", "sfx")

# customizing keymap
config.keymap['self_voicing'].clear()
config.keymap['screenshot'] = ['K_F12']
config.keymap['rollback'].clear()
config.keymap['rollforward'].clear()
# mousedown_4, mousedown_5

config.overlay_screens.append("quick_menu")
