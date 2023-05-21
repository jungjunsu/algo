T = int(input())

for tc in range(1, T+1):
    origin_bit = list(map(int, input()))
    count = 0
    bit = 0
    for i in range(len(origin_bit)):
        if origin_bit[i] != bit:
            count += 1
            bit = origin_bit[i]
    print(f"#{tc} {count}")