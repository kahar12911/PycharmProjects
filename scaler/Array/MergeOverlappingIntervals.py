

#A= [[1,3],[2,6],[8,10],[15,18]]

A= [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]


result=[]
result.append(A[0])
# print(A[0])
# print([A[0]])
# print(result)
l=0
for i in range(1,len(A)):
    if result[l][1] > A[i][0]:
        result[l]= [min(result[l][0],A[i][0]) , max(result[l][1],A[i][1]) ]
    else:
        l+=1
        result.append(A[i])

print(result)


