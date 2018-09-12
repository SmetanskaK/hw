def is_isogram(s):
    b = 0
    for letter in s:
        if " " == letter:
            continue
        b = s.count(letter)
        if b >= 2:
            return False
    return True


k = input("Enter your text: ")
print(is_isogram(k))