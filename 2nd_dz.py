import numpy as np

# P_1

# 1

#  б) BA 5*5
#  в) AB 8*8, BA 3*3
#  г) AB BA 4*4

# 2

A = np.array([[1, -2], [3, 0]])
B = np.array([[4, -1], [0, 5]])

sum_arr = A + B
dot_arr = np.dot(A, B)
print(f'Сумма матриц\n{sum_arr}')
print(f'Произведение матриц\n{dot_arr}')

# 3

A = np.array([[1, 7], [3, -6]])
B = np.array([[0, 5], [2, -1]])
C = np.array([[2, -4], [1, 1]])

result = 3*A - 2*B + 4*C
print(f'результат\n{result}')

# 4

A = np.array([[4, 1], [5, -2], [2, 3]])

A_At = np.dot(A, A.T)
At_A = np.dot(A.T, A)
print(A_At)
print(At_A)


# P_2


# 1a

# sin*sin - cos *(-cos) = 1

# 1б

A = np.array([[4, 2, 3], [0, 5, 1], [0, 0, 9]])
print(np.linalg.det(A)) # 180

# 1в

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.linalg.det(A)) # 0

# 2a 16
# 2б 4
# 2в нужна размерность матрицы

# 3

A = np.array([[-2, 7, -3], [4, -14, 16], [-3, 7, 13]])
print(np.linalg.det(A)) # -70 det != 0

# 4a

A = np.array([[1, 2, 3], [1, 1, 1], [2, 3, 4]])
print(np.linalg.matrix_rank(A)) # 2

# 4б

A = np.array([[0, 0, 2, 1], [0, 0, 2, 2], [0, 0, 4, 3], [2, 3, 5, 6]])
print(np.linalg.matrix_rank(A)) # 3


