# https://www.acmicpc.net/problem/1049

need, brands = map(int, input().split())

packages = []
individual = []
result = 0

for _ in range(brands):
    package, indiv = map(int, input().split())
    packages.append(package)
    individual.append(indiv)

minPackage = min(packages)
minIndividual = min(individual)

if (minPackage >= minIndividual * 6):
    result = minIndividual * need

elif need < 6: 
    result = min(minPackage, minIndividual*need)

else:
    result = min(minPackage * (need // 6) + minIndividual * (need % 6), minPackage * (need // 6 + 1))

print(result)