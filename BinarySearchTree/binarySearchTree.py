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
            self.root = Node(data=data, parent=None)
    
    def _insert_node(self, data, node):
        if data < node.data:
            if node.left_node:
                """
                Recursively inserts a new value into the binary search tree by comparing 
                data with the current node and placing it in the appropriate left or right subtree.
                """
                self._insert_node(data, node.left_node)
            else:
                node.left_node = Node(data=data, parent=node)
        else:
            if node.right_node:
                self._insert_node(data, node.right_node)
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
            # removing a leaf node
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node", node.data)
                parent = node.parent

                # when the leaf node is the left node of it's parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                
                # when the leaf node is the right node of it's parent
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                
                if parent is None:
                    self.root = None
                
                del node

            # when the node has a single right child
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with a single right child", node.data)
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                if parent is None:
                    self.root = node.right_node
                
                node.right_node.parent = parent
                del node
            
            # when the node has a single left child
            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with a single left child", node.data)
                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                if parent is None:
                    self.root = node.left_node
                
                node.left_node.parent = parent
                del node

            # when the node has two children
            else:
                print("Removing a node with two children")
                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self._remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node
    
    def in_order(self):
        if self.root:
            self._in_order_traversal(self.root)
        else:
            print("Tree is empty")
    
    def _in_order_traversal(self, node):
        if node.left_node:
            self._in_order_traversal(node.left_node)
        print(node.data)

        if node.right_node:
            self._in_order_traversal(node.right_node)

    def pre_order(self):
        if self.root:
            self._pre_order_traversal(self.root)
        else:
            print("Tree is empty!")
        
    def _pre_order_traversal(self, node):
        print(node.data)

        if node.left_node:
            self._pre_order_traversal(node.left_node)
        
        if node.right_node:
            self._pre_order_traversal(node.right_node)

    def post_order(self):
        if self.root:
            self._post_order_traversal(self.root)
        else:
            print("Tree is empty!")

    def _post_order_traversal(self, node):
        if node.left_node:
            self._post_order_traversal(node.left_node)
        
        if node.right_node:
            self._post_order_traversal(node.right_node)
        
        print(node.data)



if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(7)
    bst.insert(8)
    bst.insert(14)
    bst.insert(19)
    bst.insert(10)
    bst.post_order()
    print("----------------")
    bst.remove(10)
    bst.post_order()