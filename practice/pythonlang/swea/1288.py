T = int(input())
ans_list = [0] * 10
rep = 1

for i in range(1, T+1):
    N = input()
    ans_list = [0] * 10
    rep = 1
    if int(N)< 0 or int(N) > 1000000:
        exit(1)
    while sum(ans_list) < 10:
        for n in str(int(N) * rep):
            ans_list[int(n)] = 1
        rep += 1

    print(f"#{i} {str(int(N) * (rep - 1))}")