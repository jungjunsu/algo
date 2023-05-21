T = int(input())

for i in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    ans_list = []
    for e in range(N):
        s = 0
        while s + e < N:
            sum = 0
            for k in range(e):
                sum += N_list[s + k]
            s += 1
            ans_list.append(sum)
    ans_list.sort()
    print(f"#{i} {ans_list[-1]}")