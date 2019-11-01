n = int(input())
a = list(map(int, input().split()))
for i in range(int(input())):
    index, pos = list(map(int, input().split()))
    index = index-1
    if index-1 >= 0:
        a[index-1] += (pos-1)
    if index+1 < n:    
        a[index+1] += (a[index]-pos)
    a[index] = 0 


print(*a,sep="\n")    
    
               
