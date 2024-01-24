from collections import Counter

A = "ADOBECODEBANC"
B = "ABC"

def WindowString(A , B):
    map = Counter(B)
    n = len(A)
    m = len(B)
    l = 0  
    r = 0
    count = m
    minlen = n
    Found = False
    start = 0
    end = n-1

    while r < n:
        
        # find all chars of B in A till count 0
        if A[r] in map:
            map[A[r]] -= 1
            if map[A[r]] >= 0:
                count -= 1
        r += 1

        if count > 0:
            continue
        
        # After finding all chars of B in A, find last occurance of 1st char of B in A
        while count==0:
            if A[l] in map:
                map[A[l]] += 1
                if map[A[l]] > 0 :
                    count += 1
            l += 1

        # Got l and r pos of substring in A
        if (r-l) < minlen:
            Found = True
            start = l
            end = r
            minlen = r-l
        
    if Found==True:
        if start == 0:
            return A[start:end]
        return A[start-1 : end]
    return ""

ans = WindowString(A,B)
print(ans)
           