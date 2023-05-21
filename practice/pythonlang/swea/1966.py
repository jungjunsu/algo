T = int(input())

for i in range(1, T+1):
    N = int(input())
    if N < 5 or N > 50:
        exit(1)
    N_list = list(map(int, input().split()))
    N_list.sort()
    print(f"#{i} {' '.join(map(str, N_list))}")