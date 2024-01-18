import sys
# A = [1, 12, 10, 3, 14, 10, 5]
# B = 8

# A=[52,7,93,47,68,26,51,44,5,41,88,19,78,38,17,13,24,74,92,5,84,27,48,49,37,59,3,56,79,26,55,60,16,83,63,40,55,9,96,29,7,22,27,74,78,38,11,65,29,52,36,21,94,46,52,47,87,33,87,70]
# B=19
A=[5,17,100,11]
B=20
count=0

for i in A:
    if i <=B:
        count+=1

l=0
r=count-1
curr_swap=0
for i in range(count):
    if A[i] > B :
        curr_swap+=1
print(count,curr_swap)
min_ans=curr_swap
l+=1
r+=1
while r < len(A):
    print(l,r,curr_swap,min_ans)
    if A[l-1] > B :
        curr_swap-=1
    if A[r] > B :
        curr_swap+=1
    min_ans=min(min_ans,curr_swap)
    l+=1
    r+=1

print(min_ans)



