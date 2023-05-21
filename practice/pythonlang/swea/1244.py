TC = int(input())

for i in range(1, TC+1):
    input_list, count = list(map(int, input().split()))
    input_list = list(str(input_list))
    len_list = len(input_list)
    flags = 1
    for j in range(len_list-1):
        max_i = j + input_list[j:].index(max(input_list[j:]))
        if max_i < len_list - 1 and input_list[max_i] in input_list[max_i + 1:]:
            max_i = max_i + 1 + input_list[max_i + 1:].index(input_list[max_i])
            flags = 0
        if input_list[j] != input_list[max_i]:
            input_list[j], input_list[max_i] = input_list[max_i], input_list[j]
            count -= 1
        if count == 0:
            break
    if count % 2 and flags:
        input_list[-1], input_list[-2] = input_list[-2], input_list[-1]
    print(f"#{i} {''.join(input_list)}")