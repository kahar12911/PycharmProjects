# A=[1,2,3,4,5]
# B=10
# A=[5,10,20,100,105]
# B=130

# A= [2,24,38,25,35,33,43,12,49,35,45,47,5,33]
# B= 249

# A= [2,24,38,25,35,33,43,12,49,35,45,47,5,33]
# B= 249

# A= [5,10,20,100,105]
# B=130

A= [1,2,3,4,5,100]
B=10

# A= [1,1000000000]
# B= 1000000000
n=len(A)
ps=[0]*(n+1)
ps[0]=0
ps[1]=A[0]
for i in range(2,n+1):
    ps[i] = ps[i-1] +A[i-1]
k=0
print(A)
print(ps)
for i in range(n,0,-1):
    ans=ps[i]

    if ans > B:
        k=i
        print(i, ans, " < ", B, " failed")
        continue
    print(i, ans, " < ", B," true")
    for j in range(i+1,n):

        ans=ans-A[j-i-1]+ A[j]
        print(i, j, ans)
        if ans > B:
            if i==0:
                k=0
            k=i
            print("failed for ",i)
            break
    if ans <= B:
        k=i
        break

print(k)