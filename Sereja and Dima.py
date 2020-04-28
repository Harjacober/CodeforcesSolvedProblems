from collections import deque
sereja,dima = 0,0
s,d = True, False
n = int(input())
cards = deque(map(int, input().split()))
while cards:
    if cards[0] > cards[-1]:
        if s:
            sereja += cards[0]
            s = False
            d = True
        else:
            dima += cards[0]
            d = False
            s = True
        cards.popleft()
    else:
        if s:
            sereja += cards[-1]
            s = False
            d = True
        else:
            dima += cards[-1]
            d = False
            s = True
        cards.pop()        

print(sereja, dima)
