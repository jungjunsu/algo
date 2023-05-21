T = int(input())

for i in range(1, T+1):
    palindrome_str = input().strip()
    l_str = len(palindrome_str)
    is_pal = 1
    if l_str < 3 or l_str > 10:
        exit(1)
    for j in range(l_str // 2):
        if palindrome_str[j] != palindrome_str[l_str - 1 - j]:
            is_pal = 0
    print(f"#{i} {is_pal}")