n = int(input()) 
y_cord = []
for i in range(n):
    e = list(map(int, input().split())) 
    y_cord.append(e[1])
k = int(input())
count = 0
for j in y_cord:
    if k <= j:
        break
    else:
        count += 1
print(n-count)        
