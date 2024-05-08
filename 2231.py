target = int(input())
result = 0

def digitSum(num):
    strNum = str(num)
    sum = 0
    for i in range(len(strNum)):
        sum += int(strNum[i])
    return sum

for num in range(target, 0, -1):
    if num + digitSum(num) == target:
        result = num
        
print(result)