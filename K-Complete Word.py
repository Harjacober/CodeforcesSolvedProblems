from collections import Counter
def solution(n,k,string):
    dic = {}
    for i in range(0,k):
        p = []
        pos = i
        for j in range(0,(n//k)): 
            p.append((string[pos],pos))
            pos += k 
        Dhere = {}
        for e,m in p:
            if e not in Dhere:
                Dhere[e] = [1,m]
            else:
                Dhere[e][0] += 1
                Dhere[e][1] = m
        print(Dhere)
        dic[i] = [max(Dhere,key=lambda x:(Dhere[x][0],Dhere[x][1])),Dhere[max(Dhere,key=lambda x:Dhere[x])]]
    print(dic)
            
    arr = list(string[0:k])
    l,r = 0,len(arr)-1
    while l<r:
        if arr[l] != arr[r]:
            a,b = dic[l],dic[r]
            if a[1][0] > b[1][0]:
                val = a[0]
            else:
                val = b[0]
            arr[r],arr[l] = val,val
        l += 1
        r -= 1
    new_string = arr*(n//k)
    ans = 0
    for i in range(n):
        if string[i] != new_string[i]:
            ans += 1

    return ans


for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    print(solution(n,k,input()))
