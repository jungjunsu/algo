for i in range(10):
    index = int(input())
    search = input()
    index_list = input()
    count = 0
    pos = 0
    while index_list[pos:].find(search) >= 0:
        if index_list[pos:].find(search) >= 0:
            count += 1
            pos += index_list[pos:].find(search) + len(search) + 1
    print(f"#{index} {count}")