import math
q = int(input())
for _ in range(q):
    a,b,n,s = list(map(int, input().split())) 
    if s//n <= a:
        if s%n <= b:
            print("YES")
        else:
            print("NO")
    else:
        if math.ceil((s-b)/n) <= a:
            print("YES")
        else:
            print("NO")
