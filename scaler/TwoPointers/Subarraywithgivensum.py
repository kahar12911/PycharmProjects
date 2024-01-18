

A=[1,2,3,4,5]
B=5

i=0
j=0
sum=0

while i < len(A) and j < len(A):
    if sum < B:
        sum += A[j]
        j +=1

    if sum > B:
        sum -= A[i]
        i +=1

    if sum ==B:
        print(i,j,A[i:j])
        break

