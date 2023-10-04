class Singleton:
    _instance = None  # 클래스 변수로서 인스턴스를 저장

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = None
        return cls._instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


# 싱글턴 인스턴스 생성
singleton1 = Singleton()
singleton2 = Singleton()

# 두 변수가 동일한 인스턴스를 참조하는지 확인
print(singleton1 is singleton2)  # 출력: True

# 값을 설정하고 확인
singleton1.set_value(42)
print(singleton2.get_value())  # 출력: 42
