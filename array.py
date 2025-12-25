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


class Array2D:
    def __init__(self, num_of_rows, num_of_cols):
        self.num_of_rows = num_of_rows
        self.num_of_cols = num_of_cols

        self._the_rows = Array(num_of_rows)

        for i in range(num_of_rows):
            self._the_rows[i] = Array(num_of_cols)

    def __getitem__(self, index):
        try:
            return self._the_rows[index]
        except:
            raise IndexError

    def __setitem__(self, index, value):
        for indexes in range(len(self._the_rows)):
            try:
                self._the_rows[indexes] = value
            except IndexError as IR:
                print(f'Index error {indexes} index does not exist')

    def __len__(self):
        return self.num_of_rows

    def num_rows(self):
        return self.num_of_rows

    def num_cols(self):
        return self.num_of_cols

    def show(self):
        for row in range(self.num_rows()):
            for column in range(len(self._the_rows[row])):
                print(f'the column {column+1}: {self._the_rows[row][column]}')
            print('*'*30)

    def clear(self, value):
        for row in range(self.num_rows()):
            for column in range(len(self._the_rows[row])):
                self._the_rows[row][column] = value
