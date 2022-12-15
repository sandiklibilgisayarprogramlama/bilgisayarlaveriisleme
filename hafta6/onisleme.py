
import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem.porter import *


def convert_lower(input):
    return input.lower()


def remove_punctuation(input):
    for p in punctuation:
        input = input.replace(p, "")
    return input


# stop_words -> cümlelerde sık geçen zamir, bağlaç vs.
# nltk -> natural language processing toolkit
# ingilizce stop words
# ingilizce kök bulma (porter stemmer)
# pip3 install ntlk
# py -m install nltk
# python -m install nltk
# pip install nltk
# import nltk
# nltk.download('stopwords')
# print(stopwords.words('english'))


def remove_stop_words(input):
    input_list = input.split(" ")
    for w in stopwords.words('english'):
        if w in input_list:
            input_list.remove(w)

    return " ".join(input_list)

# iki harf veya tek harf olanlarıda çıkaralım.


def remove_small_length(input):
    input_list = input.split(" ")
    input_list_copy = input_list.copy()
    for kelime in input_list_copy:
        if len(kelime) < 3:
            input_list.remove(kelime)

    return " ".join(input_list)


def find_stems(input):
    stemmer = PorterStemmer()
    input_list = input.split(" ")
    stem_list = []
    for kelime in input_list:
        stem_list.append(stemmer.stem(kelime))

    return " ".join(stem_list)


def find_word_count(etiket_list, message_list):  # [merhaba, naer, nasılsın,]
    from collections import Counter
    spam_word_list = []

    for index in range(len(message_list)):
        if etiket_list[index] == "spam":
            word_list = message_list[index].split(" ")
            spam_word_list.extend(word_list)

    print(Counter(spam_word_list))

"""
george
inform
information
"""
