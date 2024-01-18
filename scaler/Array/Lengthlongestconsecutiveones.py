#A = "111000"
#A='11010110000000000'
#A='00000011111111'
#A='0111001101111101010010'
#A='0111110110'
#A='11010110000000000'
#A='1111111111111'
A="0111111111"
n = len(A)
l = [0] * n
r = [0] * n
l[0] = int(A[0])
count = 0
curr_count = 0
max_count = 0
for i in range(0, n):
    if A[i] == '1':
        count += 1
if count==n:
    max_count=count
    print(max_count)
    exit(0)
#print(A,l,r)
for i in range(1, n):
    if A[i] == '1':
        l[i] = l[i - 1] + 1

r[n - 1] = int(A[n - 1])
for i in range(n - 2, -1, -1):
    if A[i] == '1':
        r[i] = r[i + 1] + 1
print("maxl",max(l),"maxr",max(r))
print(A,count, l, r)
if A[0]=='0' and r[1]==count:
    print(count)
    exit(0)
if A[n-1]=='0' and l[n-2]==count:
    print(count)
    exit(0)

for i in range(1, n-1):
    curr_count = l[i-1]+r[i+1]
    if A[i] == '0':
        if curr_count == count:
            print(count)
            max_count = max(max_count, curr_count)
            break
        if curr_count < count:
            curr_count = l[i - 1] + r[i + 1] + 1
            max_count = max(max_count, curr_count)
        #print("i",i,l[i-1], r[i+1])

print("max",max_count)


