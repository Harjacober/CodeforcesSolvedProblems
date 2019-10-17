import math
n = int(input())
lis = list(map(int, input().split()))
arr = []
count = 0 
for i in range(1,n-1):
    if lis[i]==0 and lis[i-1]==1 and lis[i+1]==1:
        count += 1
        lis[i+1] = 0
        
print(count)        
      
    
