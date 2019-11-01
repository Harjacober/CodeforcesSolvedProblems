l,b = list(map(int, input().split()))
years = 0
while True:
    if l > b:
        break 
    l *= 3
    b *= 2
    years += 1 

print(years)    
