import MyFunctions

image = MyFunctions.getImg('Images/Monkey.jpg')  # получить изображение
MyFunctions.saveImg(image, 'Images/Monkey.png')  # сохранить изображение в формате png

MyFunctions.showImg(image)  # Открыть изображение
MyFunctions.printInformation(image)  # вывести информацию об изображении

MyFunctions.showImg(  # Открыть изображение
    MyFunctions.saveImg(  # сохранить изображение
        MyFunctions.cropImg(image, 50, 50, 100, 100),  # вырезать кусок из изображения
        'Images/cropped_Monkey.jpg')  # путь для сохранения
)

MyFunctions.showImg(  # Открыть изображение
    MyFunctions.saveImg(  # сохранить изображение
        MyFunctions.rotateImg(image, 180),  # повернуть изображение
        'Images/rotated_Monkey.jpg')  # путь для сохранения
)

MyFunctions.showImg(  # Открыть изображение
    MyFunctions.saveImg(  # сохранить изображение
        MyFunctions.resizeImg(image, 900, 300),  # изменить размер изображения
        'Images/resized_Monkey.jpg')  # путь для сохранения
)

MyFunctions.showImg(  # Открыть изображение
    MyFunctions.saveImg(  # сохранить изображение
        MyFunctions.drawSquare(  # нарисовать квадрат
            MyFunctions.createImg('RGB', 200, 200, 'black')  # создать изображение
            , 50, 50, 100, 100, 'pink'),  # размер и цвет квадрата
        'Images/painting.jpg')  # путь для сохранения
)
