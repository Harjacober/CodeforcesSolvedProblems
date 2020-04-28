arr = "qwertyuiopasdfghjkl;zxcvbnm,./"
dic = {"q":["","w"],"/":[".",""]}
for i in range(1,len(arr)-1):
    dic[arr[i]] = [arr[i-1],arr[i+1]]
shift = input()
word = input()
ans = []
if shift == "L":
    for e in word:
        ans.append(dic[e][1])
else:
    for e in word:
        ans.append(dic[e][0])
print("".join(ans))        
       
    
