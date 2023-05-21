T = int(input())

for i in range(1, T+1):
    N = int(input())
    N_list = list(map(int, str(N)))
    N_len = len(str(N))
    k = 2
    val = 0
    while len(str(N * k)) == N_len:
        temp_list = list(map(int, str(N*k)))
        temp_n = list(map(int, str(N)))
        for j in range(N_len):
            if temp_list[j] in temp_n:
                temp_n.remove(temp_list[j])
        if len(temp_n) == 0:
            val = 1
            break
        k += 1
    if val == 1:
        print(f"#{i} possible")
    else:
        print(f"#{i} impossible")