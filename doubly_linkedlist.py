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
            self.head = self.tail = new_node
        self.length += 1

    def insert_at_position(self, index, data):
        if index <= 0:
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

    def remove_start(self):
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            self.length -= 1

    def remove_at_position(self, index):
        if index < 0 or index >= self.length:
            print('Index out of range!')
        
        if index == 0:
            self.remove_start()
        
        if index == self.length - 1:
            self.remove_end()
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.length -= 1
    
    def remove_end(self):
        if self.tail:
            if self.tail == self.head:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            self.length -= 1

    def traverse_forward(self):
        if not self.head:
            return 'Linked list is empty!'

        result = ''
        temp = self.head
        while temp:
            result += str(temp.data)+ ' <-> '
            temp = temp.next
        return result.rstrip(' <-> ')
    
    def traverse_backward(self):
        if not self.tail:
            return 'Linked list is empty!'
        
        result = ''
        temp = self.tail
        while temp:
            result += str(temp.data) + ' <-> '
            temp = temp.prev
        return result.rstrip(' <-> ')


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_start(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_end(4)
    dll.insert_at_position(0, 77)
    print(dll.traverse_forward())
    print(dll.traverse_backward())
