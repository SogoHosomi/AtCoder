q = input()

def judge(q):
    for i in range(8):
        if q[2 * i + 1] == "1":
            return 0
    return 1


if judge(q) == 1:
    print("Yes")
else:
    print("No")