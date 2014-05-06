__author__ = 'halfcrazy'

from PIL import Image
import StringIO

#------------------------------------------------------------------------------
# binaryzation


def binary(data):
    data.seek(0)
    img = Image.open(data)
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    return img

#------------------------------------------------------------------------------
# divide the image


def division(img):
    font = []
    for i in range(4):
        x = 6 + i * 13
        y = 3
        font.append(img.crop((x, y, x + 9, y + 13)))
    return font

#------------------------------------------------------------------------------
# note that the image should be a StringIO object


def recognize(img):
    fontMods = []
    for i in range(10):
        fontMods.append((str(i), Image.open('./zimo/%d.jpg' % i)))
    result = ''
    font = division(img)
    for i in font:
        target = i
        points = []
        for mod in fontMods:
            diffs = 0
            for yi in range(13):
                for xi in range(9):
                    if mod[1].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                        diffs += 1
            points.append((diffs, mod[0]))
        points.sort()
        result += points[0][1]
    return result
