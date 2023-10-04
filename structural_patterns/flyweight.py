class TreeType:
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture


class Tree:
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def draw(self):
        print(f"Drawing a {self.tree_type.name} tree at ({self.x}, {self.y})")


class TreeFactory:
    tree_types = {}

    @staticmethod
    def get_tree_type(name, color, texture):
        key = (name, color, texture)
        if key not in TreeFactory.tree_types:
            TreeFactory.tree_types[key] = TreeType(name, color, texture)
        return TreeFactory.tree_types[key]


if __name__ == "__main__":
    tree1 = Tree(1, 2, TreeFactory.get_tree_type("Pine", "Green", "Fine"))
    tree2 = Tree(3, 4, TreeFactory.get_tree_type("Pine", "Green", "Fine"))
    tree3 = Tree(5, 6, TreeFactory.get_tree_type("Maple", "Red", "Rough"))

    tree1.draw()  # Drawing a Pine tree at (1, 2)
    tree2.draw()  # Drawing a Pine tree at (3, 4)
    tree3.draw()  # Drawing a Maple tree at (5, 6)
