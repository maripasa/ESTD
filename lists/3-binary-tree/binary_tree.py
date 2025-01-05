import random
""" Escreva algoritmos recursivos e não-recursivos para determinar:
    o número de nós de uma árvore binária;
    a soma do conteúdo de todos os nós de uma árvore binária;
    o nível com maior soma de uma árvore binária;
    a altura de uma árvore binária;
    a profundidade de uma árvore binária.
Escreva um algoritmo para determinar se uma árvore binária é:
    própria
    completa
    quase completa """

class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
        self.father = None
        self.isLeft = False

    def setLeft(self, data):
        self.left = Node(data)
        self.left.isLeft = True
        self.left.father = self

    def setRight(self, data):
        self.right = Node(data)
        self.right.isLeft = False
        self.right.father = self

class BinaryTree:
    def __init__(self, root = None):
        self.root =root

    def preOrder(self, root):
        if root is None:
            return
        print(root.data,sep="-->", end="-->")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data,sep="-->", end="-->")
        self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)        
        self.postOrder(root.right)
        print(root.data,sep="-->", end="-->")

def buildRandomTree(seed, size):
    root = Node(seed)
    bt = BinaryTree(root)
    i = 1

    while( i < size):
        p = q = root
        number = random.randint(0,size*40)
        while  number != p.data  and q is not None:
            p=q
            if number < p.data:
                q = p.left
            else:
                q = p.right
        if number == p.data:
            continue
        elif number < p.data:
            p.setLeft(number)
        else:
            p.setRight(number)
        i+=1
    return bt, root
   
b,r = buildRandomTree(45,10)
b.inOrder(r)

""" Escreva algoritmos recursivos e não-recursivos para determinar:
    o número de nós de uma árvore binária;
    a soma do conteúdo de todos os nós de uma árvore binária;
    o nível com maior soma de uma árvore binária;
    a altura de uma árvore binária;
    a profundidade de uma árvore binária.
Escreva um algoritmo para determinar se uma árvore binária é:
    própria
    completa
    quase completa """

def non_recursive_node_num(root: Node | None) -> int:
    if root is None:
        return 0
    stack = [root]
    count = 0
    while stack:
        node = stack.pop()
        count += 1
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return count

def non_recursive_content_sum(root: Node | None) -> int:
    if root is None:
        return 0
    stack = [root]
    total = 0
    while stack:
        node = stack.pop()
        total += node.data
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return total

def non_recursive_biggest_level(root: Node | None) -> int | None:
    if root is None:
        return None
    queue = [(root, 0)]  # (node, level)
    level_sums = {}
    
    while queue:
        node, level = queue.pop(0)
        if level not in level_sums:
            level_sums[level] = 0
        level_sums[level] += node.data
        
        if node.left: queue.append((node.left, level + 1))
        if node.right: queue.append((node.right, level + 1))

    max_level = max(level_sums, key=level_sums.get)
    return max_level

def recursive_height(node: Node | None) -> int:
    return 0 if node is None else 1 + max(recursive_height(node.left), recursive_height(node.right))

def non_recursive_height(root: Node | None) -> int:
    if root is None:
        return 0
    queue = [root]
    height = 0
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        height += 1
    return height

def recursive_depth(node: Node | None, value: int) -> int:
    if node is None:
        return -1
    if node.data == value:
        return 0
    left_depth = recursive_depth(node.left, value)
    right_depth = recursive_depth(node.right, value)
    
    if left_depth != -1: return left_depth + 1
    if right_depth != -1: return right_depth + 1
    return -1

def non_recursive_depth(root: Node | None, value: int) -> int:
    if root is None:
        return -1
    queue = [(root, 0)]  # (node, depth)
    
    while queue:
        node, depth = queue.pop(0)
        if node.data == value:
            return depth
        if node.left: queue.append((node.left, depth + 1))
        if node.right: queue.append((node.right, depth + 1))
    
    return -1

def is_proper(root: Node | None) -> bool:
    if root is None:
        return True
    if (root.left is None and root.right is not None) or (root.left is not None and root.right is None):
        return False
    return is_proper(root.left) and is_proper(root.right)

def is_complete(root: Node | None) -> bool:
    if root is None:
        return True
    queue = [root]
    is_full = False
    
    while queue:
        node = queue.pop(0)
        
        if node.left:
            if is_full: return False
            queue.append(node.left)
        else:
            is_full = True
            
        if node.right:
            if is_full: return False
            queue.append(node.right)
        else:
            is_full = True
    return True

def is_almost_complete(root: Node | None) -> bool:
    if root is None:
        return True
    queue = [root]
    found_null = False
    
    while queue:
        node = queue.pop(0)
        
        if node is None:
            found_null = True
        else:
            if found_null:
                return False
            queue.append(node.left)
            queue.append(node.right)
    return True
