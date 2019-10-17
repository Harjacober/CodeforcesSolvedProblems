def badPrices(n, days):
    smallest = days[-1]
    count = 0
    for i in range(n-2,-1,-1):
        if days[i] > smallest:
            count += 1
        else:
            smallest = days[i]
    return count


t = int(input())
for i in range(t):
    n = int(input())
    days = list(map(int, input().split()))
    print(badPrices(n, days))
            
        
