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
    
class RBTree:
    def __init__(self):
        self.root: Optional[BinaryNode] = None


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
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return left_height - right_height

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
            if key < node.key:
                node.left = insert(node.left)
            elif key > node.key:
                node.right = insert(node.right)
            else:
                node.value = value

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

    def remove(self, key: int) -> None:
        def remove(node: Optional[BinaryNode], delete_key: int) -> Optional[BinaryNode]:
            if node is None:
                raise KeyError("Item not in list")
            if delete_key < node.key:
                node.left = remove(node.left, delete_key)
            if delete_key > node.key:
                node.right = remove(node.right, delete_key)

            if delete_key == node.key:
                if node.left is None and node.right is None:
                    return None

                if node.left is None:
                    return node.right

                if node.right is None:
                    return node.left

                successor = node.right
                while successor.left is not None:
                    successor = successor.left

                node.key = successor.key
                node.value = successor.value
                node.right = remove(node.right, successor.key)

            balance = self.balance(node)
            if balance > 1:
                left_balance = self.balance(node.left)
                if left_balance >= 0:
                    return self.rotate_right(node)
                else:
                    node.left = self.rotate_left(node.left)
                    return self.rotate_right(node)
            elif balance < -1:
                right_balance = self.balance(node.right)
                if right_balance <= 0:
                    return self.rotate_left(node)
                else:
                    node.right = self.rotate_right(node.right)
                    return self.rotate_left(node)
            return node

        try:
            self.root = _remove(self.root, key)
        except KeyError:
            pass
