def get_encode(text):
    table = "abcdefghijklmnopqrstuvwxyz0123456789"
    new_text = ""
    text = text.lower()
    for symbol in text:
        if not table.__contains__(symbol):
            new_text += symbol
            continue
        old_index = table.index(symbol)
        new_index = old_index + 5
        wrapped_index = new_index % len(table)
        new_text += table[wrapped_index]
    return new_text


s = input("Enter your text: ")
print(get_encode(s))
