import math
def thanosSort(arr):
    mas = []
    t = 1
    length = 1
    for i in range(int(math.log(len(arr))/math.log(2))):
        t *= 2
        for j in range(len(arr)//t):
            start = j*t
            stop = j*t+t
            mas.append(arr[start:stop])

    for e in mas:
        if e == sorted(e):
            if len(e) > length:
                length = len(e)
    return length            
        

def thanossort2(arr):
    count = 1
    lpower = 1
    ans = 1
    i = 1
    j = 0
    while i < len(arr): 
        if arr[i] >= arr[i-1]:
            count += 1
            i += 1
            log = math.log(count)/math.log(2)
            print(i)
            if log-int(log) == 0.0 and math.log(i-1)/math.log(2)==0.0: 
                print(count,j,-2)
                lpower = count 
                ans = max(ans, lpower)
        else: 
            i *= 2
            lpower = 1

    return ans            
            
            
        
n = int(input())
arr = list(map(int,input().split())) 
print(thanossort2(arr))     
