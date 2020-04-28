n = int(input())
s = list(map(int, input().split()))
#using hashtable. makes it suitable for any number of students
dic = dict()
arr = []
for i in range(n):
    if s[i] not in dic:
        dic[s[i]] = [1,[i+1]]
    else:
        dic[s[i]][0] += 1
        dic[s[i]][1].append(i+1)

for key in dic:
    arr.append(dic[key][1])

if len(dic) == 3: 
    print(dic[min(dic, key=lambda x:dic[x][0])][0])    
    for e in (zip(*arr)):
        print(*e, sep=" ")
else:
    print(0)
#using arrays only. this is okay for limited students. say we have 100 students,
#we can't create 100 array variables but the hashtable method will handle such case wee    
one,two,three = [],[],[]
arr = []
for i in range(n):
    if s[i] == 1:
        one.append(i+1)
    elif s[i] == 2:
        two.append(i+1)
    else:
        three.append(i+1)
  
print(min(len(one),len(two),len(three)))    
for e in (zip(one,two,three)):
    print(*e, sep=" ") 
    
