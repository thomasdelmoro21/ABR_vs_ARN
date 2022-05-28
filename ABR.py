"""
@author Thomas Del Moro
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = Node(key)

    def treeSearch(self, key):
        return self.search(self.root, key)

    def search(self, currentNode, key):
        if currentNode is None or key == currentNode.key:
            return currentNode
        if key < currentNode.key:
            return self.search(currentNode.left, key)
        else:
            return self.search(currentNode.right, key)

    def treeInorder(self):
        self.inorder(self.root)

    def inorder(self, currentNode):
        if currentNode is not None:
            self.inorder(currentNode.left)
            print(str(currentNode.key) + " , ")
            self.inorder(currentNode.right)

    def treeMinimum(self):
        return self.minimum(self.root)

    def minimum(self, currentNode):
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def treeMaximum(self):
        return self.maximum(self.root)

    def maximum(selfself, currentNode):
        while currentNode.right is not None:
            currentNode = currentNode.right
        return currentNode

    def insert(self, key):
        y = None
        x = self.root
        while x is not None:
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        if y is None:
            self.setRoot(key)
        elif key < y.key:
            y.left = Node(key)
            y.left.parent = y
        else:
            y.right = Node(key)
            y.right.parent = y

    def transplant(self, u, v):
        if u.parent is None:
            self.setRoot(v.key)
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is None:
            v.parent = u.parent

    def delete(self, key):
        z = self.treeSearch(key)
        if z is None:
            return None
        elif z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
        return z

    def treeHeight(self):
        return self.height(self.root)

    def height(self, currentNode):
        if currentNode is None:
            return 0
        else:
            leftHeight = self.height(currentNode.left)
            rightHeight = self.height(currentNode.right)
            return max((leftHeight+1), (rightHeight+1))

