class LegacyCalculator:
    def calculate(self, x, y):
        result = x + y
        print(f"Legacy Calculator: {x} + {y} = {result}")


class ModernCalculator:
    def add(self, x, y):
        result = x + y
        print(f"Modern Calculator: {x} + {y} = {result}")


class ModernCalculatorAdapter:
    def __init__(self, modern_calculator):
        self.modern_calculator = modern_calculator

    def calculate(self, x, y):
        self.modern_calculator.add(x, y)


# 기존의 레거시 코드
legacy_calculator = LegacyCalculator()
legacy_calculator.calculate(5, 3)

# 새로운 모던 코드
modern_calculator = ModernCalculator()
modern_calculator.add(5, 3)

# 어댑터 패턴을 사용하여 모던 코드를 레거시 코드와 호환되게 함
adapter = ModernCalculatorAdapter(modern_calculator)
adapter.calculate(5, 3)
