class Queue:
    def __init__(self, size):
        self.get_size = size
        self.queue = [] 
        self.top = 0
    
    def enqueue(self, value):
        if len(self.queue) < self.get_size:
            self.queue.append(value)
        else:
            print("Queue is full!")

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop()
        else:
            return "Queue is empty!"
        
    def rear(self):
        if len(self.queue):
            return self.queue[-1]
        else:
            return "Queue is empty!"  
    
    def front(self):
        if len(self.queue):
            return self.queue[0]
        else:
            return "Queue is empty!"