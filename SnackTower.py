import heapq
n=int(input())
snacks = list(map(int, input().split()))
heap = []
heapq.heapify(heap)

for e in snacks:
    if e == n:
        ans = []
        ans.append(n)
        while heap:
            if abs(heap[0]) == n-1:
                ans.append(abs(heapq.heappop(heap)))
                n = n-1
            else: 
                break
        print(*ans)
        n = n-1
    else:
        print("")
        heapq.heappush(heap, -e) 
            
