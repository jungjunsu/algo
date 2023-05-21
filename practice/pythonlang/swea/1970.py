T = int(input())
ans_arr = []
price_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def append_list(list, N, price):
    list.append(N // price)
    return N % price

for i in range(1, T+1):
    N = int(input())
    ans_arr = []
    if N < 10 or N > 10**6:
        exit(1)
    elif N % 10 != 0:
        pass
    for index in range(len(price_list)):
        N = append_list(ans_arr, N, price_list[index])
    print(f"#{i}\n{' '.join(map(str, ans_arr))}")