import random

SHIFT_NO_PUNCTUATION = 1

SHIFT_WITH_PUNCTUATION = 2

STEP = 3

MIN_LENGTH_TO_SHUFFLE = 4


def permute(text):
    new_text = ""
    words = text.split(" ")
    for word in words:
        if len(word) < MIN_LENGTH_TO_SHUFFLE:
            new_text += " " + word
            continue
        # getting first and last symbols and intermediate symbols
        first_letter = word[0]
        last_letter = word[len(word) - SHIFT_NO_PUNCTUATION]
        letters = word[SHIFT_NO_PUNCTUATION:len(word) - SHIFT_NO_PUNCTUATION]
        if not last_letter.isalpha():
            # getting new last letters and letters in the middle
            last_letter = word[len(word) - SHIFT_WITH_PUNCTUATION:]
            letters = word[SHIFT_NO_PUNCTUATION:len(word) - SHIFT_WITH_PUNCTUATION]
        i = 0
        # start forming new shuffled word - add first letter
        new_word = first_letter
        while i < len(letters):
            i += STEP
            # it is possible, that middle part, that will be shuffled, will contain less than 3 symbols,
            # so we need to check and handle it
            last_index = len(letters) if i >= len(letters) else i
            part = letters[i - STEP:last_index]
            lst = list(part)
            random.shuffle(lst)
            # adding intermediate shuffled letters
            new_word += ''.join(lst)
        # finally, adding last symbol(s) and adding shuffled word to new text
        new_word += last_letter
        new_text += " " + new_word
    return new_text


print(permute("По результатам исследований одного английского университета, не имеет значения,"
              " в каком порядке расположены буквы в слове."))

