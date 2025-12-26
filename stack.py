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
        
    def peek(self):
        try:
            return self.stack[-1]
        except:
            return "Stack is empty!"
                               
    def get_items(self):
        return f'stack -> {self.stack}'
    
    
    def traverse(self):
        if len(self.stack):
            for i in self.stack:
                print(i)
        else:
            print("Stack is empty!")

