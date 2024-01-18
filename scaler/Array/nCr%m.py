def compute(n,r,m):
    ans=1
    for i in range(n-r+1,n+1):
        ans=ans*i
    for i in range(1,r+1):
        ans=ans//i
    print(ans%m)

compute(5,2,13)