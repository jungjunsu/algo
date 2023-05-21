T = int(input())

for i in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    n_avr = sum(N_list) / N
    count = 0
    for j in range(N):
        if N_list[j] <= n_avr:
            count += 1
    print(f"#{i} {count}")