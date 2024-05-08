# Not using DP
N = int(input())
if N == 1:
    print("SK")
elif N == 2:
    print("CY")
else:
    r = N % 3
    if r % 2 == 0 or r % 2 == 2:
        print("CY")
    else:
        print("SK")