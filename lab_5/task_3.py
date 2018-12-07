import numpy as np
from PIL import Image, ImageEnhance
from matplotlib import image, pyplot as plot


def show_image(img):
    plot.imshow(img)
    plot.show()


def split_into_channels(img):
    red, blue, green = img.copy(), img.copy(), img.copy()
    red[:, :, 1], red[:, :, 2] = 0, 0
    plot.imshow(red)
    plot.show()
    blue[:, :, 0], blue[:, :, 1] = 0, 0
    plot.imshow(blue)
    plot.show()
    green[:, :, 0], green[:, :, 2] = 0, 0
    plot.imshow(green)
    plot.show()


def contrast(img):
    plot.imshow(ImageEnhance.Contrast(img).enhance(0.1))
    plot.show()
    plot.imshow(ImageEnhance.Contrast(img).enhance(50.0))
    plot.show()


def show_grayscale(img):
    gray = np.dot(img[..., :3], [0.299, 0.587, 0.114])
    plot.imshow(gray, cmap=plot.get_cmap('gray'))
    plot.show()


img = image.imread('photo.jpg')
show_image(img)
show_grayscale(img)
split_into_channels(img)
img = Image.open('photo.jpg')
contrast(img)
