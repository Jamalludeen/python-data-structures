import logging

logging.basicConfig(level=logging.WARNING)

class Array:
    def __init__(self, num_rows):
        self.array = [0] * num_rows
        self.index = 0

    def push(self, value):
        self.array.append(value)

    def pop(self):
        self.array.pop()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.array[self.index]
            self.index += 1
            return item
        except:
            logging.waning('Array is empty')

    def __len__(self):
        return len(self.array)

    def __getitem__(self, index):
        try:
            return self.array[index]
        except:
            logging.warning('Such value does not exist')

    def __setitem__(self, index, value):
        self.array[index] = value

    def clear(self, value):
        for i in range(len(self)):
            self.array[i] = value

    def __repr__(self):
        a = [i for i in self.array]
        return str(a)

