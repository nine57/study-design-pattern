# 반복 가능한 컬렉션 클래스를 정의합니다.
class MyCollection:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def __iter__(self):
        # 이 메서드는 반복자 객체를 반환합니다.
        return MyIterator(self)


# 반복자 클래스를 정의합니다.
class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        # 반복자 객체 자체가 반복 가능해야 합니다.
        return self

    def __next__(self):
        # 다음 요소를 반환하고 인덱스를 증가시킵니다.
        if self.index < len(self.collection.data):
            item = self.collection.data[self.index]
            self.index += 1
            return item
        else:
            # 모든 요소를 순회한 경우 StopIteration 예외를 발생시킵니다.
            raise StopIteration


if __name__ == "__main__":
    # 컬렉션 객체를 생성하고 요소를 추가합니다.
    collection = MyCollection()
    collection.add_item("첫 번째")
    collection.add_item("두 번째")
    collection.add_item("세 번째")

    # 반복자를 통해 컬렉션의 요소를 순회합니다.
    for item in collection:
        print(item)


"""
1. MyCollection 클래스:
반복 가능한 컬렉션을 나타내며,
요소를 추가하는 메서드인 add_item과 반복자를 반환하는 __iter__ 메서드를 구현합니다.

2. MyIterator 클래스:
반복자 객체를 나타내며, 컬렉션과 현재 인덱스를 추적합니다.
__iter__와 __next__ 메서드를 구현하여 반복자 객체를 만듭니다.

메인 부분에서는 컬렉션을 생성하고 요소를 추가한 후, 반복자를 통해 컬렉션의 요소를 순회하고 출력합니다.

파이썬에서는 이러한 작업을 간단하게 할 수 있는 내장된 반복자와 iter() 및 next() 함수를 제공합니다.
하지만 이 예제를 통해 반복자 패턴의 개념과 동작 방식을 이해할 수 있습니다.
"""
