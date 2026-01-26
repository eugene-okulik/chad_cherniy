text = ("Etiam tincidunt neque erat,"
        " quis molestie enim imperdiet vel."
        " Integer urna nisl, facilisis vitae semper at,"
        " dignissim vitae libero"
        )

new_text = []

for word in text.split():
    if '.' in word:
        id_el = word.index('.')
        dw = word[:id_el:]
        dot_word = dw + 'ing.'
        new_text.append(dot_word)
    elif ',' in word:
        id_el = word.index(',')
        dw = word[:id_el:]
        comma_word = dw + 'ing,'
        new_text.append(comma_word)
    else:
        s_word = word + 'ing'
        new_text.append(s_word)

ing_text = ' '.join(new_text)
print(ing_text)
