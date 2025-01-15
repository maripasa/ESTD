from typing import Optional

class BinaryNode:
    def __init__(self, 
                 key: int,
                 value = None,
                 left: Optional["BinaryNode"] = None,
                 right: Optional["BinaryNode"] = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    

class AVLTree:
    def __init__(self):
        self.root: Optional[BinaryNode] = None

    def height(self, node) -> int:
        def height(node: Optional[BinaryNode]) -> int:
            if node is None:
                return 0
            return 1 + max(height(node.right), height(node.left))
        return height(node)

    def balance(self, node) -> int:
        if node is None:
            return 0
        left = 0 if node.left is None else self.height(node.left)
        right = 0 if node.right is None else self.height(node.right)
        return left - right
    
    def rotate_left(self, node) -> BinaryNode:
        y = node.right
        t2 = y.left
        y.left = node
        node.right = t2

        return y

    def rotate_right(self, node) -> BinaryNode:
        y = node.left
        t3 = y.right
        y.right = node
        node.left = t3

        return y

    def insert(self, key: int, value=None) -> None:
        def insert(node: Optional[BinaryNode]) -> BinaryNode:
            if node is None:
                return BinaryNode(key, value)
            if key > node.key:
                node.right = insert(node.right)
            if key < node.key:
                node.left = insert(node.left)

            balance = self.balance(node)

            if node.left is not None:
                if balance > 1 and key < node.left.key:
                    return self.rotate_right(node)

                if balance > 1 and key > node.left.key:
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)

            if node.right is not None:
                if balance < -1 and key > node.right.key:
                    return self.rotate_left(node)

                if balance < -1 and key < node.right.key:
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)
            
            return node

        self.root = insert(self.root)

    def __repr__(self) -> str:
        def repr(node: Optional[BinaryNode]) -> str:
            if node is None:
                return " \n"

            result = str(node.key) + "\n"

            right = repr(node.right).splitlines()
            left = repr(node.left).splitlines()

            result += "├── " + str(left.pop(0)) + "\n"
            for i in left:
                result += "│   " + str(i) + "\n"

            result += "└── " + str(right.pop(0)) + "\n"
            for i in right:
                result += "    " + str(i) + "\n"

            return result

        return repr(self.root)

test = AVLTree()
x = [4, 6, 2, 1, 3, 5, 7]
y = [2, 1, 3]
for i in range(100):
    test.insert(i)

print(test)

