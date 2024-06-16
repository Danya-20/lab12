# Lab 12
class Matrix:
    def __init__(self, rows, cols):
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def add_element(self, row, col, value):
        self.data[row][col] = value

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed_data = list(zip(*self.data))
        rows, cols = len(transposed_data), len(transposed_data[0])
        transposed_matrix = Matrix(rows, cols)
        transposed_matrix.data = [list(row) for row in transposed_data]
        return transposed_matrix

    def multiply_by(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError("Matrix dimensions do not match for multiplication")
        
        result = Matrix(len(self.data), len(other.data[0]))
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(len(other.data)))
        return result

    def is_symmetric(self):
        return self.data == self.transpose().data

    def rotate_right(self):
        self.data = [list(row) for row in zip(*self.data[::-1])]

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        cols = len(list_of_lists[0])
        matrix = Matrix(rows, cols)
        matrix.data = list_of_lists
        return matrix

    def diagonal(self):
        if len(self.data) != len(self.data[0]):
            raise ValueError("Matrix is not square")
        return [self.data[i][i] for i in range(len(self.data))]

# Example usage for all tasks:

# Task 1
matrix = Matrix(2, 3)
print(matrix.data)  # [[0, 0, 0], [0, 0, 0]]

# Task 2
matrix.add_element(1, 2, 10)
print(matrix.data)  # [[0, 0, 0], [0, 0, 10]]

# Task 3
matrix.add_element(0, 0, 5)
matrix.add_element(0, 2, 10)
matrix.add_element(1, 1, 20)
print(matrix.sum_of_rows())  # [15, 20]

# Task 4
transposed = matrix.transpose()
print(transposed.data)  # [[0, 0], [1, 0], [0, 2]]

# Task 5
matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix1.add_element(1, 0, 4)
matrix1.add_element(1, 1, 5)
matrix1.add_element(1, 2, 6)

matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 7)
matrix2.add_element(0, 1, 8)
matrix2.add_element(1, 0, 9)
matrix2.add_element(1, 1, 10)
matrix2.add_element(2, 0, 11)
matrix2.add_element(2, 1, 12)

result = matrix1.multiply_by(matrix2)
print(result.data)  # [[58, 64], [139, 154]]

# Task 6
matrix3 = Matrix(2, 2)
matrix3.add_element(0, 1, 5)
matrix3.add_element(1, 0, 5)
print(matrix3.is_symmetric())  # True

# Task 7
matrix4 = Matrix(2, 2)
matrix4.add_element(0, 0, 1)
matrix4.add_element(0, 1, 2)
matrix4.add_element(1, 0, 3)
matrix4.add_element(1, 1, 4)
matrix4.rotate_right()
print(matrix4.data)  # [[3, 1], [4, 2]]

# Task 8
matrix5 = Matrix(2, 3)
matrix5.add_element(0, 0, 1)
matrix5.add_element(0, 1, 2)
matrix5.add_element(0, 2, 3)
matrix5.add_element(1, 0, 4)
print(matrix5.flatten())  # [1, 2, 3, 4]

# Task 9
list_of_lists = [[1, 2], [3, 4]]
matrix6 = Matrix.from_list(list_of_lists)
print(matrix6.data)  # [[1, 2], [3, 4]]

# Task 10
matrix7 = Matrix(3, 3)
matrix7.add_element(0, 0, 1)
matrix7.add_element(1, 1, 2)
matrix7.add_element(2, 2, 3)
print(matrix7.diagonal())  # [1, 2, 3]
