class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SinglyLinedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    

    def insert_start(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert_end(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def insert_at_position(self, index, data):
        if index <= 0:
            self.insert_start(data=data)
        elif index >= self.length-1:
            self.insert_end(data)
        else:
            pre = self.head
            temp = self.head

            while index:
                pre = temp
                temp = temp.next
                index -= 1
            else:
                new_node = Node(data=data)
                new_node.next = temp
                pre.next = new_node
                self.length += 1

    def delete_start(self):
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
        print("LinkedList is empty!")
    
    def delete_end(self):
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = None
                self.tail = temp
            self.length -= 1
        else:
            print("LinkedList is empty!")
    
    def traverse(self):
        _str = ''
        temp = self.head
        while temp.next:
            _str += str(temp.data) + ' -> '
            temp = temp.next
        else:
            _str += str(temp.data)
        print(_str)

if __name__ == "__main__":
    linked_list = SinglyLinedList()
    linked_list.insert_start(10)
    linked_list.insert_start(20)
    linked_list.insert_start(30)
    linked_list.insert_at_position(9, 77)
    linked_list.traverse()
    linked_list.delete_start()
    linked_list.traverse()
    linked_list.delete_end()
    linked_list.traverse()
