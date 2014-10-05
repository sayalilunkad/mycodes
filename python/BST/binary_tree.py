# Implements Binary Search Tree in Python.


class BinarySearchTree:
    '''
    Properties:
    1)The left subtree of a node contains only
    nodes with keys less than the node's key.
    2)The right subtree of a node contains only
    nodes with keys greater than the node's key.
    3)The left and right subtree each must also
    be a binary search tree.
    4)Each node can have up to two successor nodes.
    5)There must be no duplicate nodes.
    6)A unique path exists from the root to every other node.
    '''

    def __init__(self):
        '''Initializes the root node and size of the BinarySearchTree.'''

        self.root = None
        self.size = 0

    def length(self):
        '''Returns size of the BinarySearchTree.'''

        return self.size

    def __len__(self):
        '''Defines length attribute for BinarySearchTree.'''

        return self.size

    def put(self, key, val):
        '''
        Method will check to see if the tree already has a root.

        if it has a root:
            call _put()
        else:
            Create a new Node and assign it as the root node.
        '''

        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        '''
        Method will search the tree to insert the
        new node which is not the root node.

        Search algo:
        1) Starting at the root of the tree, search the binary tree comparing
        the new key to the key in the current node.
            1)If the new key is less than the current node,
            search the left subtree.
            2)If the new key is greater than the current node,
            search the right subtree.
            3)When there is no left (or right) child to search,
            we have found the position in the tree where the
            new node should be installed.
        2) To add a node to the tree, create a new Node object
        and insert the object at the point discovered in
        the previous step.
        '''

        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(key, val, parent=currentNode)


class Node:
    '''Storage class for BinarySearchTree nodes.'''

    def __init__(self, key, val, left=None, right=None, parent=None):
        '''Initializes a node.'''

        self.key = key
        self.data = val
        self.rightChild = right
        self.leftChild = left
        self.parent = parent

    def hasLeftChild(self):
        '''Checks if node has leftChild.'''

        return self.leftChild

    def hasRightChild(self):
        '''Checks if node has rightChild.'''

        return self.rightChild

    def isLeftChild(self):
        '''Checks if node is a leftChild of some node.'''

        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        '''Checks if node is a right child of some node.'''

        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        '''Checks if node is a root node.'''

        return not self.parent

    def isLeaf(self):
        '''Checks if node is a leaf node.'''

        return not (self.isLeftChild or self.rightChild)

    def hasAnyChildren(self):
        '''Checks if node has any children, left or right child node.'''

        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        '''Checks if node has both left and right child node.'''

        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, val, lc, rc):
        '''
        Replaces the node data with new node data and
        reassigns the child nodes appropriately.
        '''

        self.key = key
        self.data = val
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
