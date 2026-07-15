import os

if os.path.exists("rate.txt"):
    with open("rate.txt") as f:
        lines = f.read().split("\n")

    d = {}
    for line in lines:
        if line.strip() == "":
            continue
        name, rate = line.split()
        d[name] = int(rate)
else:
    d={
        "tourist"   :3858,
        "ksun48"    :3679,
        "Benq"      :3658,
        "Um_nik"    :3648,
        "apiad"     :3638,
        "Stonefeang":3630,
        "ecnerwala" :3613,
        "mnbvmar"   :3555,
        "newbiedmy" :3516,
        "semiexp"   :3481
    }
    
query = input()
print(d[query])