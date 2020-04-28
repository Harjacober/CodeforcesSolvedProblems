n = int(input())
first = input()
count = 1
for i in range(1,n):
    second = input()
    if second != first:
        count += 1
    first = second


print(count)    
