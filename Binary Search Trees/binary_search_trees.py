class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)


    def insert(self, new_val):
        self.insert_helper(self.root, new_val)


    def insert_helper(self, current, new_val):
