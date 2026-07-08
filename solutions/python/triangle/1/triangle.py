def equilateral(sides):
    sides.sort()
 
    return sides[0] == sides[1] == sides [2] != 0 
    

    
    pass


def isosceles(sides):
    sides.sort()
    
    return (sides[0] == sides[1] or sides[1] == sides[2]) and sides[0] + sides[1] >= sides[2]
   
    
    pass


def scalene(sides):
    sides.sort()
    return sides[0] != sides[1] != sides[2] and sides[0] + sides[1] >= sides[2]
    pass
