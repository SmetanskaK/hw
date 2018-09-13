def fib_10():
    box = []
    sum = 0
    for i in range(10):
        if i == 0:
            box.append(1)
            sum = sum + 1
            continue
        if i == 1:
            box.append(1)
            sum = sum + 1
            continue
        i = (box[i - 2]) + (box[i - 1])
        box.append(i)
        sum = sum + int(i)
    print(box)
    return sum


print(fib_10())




