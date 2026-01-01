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

    def remove(self, data):
        if self.root:
            self._remove_node(data, self.root)
        else:
            print("Tree is empty!")
    
    def _remove_node(self, data, node):
        if node is None:
            return
        
        if data < node.data:
            self._remove_node(data, node.left_node)
        
        elif data > node.data:
            self._remove_node(data, node.right_node)
        
        else:
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node", node.data)