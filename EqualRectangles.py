def equalRectangles(arr):
    Set = set(arr)
    if len(Set) == 1:
        return "YES"
    if len(Set)%2==0:
        return evaluateSet(list(Set))
    else:
        return "NO"
def evaluateSet(arr):
    arr.sort()
    low = 0
    high = len(arr)-1
    Set = set() 
    while low < high:
        Set.add(arr[low]*arr[high])
        low += 1
        high -= 1
    if len(Set)==1:
        return "YES"
    else:
        return "NO"
q = int(input())
for i in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    print(equalRectangles(arr))
    
