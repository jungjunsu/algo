for _ in range(10):
    tc = int(input())
    tc_list = list(map(int, input().split()))
    while tc_list[-1] > 0:
        for c in range(1, 5 + 1):
            num = tc_list[0] - c
            if num <= 0:
                num = 0
                tc_list.pop(0)
                tc_list.append(num)
                break
            tc_list.pop(0)
            tc_list.append(num)
    print(f"#{tc} {' '.join(map(str, tc_list))}")