def is_armstrong_number(number):
    number = str(number)
    sum = 0 
    for i in range(0,len(number)):
        sum += int(number[i])**len(number)    
    return int(number) == sum         
        





        
