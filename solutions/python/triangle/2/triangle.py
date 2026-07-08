def equilateral(sides):
    sides.sort()
 
    return sides[0] == sides[1] == sides [2] != 0 
    

    


def isosceles(sides):
    sides.sort()
    
    return (sides[0] == sides[1] or sides[1] == sides[2]) and sides[0] + sides[1] >= sides[2]
   


def scalene(sides):
    sides.sort()
    return sides[0] != sides[1] != sides[2] and sides[0] + sides[1] >= sides[2]
    