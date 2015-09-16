def transcription(strand):
    rna = ""
    for c in strand:
        if c == "T":
            rna = rna + "U"
        else:
            rna = rna + c
    return rna
