T = int(input())

for i in range(1, T+1):
    D, L, N = list(map(int, input().split()))
    sum = 0
    for j in range(N):
        damage = D * (1 + j *  L / 100)
        sum += damage

    print(f"#{i} {int(sum)}")