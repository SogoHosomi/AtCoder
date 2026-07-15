n, m = map(int, input().split())
s = input()
t = input()


def func_pre(n, s, t):
    for i in range(n):
        if s[i] != t[i]:
            return 1
    return 0
    
def func_suf(n, m, s, t):
    for i in range(n):
        if s[i] != t[m - n + i]:
            return 1
    return 0
    
pre = func_pre(n, s, t)
suf = func_suf(n, m, s, t)
print((pre << 1) | suf)