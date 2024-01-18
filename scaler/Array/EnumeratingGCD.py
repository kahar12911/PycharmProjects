def gcd(A,B):
    print(A,B)
    if A==1 or B==1:
        print("1")
        return int(1)
    elif A==0:
        print("B",B)
        return B
    elif B==0:
        print("A",A)
        return A
    if B >= A:
        return gcd(B%A,A)
    else:
        return gcd(A%B,B)

# A='678728391838182039102'
# B='678728391838182039103'

A='215591698179351812564'
B='103686308'
A=int(A)
B=int(B)
ans=0
for i in range(A,B+1):
    ans=gcd(ans,int(i))
    if ans==1:
        break
print(ans)