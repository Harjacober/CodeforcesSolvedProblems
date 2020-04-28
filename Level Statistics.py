  

for _ in range(int(input())):
    n = int(input())
    p,c = list(map(int, input().split()))
    diff = p-c
    flag = True
    if diff <0: flag = False
    for i in range(1,n):
        pi,ci = list(map(int, input().split()))
        diffi = pi-ci
        if not (pi>=p and ci>=c and pi>=ci and diffi>=diff): flag = False
        p,c,diff = pi,ci,diffi

    if flag: print("YES")
    else: print("NO")
