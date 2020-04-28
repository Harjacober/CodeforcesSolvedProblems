def solution(arr):
    i = 1
    while i < len(arr):
        if abs(arr[i] - arr[i-1])%2 != 0:
            return "NO"
        i += 1
    return "YES"

for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    print(solution(A))
