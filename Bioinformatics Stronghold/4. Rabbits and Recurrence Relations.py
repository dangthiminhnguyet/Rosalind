def rabbit_pair(n,k):
    month = 1
    baby = 1
    young = 0
    adult = 0
    while month < n:
        adult = young + adult 
        young = baby
        baby = adult * k
        total = young + baby + adult
        month = month + 1
    return total
        
        
        
    
