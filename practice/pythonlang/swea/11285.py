import math

TC = int(input())
ans_list = []

for i in range(1, TC+1):
    N = int(input())
    pos = 0
    score = 0
    for j in range(N):
        x, y = list(map(int, input().split()))
        pos = math.sqrt(x**2 + y**2)/20
        if int(pos) > 10:
            continue
        elif int(pos) == pos and pos != 0:
            pos = int(pos) - 1
        else:
            pos = int(pos)
        score += 10 - pos
    ans_list.append(score)
for k in range(len(ans_list)):
    print(f"#{k+1} {ans_list[k]}")