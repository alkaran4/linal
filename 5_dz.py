import numpy as np
np.set_printoptions(precision=2, suppress=True)


# 1

A = np.array([
    [1, 0, 3],
    [1, 0, 2],
    [0, -4, 6],
    [1, 0, 5],
    [2, 5, 0]
])

U, s, W = np.linalg.svd(A)

D = np.zeros_like(A, dtype=float)
D[np.diag_indices(min(A.shape))] = s
V = W.T


# 2

print(s[0]) # 9.32

# 3

A_f = np.linalg.norm(s)
print(A_f)
