def sum_symbol_codes(first, last):
    first = ord(first)
    last = ord(last)
    total = 0
    for i in range(first, last + 1):
        total += i
    return total


g = input("Enter your letter: ")
h = input("Enter your letter: ")
k = sum_symbol_codes(g, h)
print("The sum is", k)
