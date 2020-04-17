from itertools import permutations
def solution(n,k):
    string = ("a"*(n-2)) + ("b"*2)
    i = 1
    p = permutations(string)
    for e in p:
        if i == k:
            return(''.join(e)) 
        i += 1


for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    print(solution(n,k))
