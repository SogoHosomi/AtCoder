n = int(input())
s = input()

def func_abc(n, s):
    for i in range(len(s) - 2):
        if s[i] == "A":
            if s[i+1] == "B":
                if s[i+2] == "C":
                    return i + 1
    return -1            

print(func_abc(n, s))