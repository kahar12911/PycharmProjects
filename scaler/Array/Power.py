

def power(A,B,C):
    if B==1:
        return A%C
    #ans=(A%C * A%C)%C
    ans=(power(A,B//2,C) * power(A,B//2,C))%C
    print(A,B,C,ans)
    if B%2==0:
        return ans
    else:
        return (ans * A)%C



a=power(2,5,100)

print(a)
