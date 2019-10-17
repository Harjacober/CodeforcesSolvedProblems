from collections import deque
def pages(n, p, k):
    ans = deque(["("+str(p)+")"])
    for i in range(1,k+1):
        if p-i >= 1:
            ans.appendleft(str(p-i))
        if p+i <= n:     
            ans.append(str(p+i))

    if p-k > 1:
        ans.appendleft("<<")
    if p+k < n:
        ans.append(">>")

    return " ".join(ans)

arr = list(map(int, input().split()))
print(pages(arr[0], arr[1], arr[2]))    
     
