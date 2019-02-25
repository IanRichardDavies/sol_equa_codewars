import math

def sol_equa(n):
    '''
    Finds all solutions for a specific Diophantine equation
	'''
    solutions = []
    for num in range(1,int(math.sqrt(n))+1):
        if n % num == 0:
            two = n // num
            y = (two - num) // 4
            x = num + 2 * y
            if (x + 2*y == two):
                solutions.append([x,y])
    return solutions