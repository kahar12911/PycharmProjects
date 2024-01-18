# # A=[1,1,2,3]
# # B=4
#
# #A=[1,2,3,3,4,6,7]
# #
# #A=[1,2,6,6,7,9,9]
# # B=13
# # A=[2,3,3,5,7,7,8,9,9,10,10]
# # B=11
# # A=[1,1,2,2,3,3,4,5,5,6,9,10]
# # B=5
#
# A=[1,1,1,2,2,3,4,5,6,7,8,9]
# B=2
#
# # A=[2,2,3,4,4,5,6,7,10]
# # B=8
# hm={}
# for i in range(len(A)):
#     if A[i] not in hm:
#         hm[A[i]]=1
#     else:
#         hm[A[i]] +=1
#
# print(hm)
# count=0
# for key in hm:
#     if B-key in hm :
#
#         if key==B-key and hm[key]>1:
#
#             count+= ((hm[key] * (hm[key]-1))//2)
#             print(key, B - key,count)
#         elif key != B-key and hm[key]>0:
#             count += (hm[key] * hm[B-key])
#             hm[key]=0
#             hm[B-key]=0
#             print(key, B - key,count)
#
#
# print(count)
#

A=[2,3,5,6,10]
B=6
n=len(A)
i = 0
j = len(A)-1

count=0
while i < j:
    print(i,j)
    if A[i] + A[j] == B:
        if A[i] != A[j]:
            x = A[i]
            y = A[j]

            freq_x = 0
            freq_y = 0
            while i < n and A[i] == x:
                freq_x += 1
                i += 1
            while j > -1 and A[j] == y:
                freq_y += 1
                j -= 1
            count += (freq_x * freq_y)
        else:
            x = A[i]
            freq = 0
            while i < n and A[i] == x:
                freq += 1
                i += 1
            count += (freq * (freq - 1)) // 2

    elif A[i] + A[j] < B:
        i += 1
    else:
        j -= 1

print( count)