define nanseolSprite = "images/minigame/samplesprite.png"

image nanseol walkdown00 = im.Crop(nanseolSprite, (100 *  0, 100 *  0, 100, 100))
image nanseol walkdown01 = im.Crop(nanseolSprite, (100 *  1, 100 *  0, 100, 100))
image nanseol walkdown02 = im.Crop(nanseolSprite, (100 *  2, 100 *  0, 100, 100))
image nanseol walk down = Animation(
    "nanseol walkdown00", .25,
    "nanseol walkdown01", .25,
    "nanseol walkdown02", .25,
    "nanseol walkdown01", .25)

image nanseol walkleft00 = im.Crop(nanseolSprite, (100 *  0, 100 *  1, 100, 100))
image nanseol walkleft01 = im.Crop(nanseolSprite, (100 *  1, 100 *  1, 100, 100))
image nanseol walkleft02 = im.Crop(nanseolSprite, (100 *  2, 100 *  1, 100, 100))
image nanseol walk left = Animation(
    "nanseol walkleft00", .25,
    "nanseol walkleft01", .25,
    "nanseol walkleft02", .25,
    "nanseol walkleft01", .25)

image nanseol walkright00 = im.Crop(nanseolSprite, (100 *  0, 100 *  2, 100, 100))
image nanseol walkright01 = im.Crop(nanseolSprite, (100 *  1, 100 *  2, 100, 100))
image nanseol walkright02 = im.Crop(nanseolSprite, (100 *  2, 100 *  2, 100, 100))
image nanseol walk right = Animation(
    "nanseol walkright00", .25,
    "nanseol walkright01", .25,
    "nanseol walkright02", .25,
    "nanseol walkright01", .25)

image nanseol walkup00 = im.Crop(nanseolSprite, (100 *  0, 100 *  3, 100, 100))
image nanseol walkup01 = im.Crop(nanseolSprite, (100 *  1, 100 *  3, 100, 100))
image nanseol walkup02 = im.Crop(nanseolSprite, (100 *  2, 100 *  3, 100, 100))
image nanseol walk up = Animation(
    "nanseol walkup00", .25,
    "nanseol walkup01", .25,
    "nanseol walkup02", .25,
    "nanseol walkup01", .25)

image map01 = "images/minigame/map01.jpg"