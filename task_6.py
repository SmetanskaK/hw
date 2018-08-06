import math
print("=======================================")
print("Task #6")
print("=======================================")

a = 3.78
b = -1.45
c = 6.9
e = pow(((math.log1p(1 + c)) / -b), 4) + math.fabs(a)
print("Result of (ln(1 + c) / -b)**4 + |a| (a = %f, b =%f, c =%f) is %.2f" % (a, b, c, e))
