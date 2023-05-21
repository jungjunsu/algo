T = int(input())

for tc in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    N_list = list(map(int, input().split()))
    ans_list = []
    ans = "Possible"
    N_list.sort()
    for i in range(N):
        if ((N_list[i]//M) * K) - 1 * (i+1) < 0:
            ans = "Impossible"
            break
    print(f"#{tc} {ans}")