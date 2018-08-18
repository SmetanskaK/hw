def have_trains_crashed(v1, v2):
    if (4 / v1) < (6 / v2):
        return False
    else:
        return True


v3 = int(input("Enter v1:"))
v4 = int(input("Enter v2:"))
if have_trains_crashed(v3, v4):
    print("Crash!!!")
else:
    print("All is ok! Go on!")