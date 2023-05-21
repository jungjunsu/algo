TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    N_list = []
    for j in range(N):
        N_list.append(int(input()))
    avg_val = sum(N_list) // N
    mov_val= 0
    for k in range(len(N_list)):
        if N_list[k] > avg_val:
            mov_val += N_list[k] - avg_val
    print(f"#{i} {mov_val}")