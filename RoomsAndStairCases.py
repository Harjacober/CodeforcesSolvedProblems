def rooms(n,s):
    maxx = n
    for i in range(n):
        if s[i] == "1":
            maxx = max((n-i)*2,maxx)
            break
    for j,e in enumerate(s[::-1]):
        if e == "1":
            maxx = max((n-j)*2,maxx)
            break
    print(maxx)


for i in range(int(input())):
    n = int(input())
    s = input()
    rooms(n,s)
        
