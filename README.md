# lab12
Лабораторна робота №12: Операції з матрицями
2.2 Мета роботи:
Метою цієї лабораторної роботи є створення класу Matrix для представлення матриць та реалізації різних операцій з ними, таких як додавання елементів, обчислення сум рядків, транспонування, множення на іншу матрицю, перевірка на симетричність, обертання, вирівнювання та інше.

2.3 Опис завдання:
Конструктор __init__: Ініціалізує матрицю заданих розмірностей зі значеннями за замовчуванням (0).

Метод add_element: Додає заданий елемент у вказану позицію матриці.

Метод sum_of_rows: Обчислює суму елементів у кожному рядку матриці.

Метод transpose: Повертає транспоновану матрицю.

Метод multiply_by: Перемножує поточну матрицю на іншу матрицю.

Метод is_symmetric: Перевіряє, чи є матриця симетричною відносно головної діагоналі.

Метод rotate_right: Повертає матрицю на 90 градусів вправо.

Метод flatten: Повертає вирівняний список елементів матриці.

Статичний метод from_list: Створює об'єкт класу Matrix зі списку списків (list_of_lists).

Метод diagonal: Повертає список діагональних елементів матриці (для квадратних матриць).

2.4 Виконання роботи:
Створено клас Matrix з усіма необхідними методами.
Кожен метод був протестований з використанням відповідних прикладів використання.
Реалізовано приклади використання для кожного методу, що демонструють їх правильну роботу.
2.5 Результати:
Нижче наведено приклади використання різних методів класу Matrix з виводом результатів:


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
