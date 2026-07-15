q = int(input())
d1 = q // (10**4)
d2 = (q - d1 * (10**4)) // (10**3)
d3 = (q - d1 * (10**4) - d2 * (10**3)) // (10**2)
d4 = (q - d1 * (10**4) - d2 * (10**3) - d3 * (10**2)) // (10**1)
d5 = q % 10

if (d1 > d2 or d1 == 0) and (d2 > d3 or (d1 == 0 and d2 == 0)) and (d3 > d4 or (d1 == 0 and d2 == 0 and d3 == 0)) and (d4 > d5 or (d1 == 0 and d2 == 0 and d3 == 0 and d4 == 0)):
    print("Yes")
else: 
    print("No")