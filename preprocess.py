import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import Text

class Preprocessing:
    def __init__(self):
        pass

    def preprocess(self, inputstr):
        lemmatizer = WordNetLemmatizer()
        inputstr = inputstr.lower()
        token = nltk.word_tokenize(inputstr)
        Stopwords = set(stopwords.words('english'))
        token = [i for i in token if i not in Stopwords and i.isalpha()]
        token = [lemmatizer.lemmatize(i) for i in token]
        text = Text(token)
        return text.vocab()

    def preprocessinput(self, inputstr):
        lemmatizer = WordNetLemmatizer()
        inputstr = inputstr.lower()
        token = nltk.word_tokenize(inputstr)
        Stopwords = set(stopwords.words('english'))
        token = [i for i in token if i not in Stopwords and i.isalpha()]
        token = [lemmatizer.lemmatize(i) for i in token]
        return token
