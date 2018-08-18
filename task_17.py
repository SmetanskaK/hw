import math


def solve_quadratic_equation(a, b, c):
    if b ** 2 - 4 * a * c > 0:
        return (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a), \
               (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

    if (b ** 2) - (4 * a * c) == 0:
        return -b / 2 * a, None
    else:
        return None, None


a1 = int(input("Enter number a:"))
b1 = int(input("Enter number b:"))
c1 = int(input("Enter number c:"))
print("Result: ", solve_quadratic_equation(a1, b1, c1))