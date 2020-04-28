def permutations(n,arr): 
    pos = 0
    for j in range(1, n):
        if pos == n - 1:
            break
        i = arr.index(j)
        if i == pos:
            pos += 1
        elif i > pos:
            arr.insert(pos, arr.pop(i))
            pos = i

    return arr


q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    print(*permutations(n,arr))
