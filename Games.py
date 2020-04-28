# O(n^2) solution
arr = []
ans = 0
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
for i in range(len(arr)):
    for j in range(len(arr)):
        if j != i and arr[i][0] == arr[j][1]:
            ans += 1 

print(ans)
# O(N+M) solution
# use a counter to count all the colors of the home outfit
# and another counter to count all the colors of the away outfit
#loop through the first counter and multiply its value by the value of the matching key in the secon counter
 
