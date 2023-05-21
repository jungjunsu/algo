ans_str = ""

for tc in range(1, int(input())+1):
    p, q = list(map(int, input().split()))
    ax, ay = 0, 0
    flags = -1
    for x in range(1, 140 + 1):
        if flags > 0:
            break
        for y in range(1, 141 + 1):
            if (x + y - 1) * (x + y - 2) // 2 + x == p:
                ax += x
                ay += y
                flags += 1
            if (x + y - 1) * (x + y - 2) // 2 + x == q:
                ax += x
                ay += y
                flags += 1
            if flags > 0:
                break
    ans_str += f"#{tc} {(ax + ay - 1) * (ax + ay - 2) // 2 + ax}\n"
print(ans_str.rstrip())
