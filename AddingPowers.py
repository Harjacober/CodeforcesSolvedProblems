def getComponent(array, k):
    Set = set()
    for each in array:
        if each != 0:
            count = 0
            while each > 1:
                if each % k == 0:
                    each = each//k
                    count += 1
                else:
                    if count in Set:
                        return "NO"
                    else:
                        Set.add(count)
                        each -= 1
            if count in Set:
                return "NO"
            else:
                Set.add(count)
    return "YES"

for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    array = list(map(int, input().split()))
    print(getComponent(array, k))
               
