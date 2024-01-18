
# A = [-1, 0, 1, 2, -1, 4]
A=[1,-4,0,0,5,-5,1,0,-2,4,-4,1,-1,-4,3,4,-1,-1,-3]

A.sort()
print(A)
n=len(A)
ans=[]
for i in range(n):

    if i > 0 and A[i]==A[i-1]:
        continue



    j=i+1
    k=n-1
    while j < k:
        target=A[j]+A[k]




        if target==-A[i]:
            ans.append([A[i],A[j],A[k]])
            j+=1
            k-=1
            while j<k and A[j]==A[j+1]:
                j+=1
            while j<k and A[k]==A[k-1]:
                k-=1

        if target < -A[i]:
            j+=1

        else:
            k-=1

print(ans)



