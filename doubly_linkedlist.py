class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_start(self, data):
        new_node = Node(data=data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = self.head = new_node
        self.length += 1
    
    def insert_at_position(self, data, index):
        if index < 0:
            self.insert_start(data=data)
        elif index >= self.length-1:
            self.insert_end(data=data)
        
        else:
            new_node = Node(data=data)
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node
            self.length += 1

    def insert_end(self, data):
        new_node = Node(data=data)
        if self.tail:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1

    

