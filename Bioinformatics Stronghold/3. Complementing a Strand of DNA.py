def cdna(dna):
    rc_dna = ""
    for c in dna:
        if c == "A":
            rc_dna += "T"
        elif c == "T":
            rc_dna += "A"
        elif c == "G":
            rc_dna += "C"
        else:
            rc_dna += "G"
    c_dna = ""
    i = len(rc_dna) - 1
    while i>=0:
        c_dna = c_dna + rc_dna[i]
        i = i - 1
    return c_dna
