
import sys
import os
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB

from sklearn.linear_model import  LogisticRegression

from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline


class Training:

    def train(file, algo):
        


        train_file="Datasets//pdb_data_seq.csv"
        df = pd.read_csv(train_file)
        df=df.dropna()
        df=df.drop_duplicates()
        df=df.iloc[:50000]

        tfidf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)
        pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', algo)])
        
        model=pipeline.fit(df['sequence'], df['macromoleculeType'])
        
        if os.path.exists("models//"+file):
            pass
        else:
            pickle.dump(model, open("models//"+file, 'wb'))

    

    def main(model):
        if model=='rf':
            alg=RandomForestClassifier()
            Training.train('rf.sav', alg)

        if model=='nn':
            alg=MLPClassifier()
            Training.train('nn.sav', alg)

        if model=='lr':
            alg=LogisticRegression()
            Training.train('lr.sav', alg)

        if model=='svm':
            alg=svm.SVC()
            Training.train('svm.sav', alg)

        if model=='dt':
            alg=DecisionTreeClassifier()
            Training.train('nb.sav', alg)





if __name__ == "__main__":

    Training.main('dt')
    
