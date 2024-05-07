import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for i in itertools.permutations(arr, M):
    result.append(i)

result.sort()

# for i in range(len(result)):


for pair in result:
    for elem in pair:
        print(elem, end=" ")
    print()