T = int(input())
ans_arr = []

def f_comp(N, x):
    count = 0
    while N % x == 0:
        count += 1
        N //= x
    return str(count)

for i in range(1, T+1):
    N = int(input())
    ans_arr = []
    if N < 2 or N > 10000000:
        exit(1)
    ans_arr.append(f_comp(N, 2))
    ans_arr.append(f_comp(N, 3))
    ans_arr.append(f_comp(N, 5))
    ans_arr.append(f_comp(N, 7))
    ans_arr.append(f_comp(N, 11))
    print("#{} {}".format(i, " ".join(ans_arr)))