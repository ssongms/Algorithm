engName = list(input())
engNameDict = {}
engName.sort()

for i in range(len(engName)):
    if engName[i] not in engNameDict:
        engNameDict[engName[i]] = 1
    else:
        engNameDict[engName[i]] += 1
front = ""
rear = ""

toDelete = []
for eng, count in engNameDict.items():
    if count >= 2:
        if count % 2 == 0: #짝수 개면
            for i in range(count // 2):
                front = front + str(eng)
                rear = str(eng) + rear
            toDelete.append(eng)
        else: #홀수 개면(3,5,7, ... 개)
            for i in range((count-1)//2):
                front = front + str(eng)
                rear = str(eng) + rear
            engNameDict[eng] = 1

for key in toDelete:
    del engNameDict[key]

for eng, count in engNameDict.items():
    if count == 1:
        front += str(eng)


palindrome = list(front + rear)
if palindrome == palindrome[::-1]:
    palindromeStr = "".join(palindrome)
    print(palindromeStr)
else:
    print("I'm Sorry Hansoo")
