m = 1000000007
import sys
import numpy as np


def solve(A):
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0 and j > 0:
                A[i][j] = (A[i][j - 1] + A[i][j]) % -m
            elif j == 0 and i > 0:
                A[i][j] = (A[i - 1][j] + A[i][j]) % -m
            else:
                A[i][j] = (A[i - 1][j] + A[i][j - 1] - A[i - 1][j - 1] + A[i][j]) % -m


# A = [[-5, -4, -3], [-1, 2, 3], [2, 2, 4]]
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.max(A))
print(np.array(A[1][1]))
print(A)
solve(A)
print(A)

ans = -sys.maxsize - 1
for i in range(len(A)):
    for j in range(len(A[0])):
        for k in range(i, len(A)):
            ssum = 0
            for l in range(j, len(A)):
                if i == 0 and j == 0:
                    ssum = A[k][l]
                elif i == 0:
                    ssum = A[k][l] - A[k][j - 1]
                elif j == 0:
                    ssum = A[k][l] - A[i - 1][l]
                else:
                    ssum = (A[k][l] - A[i - 1][l] - A[k][j - 1] + A[i - 1][j - 1])
            ans = max(ans, ssum)

print(ans)
