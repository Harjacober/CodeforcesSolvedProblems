def football(n,p,w,d): 
    x,y = p//w,0
    ans = x*w + y*d
    if x>n:
        return -1
    while ans!=p: 
        x -= 1
        y += 1
        ans = x*w + y*d
        if x < 0:
            return [-1]
    z = n -(x+y)
    return (x,y,z)
 
n,p,w,d = list(map(int, input().split()))
print(*football(n,p,w,d))
        
