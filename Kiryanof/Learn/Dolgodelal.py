a = [int(n) for n in input().split()]
s = []
n_s = []
a.sort()
if len(a)!=1:
    for i in range(len(a)):
        for j in range(len(a)):
            if (i != j) and (a[i] == a[j]):
                s.append(a[i])
    for i in range(len(s)):
        if s[i]!=s[i-1]:
            n_s.append(s[i])
        else:
            continue;

    if len(s) > 1:
        if not len(s) != s.count(s[0]):
            n_s.append(s[0])
        for i in range(len(n_s)):
            print(n_s[i], end=' ')
    else:
        print('')
