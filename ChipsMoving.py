import operator
def chipsMoving(n, coord):
    zero = 0
    one = 0
    for i in coord:
        if i%2 == 0:
            one += 1
        else:
            zero += 1
    return min(one, zero)

n = int(input())
coord = list(map(int, input().split()))
print(chipsMoving(n, coord))
