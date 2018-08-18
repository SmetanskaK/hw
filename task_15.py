import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if math.fabs(r1 - r2) <= d <= (r1 + r2):
        return True
    if d > (r1 + r2):
        return False


numb_x1 = float(input("Enter x1:"))
numb_y1 = float(input("Enter y1:"))
numb_x2 = float(input("Enter x2:"))
numb_y2 = float(input("Enter y2:"))
numb_r1 = float(input("Enter the first radius:"))
numb_r2 = float(input("Enter the second radius:"))
print("Res is", circles_intersect(numb_x1, numb_y1, numb_r1, numb_x2, numb_y2, numb_r2))

