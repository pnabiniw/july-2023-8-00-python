def is_vowel(char):
    if type(char) != str:
        return False
    elif char.isnumeric():
        return False
    return char.lower() in ["a", "e", "i", "o", "u"]


result = is_vowel("2")
print(result)
