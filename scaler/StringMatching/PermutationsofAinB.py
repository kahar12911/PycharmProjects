A='abc'
B='abcbacabc'

def CreateMap(A,B):
    m=len(A)
    myMap = {}
    Window={}
    for i in range(m):
        if A[i] not in myMap:
            myMap[A[i]]=1
        else:
            myMap[A[i]]+=1
    
    for i in range(m):
        if B[i] not in Window:
            Window[B[i]]=1
        else:
            # When we see a character that is already in the window, remove it from the window.
            Window[B[i]]+=1
    
    print(myMap,Window)
    return (myMap,Window)

def PermutationCheck(A,B):
    mymap,window = CreateMap(A,B)
    ans=0
    if mymap==window:
        ans+=1
    i=0
    j=len(A)
    n=len(B)
    while j < n:
        window[B[i]]-=1
        if window[B[i]]==0:
            del window[B[i]]
        i+=1
        if B[j] not in window:
            window[B[j]]=1
        else:
            window[B[j]]+=1
        j+=1
        if mymap==window:
            ans+=1
    return ans


print(PermutationCheck(A,B))

# m = len(A)
# n = len(B)
# myMap = dict()
# window = dict()
# ans = 0
# for i in range(m) :
#     if A[i] not in myMap :
#         myMap[A[i]] = 1
#     else :
#         myMap[A[i]] += 1
# for i in range(m) :
#     if B[i] not in window :
#         window[B[i]] = 1
#     else :
#         window[B[i]] += 1
# if window == myMap :
#         ans += 1

# l = 0
# for r in range(m,n) :
#     window[B[l]] -= 1
#     if window[B[l]] == 0 :
#         del window[B[l]]
#     if B[r] not in window :
#         window[B[r]] = 1
#     else :
#         window[B[r]] += 1
#     l += 1
#     if window == myMap :
#         ans += 1
# print( ans)
