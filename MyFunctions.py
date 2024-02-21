from PIL import Image, ImageDraw


def getImg(path):
    return Image.open(path)  # вернуть изображение


def showImg(img):
    img.show()  # открыть изображение
    return img  # вернуть изображение


def saveImg(img, name):
    img.save(name)  # сохранить изображение
    return img  # вернуть изображение


def printInformation(img):
    print(img.format)  # вывести формат
    print(img.mode)  # вывести мод(RGBA, RGB ...)
    print(img.size)  # вывести размер
    print(img.filename)  # вывести имя
    print(img.histogram())  # вывести истограмму
    return img  # вернуть изображение


def cropImg(img, x1, y1, x2, y2):
    return img.crop((x1, y1, x2, y2))  # вернуть кусок изображения


def rotateImg(img, angle):
    return img.rotate(angle)  # вернуть повернутое изображение


def resizeImg(img, width, height):
    return img.resize((width, height))  # вернуть измененное изображение


def createImg(mode, width, height, color):
    return Image.new(mode, (width, height), color)  # вернуть новое изображение


def drawSquare(img, x1, y1, x2, y2, color):
    ImageDraw.Draw(img).rectangle((x1, y1, x2, y2), fill=color)  # нарисовать квадрат на изображении
    return img  # вернуть изображение
