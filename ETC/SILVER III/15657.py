import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = []
arr.sort()
for i in itertools.combinations(arr, M):
    result.append(set(i))

result.sort()

for pair in result:
    for elem in pair:
        print(elem, end=" ")
    print()