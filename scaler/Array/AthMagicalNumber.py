import math

# A=19
# B=11
# C=13
m=1000000000+7
# A=807414236
# B=3788
# C=38141
# A=21
# B=10
# C=12



A=11
B=12
C=13

l=min(B,C)
r=(min(B,C) * A)
ans=0
#print(math.lcm(B,C))
while(l<=r):
    mid=l+ (r-l)//2
    ans= ((mid//B) + (mid//C) - (mid//(math.lcm(B,C))))
    print(l,r,mid,ans)
    if ans >= A:
        if ans==A:
            ans=mid
            print(ans)
        r=mid-1
    else:
        l=(mid + 1)


#print(l,r)
print(ans % m)

A=11
B=12
C=13

m=1000000000 + 7
l=min(B,C)
r=min(B,C)*A
ans=0
lcm=(B*C)//math.gcd(B,C)
while l <= r:
    mid=l+ (r-l)//2
    count= mid//B + mid//C - mid//lcm

    if count >= A:
        if count==A:
            ans=mid
        r=mid-1
    else:
        l=mid+1

print( ans%m)

# mod = (10**9)+7
# gcd = math.gcd(B,C)
# lcm = (B*C)//gcd
#
# def gcd(self,b,c):
#     if c == 0:
#         return b
#     return self.gcd(c,b%c)
#
# def magic_count(a,b,c,lcm):
#     return ((a//b) + (a//c) - (a//lcm))
#
# l = min(B,C)
# h = min(B,C)*A
# floor = 0
# while l <= h:
#     m = l + ((h-l)//2)
#     magic = magic_count(m,B,C,lcm)
#
#     if magic >= A:
#         floor = m
#         h = m-1
#     else:
#         l = m+1
#
# print( floor%mod)
