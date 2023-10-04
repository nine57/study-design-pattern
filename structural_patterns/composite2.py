# Component
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        raise NotImplementedError


# Leaf
class Developer(Employee):
    def display_info(self):
        return f"{self.position}: {self.name}"


# Leaf
class Designer(Employee):
    def display_info(self):
        return f"{self.position}: {self.name}"


# Composite
class Manager(Employee):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.subordinates = []

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        self.subordinates.remove(employee)

    def display_info(self):
        info = [f"{self.position}: {self.name}"]
        for subordinate in self.subordinates:
            info.append("\t" + subordinate.display_info())
        return "\n".join(info)


# Usage
if __name__ == "__main__":
    dev1 = Developer("Alice", "Developer")
    dev2 = Developer("Bob", "Developer")

    designer1 = Designer("Charlie", "Designer")
    designer2 = Designer("David", "Designer")

    manager = Manager("Eve", "Development Manager")
    manager.add_subordinate(dev1)
    manager.add_subordinate(dev2)
    manager.add_subordinate(designer1)
    manager.add_subordinate(designer2)

    print(manager.display_info())
