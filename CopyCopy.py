def solution(arr):
    return len(set(arr))

for _ in range(int(input())):
    a = int(input())
    array = map(int, input().split())
    print(solution(array))
