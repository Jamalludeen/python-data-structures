class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = []
        
    def push(self, value):
        if len(self.stack) < self.size:
            self.stack.append(value)
        else:
            print("Stack is full!")
                
    def pop(self):
        if len(self.stack) >= 1:
            data = self.stack[-1]
            del self.stack[-1]
            return f'{data} poped'
        
        else:
            return "Stack is empty!"