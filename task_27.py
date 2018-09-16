import random


def permute(text):
    new_text = ""
    words = text.split(" ")
    for word in words:
        if len(word) < 4:
            new_text += " " + word
            continue
        # getting first and last symbols and intermediate symbols
        first_letter = word[0]
        last_letter = word[len(word) - 1]
        letters = word[1:len(word) - 1]
        if not last_letter.isalpha():
            # getting new last letters and letters in the middle
            last_letter = word[len(word) - 2:]
            letters = word[1:len(word) - 2]
        i = 0
        # start forming new shuffled word - add first letter
        new_word = first_letter
        while i < len(letters):
            i += 3
            # it is possible, that middle part, that will be shuffled, will contain less than 3 symbols,
            # so we need to check and handle it
            if i >= len(letters):
                part = letters[i - 3:len(letters)]
                lst = list(part)
                random.shuffle(lst)
                # adding intermediate shuffled letters
                new_word += ''.join(lst)
            else:
                part = letters[i - 3:i]
                lst = list(part)
                random.shuffle(lst)
                new_word += ''.join(lst)
        # finally, adding last symbol(s) and adding shuffled word to new text
        new_word += last_letter
        new_text += " " + new_word
    return new_text


print(permute("По результатам исследований одного английского университета, не имеет значения,"
              " в каком порядке расположены буквы в слове."))

