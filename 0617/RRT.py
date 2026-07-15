N = int(input())
s = [None] * N
win = [[0 for i in range(2)] for j in range(N)]

def count_win(N):
    for i in range(N):
        s[i] = input()
        win[i][0] = i
        for j in range(N):
            if s[i][j] == "x":
                win[i][1] += 1

def sort_win(N, win):
    # bubble sort
    for j in range(N):
        for i in range(N-1):
            if win[i][1] > win[i + 1][1]:
                tmp = win[i]
                win[i] = win[i + 1]
                win[i + 1] = tmp
    
count_win(N)
sort_win(N, win)

for i in range(N):
    print(win[i][0]+1)