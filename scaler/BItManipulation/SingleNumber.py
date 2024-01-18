


A=[3,3,3,11,11,11,2,2,2,5,8,8,8]
ans=0
for i in range(0,32):
    count=0
    for j in range(0,len(A)):
        if A[j]>>i & 1 == 1:
            count+=1

    if count%3==1:
        ans=ans | 1<<i

print(ans)

