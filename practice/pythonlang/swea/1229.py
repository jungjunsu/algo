for tc in range(1, 10 + 1):
    N = int(input())
    N_list = list(map(int, input().split()))
    M = int(input())
    M_list = input().split()
    m_len = len(M_list)
    index = 0
    while index < m_len:
        if M_list[index] == "I":
            x = int(M_list[index + 1])
            y = int(M_list[index + 2])
            apppend_list = []
            for i in range(1, y + 1):
                if index + 2 + i < m_len:
                    apppend_list.append(int(M_list[index + 2 + i]))
            for j in range(1, len(apppend_list) + 1):
                N_list.insert(x, apppend_list[-j])
            index += 2+y
        elif M_list[index] == "D":
            x = int(M_list[index + 1])
            y = int(M_list[index + 2])
            for i in range(y):
                N_list.pop(x)
            index += 2
        index += 1
    print(f"#{tc} {' '.join(map(str, N_list[:10]))}")