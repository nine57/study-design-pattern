import random
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius, bg_image):
        self.x = x
        self.y = y
        self.radius = radius
        self.bg_image = bg_image

    def draw(self):
        print(f'draw circle - x : {self.x}, y : {self.y}, '
              f'radius : {self.radius}, bg_image : {self.bg_image.filename}')


class Image:
    def __init__(self, filename):
        self.filename = filename
        print(f'load image from {self.filename}')


class ShapeFactory:
    bg_images = {}

    @classmethod
    def get_circle(cls, x, y, radius, bg_image_filename):
        bg_image = cls.bg_images.get(bg_image_filename, None)
        if bg_image is None:
            bg_image = Image(bg_image_filename)
            cls.bg_images[bg_image_filename] = bg_image

        return Circle(x, y, radius, bg_image)


bg_image_filenames = ['flower.png', 'butterfly.png']

circles = []
for i in range(10):
    x = random.randint(0, 1000)
    y = random.randint(0, 1000)
    radius = random.randint(1, 100)
    bg_image_filename = bg_image_filenames[radius % len(bg_image_filenames)]

    circle = ShapeFactory.get_circle(x, y, radius, bg_image_filename)
    circles.append(circle)

for circle in circles:
    circle.draw()