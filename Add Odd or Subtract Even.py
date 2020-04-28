for _ in range(int(input())):
    a,b = list(map(int, input().split()))
    diff = b-a
    if diff == 0: print(0)
    else: 
        if diff > 0:
            if diff&1==0: print(2)
            else: print(1)
        else:
            if diff&1==0: print(1)
            else: print(2)
