import random
""" Escreva algoritmos recursivos e não -recursivos para determinar:
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

class BinTree:
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
    bt = BinTree(root)
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
