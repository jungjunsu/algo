T = int(input())
ans_str = ""

for i in range(1, T+1):
    N = int(input())
    origin_matrix = [[0 for c in range(N)] for r in range(N)]
    n1_matrix = [[0 for c in range(N)] for r in range(N)]
    n2_matrix = [[0 for c in range(N)] for r in range(N)]
    n3_matrix = [[0 for c in range(N)] for r in range(N)]
    ans_str = ""
    if N < 3 or N > 7:
        exit(1)
    for row in range(N):
        origin_matrix[row] = list(map(int, input().split()))
    for k in range(N):
        n1_matrix[k] = [origin_matrix[r][k] for r in range(N - 1, 0 - 1, -1)]
    for k in range(N):
        n2_matrix[k] = [n1_matrix[r][k] for r in range(N - 1, 0 - 1, -1)]
    for k in range(N):
        n3_matrix[k] = [n2_matrix[r][k] for r in range(N - 1, 0 - 1, -1)]
    for r in range(N):
            ans_str += "".join(map(str, n1_matrix[r]))
            ans_str += " "
            ans_str += "".join(map(str, n2_matrix[r]))
            ans_str += " "
            ans_str += "".join(map(str, n3_matrix[r]))
            ans_str += "\n"
    print(f"#{i}\n{ans_str.rstrip()}")