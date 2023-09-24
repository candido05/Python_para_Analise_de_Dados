class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if node == None:
            return 0
        return node.height

    def getBalance(self, node):
        if node == None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rightRotate(self, node):
        leftChild = node.left
        rightGrandChild = leftChild.right
        leftChild.right = node
        node.left = rightGrandChild
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        leftChild.height = max(self.getHeight(leftChild.left), self.getHeight(leftChild.right)) + 1
        return leftChild

    def leftRotate(self, node):
        rightChild = node.right
        leftGrandChild = rightChild.left
        rightChild.left = node
        node.right = leftGrandChild
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        rightChild.height = max(self.getHeight(rightChild.left), self.getHeight(rightChild.right)) + 1
        return rightChild

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            return
        self.root = self.insertNode(self.root, val)

    def insertNode(self, node, val):
        if node == None:
            return Node(val)
        elif val < node.val:
            node.left = self.insertNode(node.left, val)
        else:
            node.right = self.insertNode(node.right, val)

        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1 and val < node.left.val:
            return self.rightRotate(node)

        if balance < -1 and val > node.right.val:
            return self.leftRotate(node)

        if balance > 1 and val > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        if balance < -1 and val < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

# Cria a árvore binária balanceada
tree = AVLTree()

# Insere alguns nós
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(25)

# Imprime a árvore
def printTree(node, level=0):
    if node != None:
        printTree(node.right, level+1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.left, level+1)

printTree(tree.root)
