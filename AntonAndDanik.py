n = int(input())
score = input()
from collections import Counter
b = Counter(score) 
if b['A'] > b['D']:
    print('Anton')
elif b['D'] > b['A']:
    print('Danik')
else:
    print("Friendship")
