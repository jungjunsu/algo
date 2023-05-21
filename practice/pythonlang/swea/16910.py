T = int(input())

for i in range(1, T+1):
    N = int(input())
    if N < 1 or N > 1000:
        exit(1)
    count =  0
    for x in range(N, -N - 1, -1):
        for y in range(N, -N - 1, -1):
            if (x**2) + (y**2) <= N**2:
                count += 1
    print(f"#{i} {count}")