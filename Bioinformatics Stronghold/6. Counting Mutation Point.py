def hamming(s,t):
    n = hamming = 0
    while n<=len(s) - 1:
        if s[n] != t[n]:
            hamming += 1
        n += 1
    return hamming
