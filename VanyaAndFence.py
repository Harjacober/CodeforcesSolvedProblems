n,h = list(map(int, input().split()))
height = list(map(int, input().split()))
width = 0
for i in height:
    if i <= h:
        width += 1
    else:
        width += 2

print(width)        
