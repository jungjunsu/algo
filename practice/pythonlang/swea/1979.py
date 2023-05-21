T = int(input())
space = 0
count = 0

for i in range(1, T+1):
    N, K = list(map(int, input().split()))
    N_list = [[0 for c in range(N)] for r in range(N)]
    space = 0
    count = 0
    if N < 5 or N > 15:
        exit(1)
    if K < 2 or K > N:
        exit(1)
    for r in range(N):
        N_list[r] = list(map(int, input().split()))
    for r in range(N):
        space = 0
        for c in range(N):
            if N_list[r][c] == 1:
                space += 1
            elif not space == K:
                space = 0
            else:
                count += 1
                space = 0
        if space == K:
            count += 1

    for c in range(N):
        space = 0
        for r in range(N):
            if N_list[r][c] == 1:
                space += 1
            elif not space == K:
                space = 0
            else:
                count += 1
                space = 0
        if space == K:
            count += 1

    print(f"#{i} {count}")