import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))


def nlp_preprocessing(text: str) -> str:
    text: str = text.lower()
    text: str = re.sub(r'd+','', text)
    text: str = text.translate(str.maketrans('','',string.punctuation))
    text: str = text.strip()
    word_tokens: list = word_tokenize(text)
    filtered_text: list = [word for word in word_tokens if word not in stop_words]
    text: str = ' '.join(str(elem) for elem in filtered_text)
    token_text: list = word_tokenize(text)
    for word in token_text:
        lemmatizer.lemmatize(word) 
        stemmer.stem(word)
    return text
