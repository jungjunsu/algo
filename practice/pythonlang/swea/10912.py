T = int(input())

for i in range(1, T+1):
    input_str = list(input())
    input_str.sort()
    index = 0
    while index < len(input_str):
        chr = input_str[index]
        count = 0
        for j in range(len(input_str)):
            if input_str[j] == chr:
                count += 1
        if count > 1:
            if count % 2 == 1:
                count -= 1
                index += 1
            while count > 0:
                while count:
                    input_str.remove(chr)
                    count -= 1
        else:
            index += 1
    input_str.sort()
    if len(input_str) == 0:
        print(f"#{i} Good")
    else:
        print(f"#{i} {''.join(input_str)}")