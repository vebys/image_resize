import os
from PIL import Image


def resize(x_new, scale=100):
    """
    :param x_new: 新尺寸宽度
    :param scale: 缩放比例1-100
    :return:
    """
    files = os.listdir('input/')
    for i in files:
        img = Image.open(f"input/{i}")
        # f = i.replace('.jpg', '')
        # 裁剪
        x, y = img.size
        y_new = int(y / (x / x_new))
        # print(x, y, x_new, y_new)
        img = img.resize((x_new, y_new), Image.ANTIALIAS)
        # 缩小
        img.save(f'output/{i}', quality=scale)


if __name__ == "__main__":
    resize(200)
