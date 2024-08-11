"""renpy
init -1 python:
"""

galleryNames = [
    ("alwaysUnlocked", "gui/recollections/g0.png", "gui/recollections/sample0/g0.png"),
    ("sample1", "gui/recollections/g1.png", "firstEvent"),
    ("sample2", "gui/recollections/g2.png", "images/gallery/sample2/s0.png", "images/gallery/sample2/s1.png"),
    ("sample3", "gui/recollections/g3.png", "images/gallery/sample3/s0.png")]

g = Gallery()

def initGallery():
    global g

    g.locked_button = "gui/recollections/insensitive.png"
    g.navigation = False
    g.slideshow_delay = 2.

    for (n, il) in enumerate(galleryNames):
        g.button(il[0])

        for galleryImages in il[2:]:
            g.unlock_image(galleryImages)

        if n == 0:
            g.condition("False")

initGallery()
