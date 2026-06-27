def check_character(text, character):
    result = 0
    for char in text:
        if char == character:
            result += 1
    return result


print(check_character('Order of the Phoenix', 'o'))
print(check_character('Test if working something else ', 'e'))