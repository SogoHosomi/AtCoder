n, m = map(int, input().split())
s = input()
t = input()

#print(n, m, s, t)

def func_pre(n, m ,s, t):
    for i in range(n):
        if s[i] == t[i]:
            if i == n - 1:
                return 0
    return 1
    
def func_suf(n, m, s, t):
    for i in range(n):
        if s[i] == t[m - n + i]:
            if i == n - 1:
                return 0
    return 1
    
pre = func_pre(n, m, s, t)
suf = func_suf(n, m, s, t)
print((pre << 1) | suf)

