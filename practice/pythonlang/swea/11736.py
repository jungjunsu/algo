TC = int(input())

for i in range(1, TC+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    count = 0
    for j in range(1, N-1):
        n1 = N_list[j-1]
        n2 = N_list[j]
        n3 = N_list[j+1]
        max_val = max(n1, n2, n3)
        min_val = min(n1, n2, n3)
        if n2 != max_val and n2 != min_val:
            count += 1
    print(f"#{i} {count}")