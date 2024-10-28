print("Programa de Don Charly Mercury")
fibunacci = [0, 1]
n = 5
for _ in range(0,n-2):
    fibunacci.append(fibunacci[-1]+fibunacci[-2])
print(fibunacci)