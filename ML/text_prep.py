import pandas as pd
import scipy as sc
import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer


class TextPreproc(object):
    """
    Класс для препроцессинга текста
    """
    def __init__(self, language='russian'):

        self.stopWords = set(stopwords.words(language))
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stemmer = SnowballStemmer(language)

    def standardize_text(self, text):
        """
        Удаляем лишние символы из текста
        """
        text.replace(r"http\S+", "")
        text.replace(r"http", "")
        text.replace(r"@\S+", "")
        text.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")
        text.replace(r"@", "at")
        text.lower()

        return text

    def tokenize_text(self, text):

        token_list = self.tokenizer.tokenize(text)

        return token_list


    def delete_stopw(self, token_list):
        """
        Удаляем стоп-слова из листа после токенизации
        """
        clear_text = []
        for word in token_list:
            if word not in self.stopWords:
                clear_text.append(word)
        return clear_text

    def stemming(self, token_list):
        """
        Просто проходим по токенам
        и аппендим чистые в новый лист
        """
        stemmed_list = []
        for word in token_list:
            stemmed_list.append(self.stemmer.stem(word))
        return stemmed_list


tp = TextPreproc()

def text_preproc(text):
    text = text.replace('\n', '').replace('\r', '')
    text = tp.standardize_text(text)
    text = tp.tokenize_text(text)
    text = tp.delete_stopw(text)
    text = tp.stemming(text)
    text = " ".join(text)
    
    return text