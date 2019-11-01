n = int(input())
cities = list(map(int, input().split()))
print(abs(cities[1]-cities[0]), abs(cities[-1]-cities[0]))
for i in range(1,n-1):
    minn = min(abs(cities[i]-cities[i-1]),abs(cities[i+1]-cities[i]))
    maxx = max(abs(cities[-1]-cities[i]),abs(cities[i]-cities[0]))
    print(minn, maxx)
    
print(abs(cities[-1]-cities[-2]), abs(cities[-1]-cities[0]))
