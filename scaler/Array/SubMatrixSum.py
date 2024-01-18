m = 1000000007
def solve(A):

    for i in range(0 ,len(A)):
        for j in range(0 ,len(A[0])):
            if i== 0 and j == 0:
                continue
            elif i == 0 and j > 0:
                A[i][j] = A[i][j - 1] + A[i][j]
            elif j == 0 and i > 0:
                A[i][j] = A[i - 1][j] + A[i][j]
            else:
                A[i][j] = (A[i - 1][j] + A[i][j - 1] - A[i - 1][j - 1] + A[i][j]) % m
    print(A)


A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
B = [1, 2, 1]
C = [1, 2, 1]
D = [2, 3, 1]
E = [2, 3, 3]

print(A)
solve(A)
print(A)
out = []
ans=0
for q in range(0, len(B)):
    i = B[q]-1
    j = C[q]-1
    k = D[q]-1
    l = E[q]-1
    print(i,j,k,l)
    if i==0 and j==0:
        out.append(A[k][l])
    elif i==0:
        out.append(A[k][l]-A[k][j-1])
    elif j==0:
        out.append(A[k][l]-A[i-1][l])
    else:
        ans = (A[k][l] - A[i - 1][l] - A[k][j - 1] + A[i - 1][j - 1]) % m
        out.append(ans)

print(out)




