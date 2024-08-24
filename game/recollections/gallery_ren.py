"""renpy
init -1 python:
"""

galleryNames = [
    ("title", "gui/recollections/g0.png", "title_orig", "title_darken"),
    ("egc1", "gui/recollections/g1.png", "firstEvent"),
    ("ecg2", "gui/recollections/g2.png", "secondEvent"),
    ("ecg3", "gui/recollections/g3.png", "thirdEvent")]

g = Gallery()

def initGallery():
    global g

    g.locked_button = "gui/recollections/insensitive.png"
    g.navigation = False
    g.slideshow_delay = 2.

    for (n, il) in enumerate(galleryNames):
        g.button(il[0])

        for galleryImages in il[2:]:
            if n == 0:
                g.image(galleryImages)
            else:
                g.unlock_image(galleryImages)

initGallery()
