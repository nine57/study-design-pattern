from abc import ABC, abstractmethod


# 실제 이미지 로딩을 담당하는 클래스
class Image:
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image from {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")


# 추상 프록시 클래스
class ImageProxy(ABC):
    @abstractmethod
    def display(self):
        pass


# 이미지 프록시 클래스
class LazyImageProxy(ImageProxy):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = Image(self.filename)
        self.real_image.display()


if __name__ == "__main__":
    # 이미지 프록시를 사용하여 이미지를 로딩 및 표시
    image_proxy = LazyImageProxy("image.jpg")

    # 이미지가 실제로 로딩되는 시점
    image_proxy.display()  # Loading image from image.jpg \n Displaying image: image.jpg
