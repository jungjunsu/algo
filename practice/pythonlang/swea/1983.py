T = int(input())
score_arr = []
result_arr = ["D0", "C-", "C0", "C+", "B-", "B0", "B+", "A-", "A0", "A+"]

for i in range(1, T+1):
    N, K = list(map(int, input().split()))
    score_arr = []
    index = 0
    comp_val = 0

    if N % 10 or N < 10 or N > 100:
        exit(1)
    if K < 1 or K > N:
        exit(1)
    for j in range(N):
        mid_score, final_score, sub_score = list(map(int, input().split()))
        score_arr.append((35 * mid_score + 45 * final_score + 20 * sub_score))
    comp_val = score_arr[K-1]
    score_arr.sort()
    index = int(score_arr.index(comp_val)/N * 10)
    print(f"#{i} {result_arr[index]}")