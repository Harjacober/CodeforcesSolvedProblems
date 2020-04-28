def minimize(n,k,s):
    s.sort()
    print(s)
    l,r = 1,n-2
    i = 1
    ans = 0
    minn = float('inf')
    while l<=r and ans<=k:
        diffl = (s[l]-s[l-1])*i 
        if ans+diffl <= k:
            minn = min(minn, s[r+1]-s[l])
        #print(minn)    
        diffr = (s[r+1]-s[r])*i 
        if ans+diffr <= k:
            minn = min(minn, s[r]-s[l-1])
        #print(minn)    
        ans += (diffl+diffr)
        if ans <= k:
            minn = min(minn, s[r]-s[l])
        #print(minn)    
        l += 1
        r -= 1
        i += 1
    return minn                       

n,k = list(map(int, input().split()))
s = list(map(int, input().split()))
print(minimize(n,k,s))
                       
