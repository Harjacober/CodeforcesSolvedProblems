import heapq
def Pad(n, arr):
    odd = []
    even = []
    for i in range(n):
        if arr[i]%2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    size = abs(len(odd) - len(even))
    if size == 0:
        return 0
    if len(odd) > len(even):
        ans = heapq.nsmallest(size-1, odd)
    else:
        ans = heapq.nsmallest(size-1, even)

    return sum(ans)

n = int(input())
arr = list(map(int, input().split()))
print(Pad(n, arr))

            
           
