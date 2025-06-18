import matplotlib.pyplot as plt;
import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from DBConfig import DBConnection

class Testing:

    def detecting(test_file, model):

        ##train_news = pd.read_csv(train_file)
        test_ = pd.read_csv("Datasets//"+test_file)
        test_=test_.dropna() 
        
        testdata=test_['macromoleculeType']
        
        train = pickle.load(open("models//"+model, 'rb'))
        predicted_class = train.predict(test_['sequence'])
        print('start')

        r=Testing.model_assessment(testdata,predicted_class)

        print(r)

        return r

    def model_assessment(y_test, predicted_class):
        l=[]
        
        #Accuracy = (TP + TN) / ALL
        accuracy=((accuracy_score(y_test, predicted_class)))
        accuracy=accuracy*100
        accuracy=round(float(accuracy),2)

        precision = precision_score(y_test, predicted_class, pos_label='', average='weighted')
        precision=precision*100
        precision=round(float(precision),2)

        recall = recall_score(y_test, predicted_class, pos_label='', average='weighted')
        recall=recall*100
        recall=round(float(recall),2)
        



        l=accuracy,precision,recall
        
        return l



    def main(file):
        db = DBConnection.getConnection()
        cursor = db.cursor()
        f=file.replace('.csv','')
        cursor.execute("delete from evaluations where dataset='"+f+"'")
        sql = "insert into evaluations values(%s,%s,%s,%s,%s)"

        d=Testing.detecting(file,'lr.sav')
        values = ("LR", d[0], d[1], d[2], f)
        cursor.execute(sql, values)


        d=Testing.detecting(file,'rf.sav')
        values = ("RF", d[0], d[1], d[2], f)
        cursor.execute(sql, values)
        
        
        d=Testing.detecting(file,'dt.sav')
        values = ("DT", d[0], d[1], d[2], f)
        cursor.execute(sql, values)
        
        
        d=Testing.detecting(file,'nn.sav')
        values = ("NN", d[0], d[1], d[2], f)
        cursor.execute(sql, values)
        
        
        d=Testing.detecting(file,'svm.sav')
        values = ("SVM", d[0], d[1], d[2], f)
        cursor.execute(sql, values)
        
        db.commit()
        
          
    
if __name__ == '__main__':
    Testing.main('Testing2.csv')

    


