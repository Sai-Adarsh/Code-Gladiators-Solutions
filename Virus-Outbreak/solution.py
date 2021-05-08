V = str(input())
N = int(input())

for _ in range(N):
    B = str(input())
    left = 0
    right = 0

    while left < len(V) and right < len(B):
        if V[left] != B[right]:
            left += 1
        else:
            left += 1
            right += 1
    if right == len(B):
        print("POSITIVE")
    else:
        print("NEGATIVE")