TC = int(input())

for i in range(1, TC+1):
    n = int(input())
    input_list = list(map(int, input().split()))
    ans_list = [0] * 7
    days_list = [0] * 7
    flags = 0
    days = 1
    for j in range(7):
        ans_list[j] = sum(input_list[j:])
        if ans_list[j] >= n:
            flags = j + 1

    if flags:
        count = 0
        for c in range(flags - 1, 7):
            if input_list[c] == 1:
                count += 1
            if count == n:
                break
        print(f"#{i} {count}")
    op = 0
    count = 0
    while not flags:
        for p in range(7):
            if input_list[op % 7] == 1:
                if ans_list[p] < n:
                    ans_list[p] += 1
                    if ans_list[p] == n:
                        days_list[p] = days + (7 - p)
                        count += 1
        if count == 7:
            print(f"#{i} {min(days_list)}")
            break
        days += 1
        op += 1