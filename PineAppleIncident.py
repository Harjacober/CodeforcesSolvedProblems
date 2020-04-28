def pineapple(t,s,x):
    first = t
    if t == x:
        return("YES")
    else:    
        while first <= x:
            first += s
            second = first + 1
            if first==x or second==x:
                return("YES") 
        else:    
            return("NO")  
def pineapple2(t,s,x):
    a = (x-t)//s 
    if a > 0:
        b = a*s+t
        b1 = b+1 
        if b==x or b1==x:
            return("YES")
        else:
            return("NO")
    else:
        if t==x:
            return "YES"
        else:
            return "NO"

    
lis = list(map(int, input().split()))
t = lis[0]
s = lis[1]
x = lis[2]
print(pineapple2(t,s,x))

  
