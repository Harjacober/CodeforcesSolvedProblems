def solution(arr, n):
    cache = []
    for i in range(n):
        j = (i+1)%n 
        val = 0 if arr[i][1] >= arr[j][0] else arr[j][0]-arr[i][1]
        cache.append((arr[i][0],val))
    ans = 0
    for k in range(len(cache)):
        
        l = i+1
        print(cache[k])
        if l<len(cache):
            ans = min(ans, cache[k][0]+cache[k][1]+cache[l][1])
        else:
            ans = min(ans, cache[k][0]+cache[k][1])
    return ans
        

    print(cache)


for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(tuple(map(int, input().split())))

    print(solution(a,n))
    
7 15 7 0
2 14 2 0
5 3  5 4
7 15 7 2
17 3 17 4
