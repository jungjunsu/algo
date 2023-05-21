for _ in range(1, 10 + 1):
    tc = int(input())
    N, M = list(map(int, input().split()))
    print(f"#{tc} {N**M}")