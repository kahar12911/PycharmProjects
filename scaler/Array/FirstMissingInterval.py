A=[3,4,-1,1]

n=len(A)
arr=[False]*(n+1)
print(arr)

for i in range(n):
    if A[i]>0 and A[i] <= n:
        arr[A[i]]=True

print(arr)
for i in range(1,n+1):
    if arr[i] == False:
        print(i)

