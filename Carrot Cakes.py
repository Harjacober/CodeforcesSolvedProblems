import math
n,t,k,d = list(map(int, input().split()))
atst = math.ceil(n/k)
t_time = atst*t
if t_time - t > d:
    print("YES")
else:
    print("NO")
