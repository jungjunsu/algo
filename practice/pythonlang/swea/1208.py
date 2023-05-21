for i in range(1, 10 + 1):
    d_num = int(input())
    flatten_list = list(map(int, input().split()))
    for j in range(d_num):
        max_i = flatten_list.index(max(flatten_list))
        min_i = flatten_list.index(min(flatten_list))
        flatten_list[min_i], flatten_list[max_i] = flatten_list[min_i] + 1, flatten_list[max_i] - 1
    print(f"#{i} {max(flatten_list) - min(flatten_list)}")