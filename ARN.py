"""
@author Thomas Del Moro
"""


class NodeRN:
    def __init__(self, key):
        #Black = True
        #Red = False
        self.key = key
        self.color = True
        self.parent = None
        self.left = None
        self.right = None


class ARN:
    def __init__(self):
        self.nil = NodeRN(0)
        self.nil.color = True
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def setRoot(self, key):
        z = NodeRN(key)
        z.color = True
        z.left = self.nil
        z.right = self.nil
        self.root = z

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        z = NodeRN(key)
        z.parent = None
        z.left = self.nil
        z.right = self.nil
        z.color = False

        y = None
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.insertFixup(z)

    def insertFixup(self, z):
        while z != self.root and z.parent.color == False:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == False:
                    z.parent.color = True
                    y.color = True
                    z.parent.parent.color = False
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.color = True
                    z.parent.parent.color = False
                    self.rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == False:
                    z.parent.color = True
                    y.color = True
                    z.parent.parent.color = False
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.color = True
                    z.parent.parent.color = False
                    self.leftRotate(z.parent.parent)
        self.root.color = True

    def treeInorder(self):
        self.inorder(self.root)

    def inorder(self, currentNode):
        if currentNode != self.nil:
            self.inorder(currentNode.left)
            print(str(currentNode.key) + " , ")
            self.inorder(currentNode.right)

    def treePreorder(self):
        self.preorder(self.root)

    def preorder(self, currentNode):
        if currentNode != self.nil:
            print(str(currentNode.key) + (" Red" if currentNode.color == False else " Black"))
            self.preorder(currentNode.left)
            self.preorder(currentNode.right)

    def treePostorder(self):
        self.postorder(self.root)

    def postorder(self, currentNode):
        if currentNode != self.nil:
            self.postorder(currentNode.left)
            self.postorder(currentNode.right)
            print(str(currentNode.key) + (" Red" if currentNode.color == False else " Black"))

    def treeHeight(self):
        return self.height(self.root)

    def height(self, currentNode):
        if currentNode == self.nil:
            return 0
        else:
            leftHeight = self.height(currentNode.left)
            rightHeight = self.height(currentNode.right)
            return max((leftHeight+1), (rightHeight+1))

    def treeSearch(self, key):
        return self.search(self.root, key)

    def search(self, currentNode, key):
        if currentNode == self.nil:
            return False
        if key == currentNode.key:
            return currentNode
        if key < currentNode.key:
            return self.search(currentNode.left, key)
        else:
            return self.search(currentNode.right, key)
