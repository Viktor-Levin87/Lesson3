def single_root_words(root_word, *other_words):
    same_words = []
    a = 0
    other_words_l = tuple(map(str.lower, other_words))
    for i in other_words_l:
        if root_word.lower() in i or i in root_word.lower():
            same_words += [other_words[a]]
        a += 1
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
