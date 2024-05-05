bulb = list(input())
result = 0

def switchBulb(n):
    global result
    result += 1
    for i in range(n, len(bulb), n+1):
        if bulb[i] == 'N':
            bulb[i] = 'Y'
        else:
            bulb[i] = 'N'

if bulb.count('Y') == 0: # 전부 N
    print(0)
elif bulb.count('N') == 0: # 전부 Y
    print(1)
else:
    for i in range(len(bulb)):
        if bulb[i] == 'Y':
            switchBulb(i)
    
    print(result)