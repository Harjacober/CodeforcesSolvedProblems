def competitions(string):
    if n%2 != 0:
        return -1
    if validBrace(string):
        return 0
    ans,i = 0,0
    while i < n: 
        if not (string[i] == '(' and string[i+1] == ')'):
            ans += 2
        i += 2
    return ans

def validBrace(brace):
    stack = []
    for e in brace:
        if e == '(':
            stack.append(e)
        else:
            if stack:
                stack.pop()
            else:
                return False 
    if stack:
        return False
    return True

n = int(input())
string = input() 
print(competitions(string))  

(()())

((
