def square(number):
    if not 1<= number <= 64:
        raise ValueError("square must be between 1 and 64")
        
    return 2 ** (number-1)
  
    


def total():
    number= 0
    for block in range(1,65):
        number += 2 ** (block-1)
    return number    
        
        
        
        
    
