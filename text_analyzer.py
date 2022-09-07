def num_of_words(text):
    text_lst = text.split(" ")
    return len(text_lst)


def num_of_letters(text):
    count = 0
    for each in text:
        if each.isalpha():
            count += 1
    return count


def num_of_sentences(text):
    text_lst = text.split(".")
    return len(text_lst)


def most_used_letters(text):
    most_used = 0
    letter = ""
    text = text.upper()
    for i in range(ord('A'), ord('Z') + 1):
        if most_used < text.count(chr(i)):
            most_used = text.count(chr(i))
            letter = chr(i)
    if most_used == 1:
        return "0 (there is no letter that is used more than once)"
    return letter, most_used


def the_most_used_word(text):
    most_used = 0
    word = ""
    text_lst = text.split(" ")
    for each in text_lst:
        if most_used < text_lst.count(each):
            most_used = text_lst.count(each)
            word = each
    if most_used == 1:
        return "0 (there is no word that is used more than once)"
    return word, most_used


def text_analyzer(file, new_file):
    with open(file) as f:
        text = f.read()
    words = num_of_words(text)
    letters = num_of_letters(text)
    sentences = num_of_sentences(text)
    most_used_let = most_used_letters(text)
    most_used_word = the_most_used_word(text)
    analyzed_txt = f'Words: {words}\nLetters: {letters}\nSentences: {sentences}\nLetter frequency: {most_used_let[0]}' \
                   f' used {most_used_let[1]} times\nWord frequency: {most_used_word[0]} used {most_used_word[1]} ' \
                   f'times.'
    with open(new_file, "w") as fl:
        fl.write(analyzed_txt)



