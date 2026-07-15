a, b = map(int, input().split())
tmp, sum = 1, 1

for _ in range(a):
    tmp *= b
    
for _ in range(b):
    sum *= a
    
sum += tmp
print(sum)