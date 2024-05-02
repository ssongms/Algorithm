n = int(input())
pizza = [0] * 11

for i in range(2, 11):
    pizza[i] = (i//2 * (i-i//2)) + pizza[i//2] + pizza[i-i//2]

print(pizza[n])