# A=10
# B=1
# C=[1,8,11,3]

A=4
B=10
C=[884,228,442,889]

# min=C[0]
# max=C[0]
# for i in range(1,len(C)):
#     max=max + C[i]
#     if C[i]>min:
#         min=C[i]
# min=min*B
# max=max*B
#
# print(min,max)
#
# def check(A,time,P):
#     count=1
#     PainterTime=time
#     for i in range(0,len(A)):
#         if A[i]*B > time:
#             return False
#         if A[i]*B <= PainterTime:
#             PainterTime -= A[i]*B
#         else:
#             count +=1
#             if count > P:
#                 return False
#             PainterTime = time-A[i]*B
#
#     return True
#
#
#
# l=min
# r=max
# while l <= r :
#     mid=(l+r)//2
#
#     ismid=check(C,mid,A)
#     ismidminus=check(C,mid-1,A)
#     #print(l, r, mid, ismid , mid-1,ismidminus)
#     if ismid==True and ismidminus==False:
#         print(mid)
#         break
#
#     elif ismid==False:
#         l=mid+1
#
#     else:
#         r=mid-1
#
#

A=1
B=1000000
C=[1000000,1000000]

def check( A, time, P):
    count = 1
    PainterTime = time

    for i in range(len(A)):
        if A[i] * B > time:
            return False

        if A[i] * B <= PainterTime:
            PainterTime -= A[i] * B

        else:
            count += 1
            if count > P:
                return False
            PainterTime = time - A[i] * B

    return True

mint = C[0]
maxt = C[0]
for i in range(len(C)):
    maxt += C[i]
    if mint < C[i]:
        mint = C[i]

l = mint * B
r = maxt * B

while (l <= r):
    mid = (l + r) // 2

    ismid = check( C, mid, A)
    ismidminus = check( C, mid - 1, A)

    if ismid == True and ismidminus == False:
        print( mid)
        break
    elif ismid == False:
        l = mid + 1
    else:
        r = mid - 1




