n = int(input())
coins = list(map(int, input().split()))
coins.sort()
count,v = 0,0
for j in range(len(coins)-1,-1,-1):
    count += 1
    v += coins[j]
    if v > sum(coins)//2:
        break
print(count)    
        
    
