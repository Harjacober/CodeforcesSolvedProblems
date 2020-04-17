isPal = []
def printSubsequences(arr, index, subarr): 
    if index == len(arr):  
        if len(subarr) != 0: 
            if len(subarr) >= 3 and subarr == subarr[::-1]: 
                isPal.append(1)
      
    else:  
        printSubsequences(arr, index + 1, subarr)  
        printSubsequences(arr, index + 1,subarr+[arr[index]])  
    return

t = int(input())
for _ in range(t):
    n = int(input())
    string = input().split(' ')
    printSubsequences(string,0,[])
    if isPal:
        print("YES")
    else:
        print("NO")
    isPal = []
    
 
