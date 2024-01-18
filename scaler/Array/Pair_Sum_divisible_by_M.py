# A=[1,2,3,4,5]
# B=2
#
# count=0
# for i in range(0,len(A)):
#     for j in range(i+1,len(A)):
#         print(A[i],A[j],A[i]+A[j],A[i]%A[j])
#         if (A[i]+A[j]) % B== 0:
#             count+=1
#             print(count)
#
# print(count)

A=[5,17,100,11]
B=28
hm=[0] * B

for i in A:
    hm[i%B]+=1

#print(hm)
result=0

for i in range(0,B//2+1):

    if i==0 or 2*i==B:
        result=result+ (hm[i] * (hm[i]-1))//2
        #print(i, hm[i],result)
    else:

        result=result + hm[i] * hm[B-i]
        #print(i, hm[i], B - i, hm[B - i],result)
    #print(result)

print(result)