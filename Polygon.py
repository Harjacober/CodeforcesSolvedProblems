t = int(input())
for _ in range(t):
    n,m = list(map(int, input().split()))
    if n%m == 0:
        print("YES")
    else:
        print("NO")
