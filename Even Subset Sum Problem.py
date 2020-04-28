def evenSubset(arr):
    indexes = []
    for i,e in enumerate(arr):
        if e%2 == 0:  
            return 1, [i+1]
        else:
            indexes.append(i+1)
            if len(indexes) > 1:
                return 2,indexes
    return -1, []

t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    ans, index = evenSubset(array)
    print(ans)
    if index:
        print(*index) 
