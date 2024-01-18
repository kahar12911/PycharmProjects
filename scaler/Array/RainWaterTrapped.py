A=[0,1,0,2]

n=len(A)

Rmax=[0]*n
Lmax=[0]*n
Lmax[0]=A[0]
Rmax[n-1]=A[n-1]
for i in range(1,n):
    Lmax[i]=max(A[i],Lmax[i-1])

for i in range(n-2,-1,-1):
    Rmax[i]=max(A[i],Rmax[i+1])

trapwater=0
for i in range(0,n):
    trapwater += min(Lmax[i],Rmax[i])-A[i]

print(trapwater)