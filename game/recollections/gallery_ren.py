"""renpy
init -1 python:
"""

galleryNames = [
    ("alwaysUnlocked", "gui/gallery/g0.png", "gui/gallery/sample0/g0.png"),
    ("sample1", "gui/gallery/g1.png", "images/gallery/sample1/s0.png", "images/gallery/sample1/s1.png", "images/gallery/sample1/s2.png"),
    ("sample2", "gui/gallery/g2.png", "images/gallery/sample2/s0.png", "images/gallery/sample2/s1.png"),
    ("sample3", "gui/gallery/g3.png", "images/gallery/sample3/s0.png")]

g = Gallery()

def initGallery():
    global g

    g.locked_button = "gui/gallery/insensitive.png"
    g.navigation = True
    g.slideshow_delay = 2.

    for (n, il) in enumerate(galleryNames):
        g.button(il[0])

        for galleryImages in il[2:]:
            g.image(galleryImages)

        if n == 0:
            g.condition("False")

initGallery()
