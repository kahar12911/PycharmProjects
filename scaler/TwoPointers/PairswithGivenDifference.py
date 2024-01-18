#using HM
A=[8, 12, 16, 4, 0, 20]
B=4

hm={}

for i in range(len(A)):
    if hm.get(A[i])==None:
        hm[A[i]]=1
    else:
        hm[A[i]] += 1

print(A)
print(hm)
count=0
for i in A:
    if i-B in hm :
        print(i, i-B, hm[i])
        if i==abs(B-i) and hm[i] > 1:
            count+=1
        else:
            count+=1

print(count)



