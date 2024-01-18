A=36

pf=[True]*(A+1)
i=2
while i*i <= A:
    if pf[i]==False:
        i+=1
        continue
    for j in range(i*i,A,i):
        pf[j]=False
    i+=1

print(pf)

i=2
j=A-2
while i<=j:
    if pf[i]==True and pf[j]==True:
        print(i,j)
        break
    i+=1
    j-=1



