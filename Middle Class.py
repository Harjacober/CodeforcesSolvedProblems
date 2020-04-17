def solution(arr,x): 
    arr.sort(reverse=True) 
    rem, ans = 0,0
    i= 0
    while i < len(arr):  
        summ = arr[i]+rem 
        if summ >= x:
            ans += 1
            rem = summ-x
        i += 1
        
    return ans

for _ in range(int(input())):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(solution(a,x))
            
        
        
