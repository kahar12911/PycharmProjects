

#A="abababab"
#A='abcaabcaab'
#A='abababababb'
A='zzzzzzzzzzzzzzbzzzzzzzzzzzzzzbzzzzzzzzzzzzzzbzzzzzzzzzzzzzzbzzzzzzzzzzzzzzbzzzzzzzzzzzzzzbzzzzzzzzzzzzzzbzzzzzzzzzzzzzzbzzzzzzzz'

def createlps(A,lps):
    m=len(A)
    i,j=0,1
    while j < m:
        if A[i]==A[j]:
            i+=1
            lps[j]=i
            j+=1
        else:
            if i!=0:
                i=lps[i-1]
            else:
                j+=1
    return lps

def KMPSerch(A):
    n=len(A)
    lps=[0]*n
    createlps(A,lps)
    print(lps)
    i=0
    while i< n:
        if lps[i]==0:
            cnt1=i
        elif lps[i]==1:
            cnt2=i
        i+=1
    print(cnt1,cnt2)
    if cnt2-cnt1==1 or cnt1 > cnt2:
        return cnt1+1
    else:
        return cnt2
    


ans=KMPSerch(A)
print(ans)
    