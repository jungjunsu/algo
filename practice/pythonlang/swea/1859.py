T = int(input())
max_price = 0
N = 0

for i in range(1, T + 1):
    N = int(input())
    price_arr = list(map(int, input().split()))
    max_price = price_arr[-1]
    sum_benefit = 0

    if N < 2 or N > 1000000:
        exit(1)
    for j in range(N-1, 0 - 1, -1):
        if price_arr[j] > 10000:
            exit(1)
        if price_arr[j] > max_price:
            max_price = price_arr[j]
        else:
            sum_benefit += max_price - price_arr[j]
    print(f"#{i} {sum_benefit}")