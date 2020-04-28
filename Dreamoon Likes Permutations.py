def solution(n,arr):
    ans = []
    cache = [False]*199999
    count = 0
    for e in arr:
        if cache[e-1] == True:
            break
        cache[e-1] = True
        count += 1
    if all(cache[0:count]): 
        if count != n:  
            if sum(range(1,n-count+1))==sum(arr[count:n]):
                ans.append((count,n-count))
            if sum(range(1,count+1))==sum(arr[n-count:n]):
                ans.append((n-count,count))
    cache = [False]*199999
    count = 0
    for a in range(n-1,-1,-1): 
        if cache[arr[a]-1] == True:
            break
        cache[arr[a]-1] = True
        count += 1 
    if all(cache[0:count]): 
        if count != n:  
            if sum(range(1,n-count+1))==sum(arr[0:n-count]):
                ans.append((n-count,count))
            if sum(range(1,count+1))==sum(arr[0:count]):
                ans.append((n-count,count))
            
        
    return ans
    
        
for _ in range(int(input())):
    n = int(input())
    al = list(map(int, input().split()))
    res = solution(n,al)
    print(len(res))
    Set = set()
    for e in res:
        if str(e[0])+str(e[1]) not in Set:
            print(*e)
            Set.add(str(e[0])+str(e[1]))
    
    
