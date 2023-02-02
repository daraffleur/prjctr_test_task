import warnings

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from app.utils import nlp_preprocessing


warnings.filterwarnings("ignore", category=FutureWarning)


class TargetPredictorModel:
    def __init__(self):
        self.train_df = pd.read_csv('app/models/ml/data/train.csv')
        self.tfidf_vectorizer = TfidfVectorizer() 
        self.X_train = None
        self.y_train = None
        self.tfidf_train = None
        self.regression = None
        self.prepare_df()
        self.split_dataset()
        self.fit_transform_train()
        self.fit_regression()
        
    def prepare_df(self):
        self.train_df['prepared_text'] = ""
        for i in range(0, len(self.train_df)):
            self.train_df['prepared_text'][i] = nlp_preprocessing(self.train_df.excerpt[i]) 
    
    def split_dataset(self):
        X = self.train_df.prepared_text
        y = self.train_df.target
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.05, shuffle=False)
        self.X_train = X_train
        self.y_train = y_train
    
    def fit_transform_train(self):
        self.tfidf_train = self.tfidf_vectorizer.fit_transform(self.X_train)
     
    def transform_train(self, X_test):
        return self.tfidf_vectorizer.transform(X_test)
           
    def fit_regression(self):
        self.regression = LinearRegression().fit(self.tfidf_train, self.y_train)
        
    def predict(self, tfidf_test):
        return self.regression.predict(tfidf_test)
   