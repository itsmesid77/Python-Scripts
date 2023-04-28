def is_palamdrom(word):
    reverse_word = word[::-1]
    if reverse_word == word:
        return True
    else:
        return False
print(is_palamdrom("naman"))
print(is_palamdrom("horse"))
