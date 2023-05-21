for i in range(10):
    index = int(input())
    N_list = [['' for col in range(100)] for row in range(100)]
    ans_list = []
    for row in range(100):
        N_list[row] = list(map(int, input().split()))
    for row in range(100):
        sum_val = 0
        for col in range(100):
            sum_val += N_list[row][col]
        ans_list.append(sum_val)
    for col in range(100):
        sum_val = 0
        for row in range(100):
            sum_val += N_list[row][col]
        ans_list.append(sum_val)
    sum_val = 0
    for row in range(100):
        sum_val += N_list[row][row]
    ans_list.append(sum_val)
    sum_val = 0
    for row in range(100):
        sum_val += N_list[row][99-row]
    ans_list.append(sum_val)
    print(f"#{index} {max(ans_list)}")