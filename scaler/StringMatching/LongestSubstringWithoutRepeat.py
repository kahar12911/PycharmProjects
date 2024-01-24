
A = "abcabcbb"
#A='AaaA'
#A='dadbc'
A='bbbbbbbbbbbbbbbbbbbbbb'

def AnagramNoRepeat(A):
    hs=set()
    ans=0
    l,r=0,0
    n=len(A)
    while r < n:
        if A[r] not in hs:
            hs.add(A[r])
            r += 1
        else:
            while A[l] != A[r]:
                hs.remove(A[l])
                l += 1
            hs.remove(A[l])
            l += 1
    #print(hs)
        ans=max(ans , len(hs))
    return ans



print(AnagramNoRepeat(A))
#print(len(AnagramNoRepeat(A)))
    