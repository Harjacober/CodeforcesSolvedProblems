n = int(input())
x_cord = []
y_cord = []
for i in range(n):
    e = input().split()
    x_cord.append(e[0])
    y_cord.append(e[1])

set_x = set(x_cord)
set_y = set(y_cord)

if len(set_x) < len(set_y):
    print(len(set_x))
else:
    print(len(set_y))
    
