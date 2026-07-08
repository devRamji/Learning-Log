def is_armstrong_number(number):
    number = str(number)
    digits_exponential_sum = 0 
    for placevalue in range(0,len(number)):
        digits_exponential_sum += int(number[placevalue])**len(number)    
    return int(number) == digits_exponential_sum        
        





        
