def solution(arr, n):
    i = 0
    while i < n:
        j = i+1
        while arr[i] ==  array[j]:
            if j+1<n and arr[i]+1 == array[j+1]:
                arr[i:j] = [arr[i]+1]
            elif i-1 > 0 and arr[i]+1 == array[i-1]:
                arr[j:j+1] = [arr[i]+1]
            j += 1
        i
            

n = int(input())
array = list(map(int, input().split()))
print(solution(array, n))

