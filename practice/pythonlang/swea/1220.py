for tc in range(1, 10 + 1):
    tc_len = int(input())
    tc_list = [[0 for _ in range(tc_len)] for _ in range(tc_len)]
    count = 0
    for row in range(tc_len):
        tc_list[row] = list(map(int, input().split()))
    for col in range(tc_len):
        temp_list = []
        index_sn = [-1, -1]
        for row in range(tc_len):
            if tc_list[row][col]:
                if tc_list[row][col] == 2:
                    index_sn[0] = row
                elif index_sn[1] < 0:
                    index_sn[1] = row
        if index_sn[0] * index_sn[1] >= 0:
            for a in range(index_sn[0] - index_sn[1] + 1):
                if tc_list[index_sn[1] + a][col]:
                    temp_list.append(tc_list[index_sn[1] + a][col])
            tg = 1
            for c in range(len(temp_list)):
                if tg % temp_list[c]:
                    count += 1
                tg = temp_list[c] % 2
    print(f"#{tc} {count}")