n,x = list(map(int, input().split()))
d = 0
for i in range(n):
    sign, val = input().split()
    val = int(val)
    if sign == "+":
        x += val
    else:
        if x >= val:
            x -= val
        else:
            d += 1

print(x,d)
