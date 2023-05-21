T = int(input())

for i in range(1, T+1):
    N, M = list(map(int, input().split()))
    N_list = [[0 for c in range(N)] for r in range(N)]
    fly_sum = 0
    max_sum = 0
    if N < 5 or N > 15:
        exit(1)
    if M < 2 or M > N:
        exit(1)
    for row in range(N):
        N_list[row] = list(map(int, input().split()))
    for k in range(0, N-M + 1):
        for p in range(0, N-M + 1):
            fly_sum = 0
            for l in range(M):
                for m in range(M):
                    if N_list[k+l][p+m] > 30:
                        exit(1)
                    fly_sum += N_list[k+l][p+m]
            if max_sum < fly_sum:
                max_sum = fly_sum
    print(f"#{i} {max_sum}")