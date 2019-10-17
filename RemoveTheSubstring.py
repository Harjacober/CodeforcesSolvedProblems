def remove(s, t):
    if len(s)==len(t):
        return 0
    for i in range(len(s)-len(t)): 
        arr = [s[i]]
        for j in range(i+1,i+len(t)):
            arr.append(s[j]) 
        if arr == t:
            if len(s)-(i+len(t)) > i:
                return len(s)-(i+len(t))
            else:
                return i
            


s = list(input())
t = list(input())
print(remove(s,t))            
