for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    x,y,x1,y1,x2,y2 = list(map(int, input().split()))
    u = b-a+x
    v = d-c+y 
    flag = True
    if (u >= x1 and u <= x2) and (v >= y1 and v <= y2):
        if(x-int(bool(a))) < x1 and (x+int(bool(b))) > x2:flag = False 
        if(y-int(bool(c))) < y1 and (y+int(bool(d))) > y2: flag = False
    else:
        flag = False
    if flag: print("Yes")
    else: print("No")
