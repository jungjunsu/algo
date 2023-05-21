TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    N_list = []
    count = 0
    for j in range(N):
        A, B = list(map(int, input().split()))
        N_list += [A, B]
    for k in range(0,len(N_list),2):
        for p in range(0,len(N_list),2):
            if N_list[k] < N_list[p] and N_list[k+1] > N_list[p+1]:
                count += 1
            elif N_list[k] > N_list[p] and N_list[k + 1] < N_list[p + 1]:
                count += 1
    print(f"#{i} {count//2}")