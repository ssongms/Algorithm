A, B = map(str, input().split())

if A in B:
    print(0)

elif len(A) == len(B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    print(count)

else:
    mismatches = []
    for i in range(len(B)-len(A)+1):
        tempStr = B[:i] + A + B[len(A)+i:]
        count = 0
        for j in range(len(B)):
            if tempStr[j] != B[j]:
                count += 1
        mismatches.append(count)
    print(min(mismatches))