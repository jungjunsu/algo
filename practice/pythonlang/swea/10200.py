T = int(input())

for i in range(1, T+1):
    N, A, B = list(map(int, input().split()))
    if A >= B:
        max = B
    else:
        max = A
    if N > A + B:
        min = 0
    else:
        min = A + B - N
    print(f"#{i} {max} {min}")