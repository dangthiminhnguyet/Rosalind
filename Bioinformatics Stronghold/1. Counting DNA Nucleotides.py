def count_nu(str):
    i = 0
    nu_A = 0
    nu_C = 0
    nu_G = 0
    nu_T = 0
    while i<len(str):
        if str[i] == "A":
            nu_A += 1
            i+=1
        elif str[i] == "C":
            nu_C += 1
            i+=1
        elif str[i] == "G":
            nu_G += 1
            i+=1
        else:
            nu_T += 1
            i+=1
        
    print nu_A, nu_C, nu_G, nu_T

    

