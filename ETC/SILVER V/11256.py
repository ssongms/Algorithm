testcase = int(input())
result = []

for _ in range(testcase):
    candy, box = map(int, input().split())
    boxCapacity = []
    
    for _ in range(box):
        r, c = map(int, input().split())
        boxCapacity.append(r*c)

    boxCapacity.sort(reverse=True) # 내림차순 정렬
    pointer = 0
    while candy > boxCapacity[pointer]:
        candy -= boxCapacity[pointer]
        pointer += 1
    
    result.append(pointer+1)

for i in range(len(result)):
    print(result[i])