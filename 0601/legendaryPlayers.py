with open("rate.txt") as f:
    lines = f.read().split("\n")

d = {}
for line in lines:
    if line.strip() == "":
        continue
    name, rating = line.split()
    d[name] = int(rating)

query = input()
print(d[query])