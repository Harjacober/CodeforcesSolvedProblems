def weirdSort(arr):
    n = len(arr)
    i = n-1
    Set = set()
    while i>=0:
        j = i-1
        while arr[i] < arr[j] and j>=0:
            arr[i],arr[j] = arr[j],arr[i]
            Set.add(j+1)
            j-=1
        i-=1
    return Set
 
for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = set(map(int, input().split()))
    ans = weirdSort(a)
    if ans.issubset(p): print("YES")
    else: print("NO")
