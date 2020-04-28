n = int(input())
arr = list(map(int, input().split()))
import heapq
smallest = heapq.nsmallest(arr)
count = 1
for i in range(1,smallest//2+1):
    if smallest%i == 0:
        count += 1
print(count)        
