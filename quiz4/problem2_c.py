a = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0]
for i in range(2 ** 8):
    rec = 0
    s = format(i, f'0{8}b')
    for j in range(8):
        now = 0
        for k in range(8):
            now += a[j+1+k] * int(s[7-k])
            now %= 2
        if a[j] != now:
            rec = 1
            break
    if rec == 0:
        for i in range (len(s)):
            print(f'C{i}:{s[i]}')
        break