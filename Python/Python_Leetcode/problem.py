def minAlternations(s):
    n = len(s)
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            if s[i] == '1':
                ans += 1
        else:
            if s[i] == '0':
                ans += 1
    return min(ans, n - ans)


print(minAlternations("0010"))
