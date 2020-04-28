k, r = list(map(int, input().split()))
b = k
i = 1
while True:
    if k*i%10 == 0 or k*i%10 == r:
        break
    i += 1 

print(i)
