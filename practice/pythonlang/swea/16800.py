TC = int(input())

def is_root(N):
    i = 0
    while True:
        if i*i >= N:
            break
        i += 1
    return i

for i in range(1, TC+1):
    N = int(input())
    min_v = N + 1
    for j in range(1, is_root(N) + 1):
        if N % j == 0:
            if min_v > (j + N // j):
                min_v = j + N // j
    print(f"#{i} {min_v - 2}")