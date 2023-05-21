T = int(input())

def exc_check(p, q, r, s, w):
    if p < 1 or q < 1 or r < 1 or s < 1 or w < 1:
        exit(1)
    if p > 10000 or q > 10000 or r > 10000 or s > 10000 or w > 10000:
        exit(1)

for i in range(1, T+1):
    P, Q, R, S, W = list(map(int, input().split()))
    exc_check(P, Q, R, S, W)
    pay = 0
    if P*W < Q + (W - R) * S * (W > R):
        pay = P * W
    else:
        pay = Q + (W - R) * S * (W > R)
    print(f"#{i} {pay}")