
A='abcd'


def BoringString(A):
    m=36
    Even=''
    Odd=''
    for i in A:
        if int(i,m)%2==0:
            Even+=i
        else:
            Odd+=i
    
    minE,maxE=Even[0],Even[0]
    for i in Even:
        if minE > i:
            minE = i
    maxO=Odd[0]
    for j in Odd:
        if j > maxO:
            maxO = j
    
    print(minE,maxO)

    if abs(int(minE,36) - int(maxO,36)) !=1:
        return 1
    else :
        return 0
    # if abs(int(Even[0],36) - int(Odd[-1],36))!=1:
    #     return 1
    # elif abs(int(Odd[0],36) - int(Even[-1],36))!=1:
    #     return 1
    # return 0
    



print(BoringString(A))


