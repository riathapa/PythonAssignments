import math

def compute_quadratic_roots(a, b, c) :
    denominator = 2*a
    numeratorPart1 = (-1) * b
    numeratorPart2 = (b*b) - (4*a*c)
    numeratorPart2 = math.sqrt(numeratorPart2)
    root1 = (numeratorPart1 + numeratorPart2)/denominator
    root2 = (numeratorPart1 - numeratorPart2)/denominator
    print("Roots are :: ", root1, ", ", root2)

a = float(input("Coefficient 1 :: "))
b = float(input("Coefficient 2 :: "))
c = float(input("Coefficient 3 :: "))
compute_quadratic_roots(a,b,c)