import math
print("=======================================")
print("Task #5")
print("=======================================")

a = 1.97
b = -4.54
c = 4.56
e = math.fabs(a - b) / pow((a + b), 3) - math.cos(c)
print("Result of |a - b| / (a + b)**3 - cos(c) (a = %f, b = %f, c = %f) is %.2f" % (a, b, c, e))
