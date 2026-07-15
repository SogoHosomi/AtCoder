with open("rate.txt") as f:
    lines = f.read().split("\n")

d = {}

for line in lines:
    if line.strip() == "":
        continue
    name, rate = line.split()
    d[name] = rate
    
query = input()
print(d[query])