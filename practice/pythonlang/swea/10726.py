TC = int(input())

for i in range(1, TC+1):
    N, M = list(map(int, input().split()))
    bin_M = format(M, 'b')
    count = 0
    if N <= len(bin_M):
        for j in range(len(bin_M) - 1, len(bin_M) - N - 1, -1):
            if bin_M[j] == "1":
                count += 1
    if count == N and N <= len(bin_M):
        print(f"#{i} ON")
    else:
        print(f"#{i} OFF")