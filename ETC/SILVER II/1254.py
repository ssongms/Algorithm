inputStr = input()

for i in range(len(inputStr)):
    if inputStr[i:] == inputStr[i:][::-1]:
        print(len(inputStr)+i)
        break