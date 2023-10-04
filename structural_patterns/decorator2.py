from abc import ABCMeta, abstractmethod


class Beverage(metaclass=ABCMeta):
    """
    Component
    """

    @abstractmethod
    def get_cost(self) -> int:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class Americano(Beverage):
    """
    Concrete Component
    """

    def get_cost(self) -> int:
        return 3000

    def get_description(self) -> str:
        return "아메리카노"


class HerbalTea(Beverage):
    """
    Concrete Component
    """

    def get_cost(self) -> int:
        return 4000

    def get_description(self) -> str:
        return "허브티"


class CondimentDecorator(Beverage):
    """
    Decorator
    """

    def __init__(self, beverage: Beverage):
        self.__beverage = beverage

    @abstractmethod
    def get_cost(self) -> int:
        return self.__beverage.get_cost()

    @abstractmethod
    def get_description(self) -> str:
        return self.__beverage.get_description()


class Sugar(CondimentDecorator):
    """
    Concrete Decorator
    """

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def get_cost(self) -> int:
        return super().get_cost() + 200

    def get_description(self) -> str:
        return super().get_description() + " 설탕 추가"


class Shot(CondimentDecorator):
    """
    Concrete Decorator
    """

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def get_cost(self) -> int:
        return super().get_cost() + 500

    def get_description(self) -> str:
        return super().get_description() + " 샷 추가"


americano = Americano()
americano_one_sugar = Sugar(americano)

print(americano_one_sugar.get_cost())
print(americano_one_sugar.get_description())

# 3200
# 아메리카노 설탕 추가
