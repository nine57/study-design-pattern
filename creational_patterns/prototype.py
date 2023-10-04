import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype1(Prototype):
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"ConcretePrototype1 with value: {self.value}")


class ConcretePrototype2(Prototype):
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"ConcretePrototype2 with name: {self.name}")


# 프로토타입 생성
prototype1 = ConcretePrototype1(10)
prototype2 = ConcretePrototype2("Prototype")

# 프로토타입 복제
clone1 = prototype1.clone()
clone2 = prototype2.clone()

# 복제된 객체 확인
clone1.show()  # 출력: ConcretePrototype1 with value: 10
clone2.show()  # 출력: ConcretePrototype2 with name: Prototype