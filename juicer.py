n,b,d = list(map(int, input().split()))
oranges = map(int,input().split())
waste, count = 0,0
for i in oranges:
    if i <= b:
        waste += i
    if waste > d:
        count += 1
        waste = 0

print(count)        
