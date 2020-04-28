 
t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(*sorted(array, reverse=True))

