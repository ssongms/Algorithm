N = int(input())

nameList = []
for i in range(N):
    name = input()
    nameList.append(name)

ascList = sorted(nameList)
descList = sorted(nameList, reverse=True)

if nameList == ascList:
    print("INCREASING")

elif nameList == descList:
    print("DECREASING")

else:
    print("NEITHER")