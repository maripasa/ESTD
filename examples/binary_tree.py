from typing import Optional

class BinaryNode:
    def __init__(self, 
                 key: int,
                 value = None,
                 parent: Optional["BinaryNode"] = None,
                 left: Optional["BinaryNode"] = None,
                 right: Optional["BinaryNode"] = None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def penis(self) -> None:
        print("penis")

class AVLTree:
    def __init__(self):
        self.root: Optional[BinaryNode] = None

    def insert(self, key: int, value=None) -> None:
        def _insert(node: BinaryNode):
            if key == node.key:
                raise ValueError

            if key > node.key:
                if node.right is None:
                    node.right = BinaryNode(key, value, node)
                    return
                _insert(node.right)

            if key < node.key:
                if node.left is None:
                    node.left = BinaryNode(key, value, node)
                    return
                _insert(node.left)

        if self.root is None:
            self.root = BinaryNode(key, value)
            return
        return _insert(self.root)

    def __repr__(self) -> str:

        def repr(node: Optional[BinaryNode]) -> str:
            if node is None:
                return " \n"

            result = str(node.key) + "\n"
            right, left = "", ""

            right = repr(node.right)
            left = repr(node.left)

            right = right.splitlines()
            left = left.splitlines()
            
            result += "├── " + str(left.pop()) + "\n"
            for i in left:
                result += "│   " + str(i) + "\n"

            result += "└── " + str(right.pop()) + "\n"
            for i in right:
                result += "    " + str(i) + "\n"

            return result

        return repr(self.root)

test = AVLTree()
x = [4, 6, 2, 1, 3, 5, 7]
y = [2, 1, 3]
for i in y:
    test.insert(i)

print(test)

