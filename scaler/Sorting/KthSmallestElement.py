A=[8,16,80,55,32,8,38,40,65,18,15,45,50,38,54,52,23,74,81,42,28,16,66,35,91,36,44,9,85,58,59,49,75,20,87,60,17,11,39,62,20,17,46,26,81,92]

B=9
n=len(A)
for i in range(0,n):
    ismall=A[i]
    pos=i
    for j in range(i+1,n):
        if ismall > A[j]:
            ismall=A[j]
            pos=j
    temp=A[i]
    A[i]=A[pos]
    A[pos]=temp
    print(A)
    if i== B-1:
        print("kth smallest element ",A[B-1])
        break