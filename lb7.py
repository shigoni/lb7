import requests
from PIL import Image, ImageFilter
import os
from io import BytesIO

photo = requests.get(
    "https://gas-kvas.com/grafic/uploads/posts/2023-09/1695802650_gas-kvas-com-p-kartinki-kot-7.jpg"
)

photo_num_3 = [
    "https://gas-kvas.com/grafic/uploads/posts/2023-09/1695802650_gas-kvas-com-p-kartinki-kot-7.jpg",
    "https://proprikol.ru/wp-content/uploads/2020/08/krasivye-kartinki-kotov-20.jpg",
    "https://gas-kvas.com/grafic/uploads/posts/2023-09/1695931383_gas-kvas-com-p-kartinki-s-kotami-9.jpg",
    "https://mykaleidoscope.ru/x/uploads/posts/2022-10/1666152147_2-mykaleidoscope-ru-p-sereznii-kot-krasivo-3.jpg",
    "https://famt.ru/wp-content/uploads/2019/05/sonnik-govoryaschiy-kot.jpg",
]

watermark = requests.get(
    "https://pluspng.com/img-png/lines-png-lines-png-photos-1280.png"
)

if not os.path.exists("filter"):
    os.makedirs("filter")


def number_1():
    with open(file="cat.jpg", mode="wb") as file:
        file.write(photo.content)
        img = Image.open("cat.jpg")
        img.show()
        print("Размер: ", img.size)
        print("Формат: ", img.format)
        print("Цветовая модель: ", img.mode)


def number_2():
    with open(file="cat.jpg", mode="wb") as file:
        file.write(photo.content)
        img = Image.open("cat.jpg")
        width, height = img.size
        width_new = width // 3
        height_new = height // 3
        img_resize = img.resize((width_new, height_new))
        img_resize.save("resize_cat.jpg")
        img_mirror_horizont = img.transpose(Image.FLIP_LEFT_RIGHT)
        img_mirror_horizont.save("horizont_cat.jpg")
        img_mirror_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)
        img_mirror_vertical.save("vertical_cat.jpg")


def number_3():
    for i, url in enumerate(photo_num_3):
        i += 1
        photo_cat = requests.get(url)
        img = Image.open(BytesIO(photo_cat.content))
        img_filter = img.filter(ImageFilter.FIND_EDGES)
        img_filter.save(f"filter/filter_cat_{i}.jpg")


def number_4():
    img = Image.open(BytesIO(photo.content))
    img_width, img_height = img.size

    img_watermark = Image.open(BytesIO(watermark.content))
    img_watermark = img_watermark.resize((img_width, img_height))

    img = Image.alpha_composite(img.convert("RGBA"), img_watermark)
    img.show()


while True:
    number = int(input("Введите номер задания: "))

    if number == 1:
        number_1()
    elif number == 2:
        number_2()
    elif number == 3:
        number_3()
    elif number == 4:
        number_4()
    else:
        print("Такого задания нет")
