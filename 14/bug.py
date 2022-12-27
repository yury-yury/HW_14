"""
Следующий код определяет функцию add_underscores(), принимающую в качестве аргумента строковый объект
и возвращающую новую строку – копию слова с каждым символом, окруженным подчеркиванием.
Например, add_underscores("python") вернет «_p_y_t_h_o_n_».
"""

def add_underscores(word):
    new_word = "_"
    for i in range(len(word)):
        new_word += word[i] + "_"
    return new_word

phrase = "hello"
print(add_underscores(phrase))
print(add_underscores('python'))