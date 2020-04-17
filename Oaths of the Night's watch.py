n = int(input())
arr = list(map(int, input().split()))
maxx, minn = max(arr), min(arr)
count = 0 
for i in arr:
    if i > minn and i < maxx:
        count += 1

print(count)        
