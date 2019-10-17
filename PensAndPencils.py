import math
def pens(a,b,c,d,k):
    l = math.ceil(a/c)
    p = math.ceil(b/d)
    if (l+p) <= k:
        print(l,p)
    else:
        print(-1)


for i in range(int(input())):
    a,b,c,d,k = list(map(int, input().split()))
    pens(a,b,c,d,k)
               
