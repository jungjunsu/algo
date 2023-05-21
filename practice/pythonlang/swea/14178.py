T = int(input())

for i in range(1, T+1):
    N, D = list(map(int, input().split()))
    count = 0
    while N > 0:
        N -= (2 * D + 1)
        count += 1
    print(f"#{i} {count}")