from collections import Counter
a = list(map(int, input().split()))
s = list(map(int,input())) 
ans = 0
for e in s:
    ans += a[e-1] 
print(ans)
