class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left_node = None
        self.right_node = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            self._insert_node(data, self.root)
        else:
            self.root = Node(data=data)
    
    def _insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                self._insert_node(data=data, node=node.left_node)
            else:
                node.left_node = Node(data=data, parent=node)
        else:
            if node.right_node:
                self._insert_node(data=data, node=node)
            else:
                node.right_node = Node(data=data, parent=node)
