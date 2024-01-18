import time
#A = [2, 1, 6, 4]
#A=[1,1,1]
A=[1,2,3,7,1,2,3]
E = []
O = []
E.append(A[0])
O.append(0)
for i in range(1,len(A)):
    if i % 2 == 0:
        E.append(A[i] + E[i - 1])
        O.append(O[i - 1])
    else:
        O.append(A[i]+O[i-1])
        E.append(E[i-1])
    #print(time.sleep(5))
    print(E,O)

print(E,O)
count=0
n=len(A)
if E[n-1]-E[0]==O[n-1]:
    count+=1

for i in range(1,n):
    sum_E=E[i-1]+O[n-1]-O[i]
    sum_O=O[i-1]+E[n-1]-E[i]
    if sum_E==sum_O:
        count+=1

print(count)

