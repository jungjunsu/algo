for i in range(1, 10 + 1):
    N = int(input()) + 4
    N_list = [-1, -1]
    N_list += list(map(int, input().split()))
    N_list += [-1, -1]
    count = 0
    for j in range(2, N - 2):
        for k in range(1, N_list[j] + 1):
            if k > N_list[j-1] and k > N_list[j-2] and k > N_list[j+1] and k > N_list[j+2]:
                count += 1
    print(f"#{i} {count}")