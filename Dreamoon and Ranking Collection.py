def solution(n,x,arr):
    cache = [False]*201
    for e in arr:
        cache[e-1] = True
    
    for i in range(len(cache)):
        if cache[i] == False and x>0:
            cache[i] = True
            x -= 1
        if x <= 0: break 
    for j,b in enumerate(cache):
        if b==False:
            return j 


for _ in range(int(input())):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(solution(n,x,a))
