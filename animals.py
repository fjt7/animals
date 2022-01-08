# Set 8

def animals(heads,legs):
    if (heads >= legs):
        return None
    for x in range(0, heads + 1):
        if (4*(heads-x)+2*x) == legs:
            return([x, heads - x])
    return None
        
print(animals(5,12))
    
