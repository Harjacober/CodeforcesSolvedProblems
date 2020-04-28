def cme(n):
    if n < 4:
        return 4-n 
    if n%2 == 0:
        return 0
    else:
        return 1

n =int(input())
for i in range(n):
    print(cme(int(input())))





    
