def getMax(heights):
    ans = []
    for i in range(len(heights)-1):  
        ans.append(heights[i+1] - heights[i])
    return max(ans)
def minimumDifficulty(heights):
    ans = []
    for i in range(1, len(heights)-1):
        popped = heights.pop(i) 
        ans.append(getMax(heights))
        heights.insert(i, popped)    

    return min(ans)

n = int(input())
heights = list(map(int, input().split()))
print(minimumDifficulty(heights))
