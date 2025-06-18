import matplotlib.pyplot as plt;
import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import  accuracy_score, confusion_matrix
import pickle
from sklearn.metrics import  accuracy_score, confusion_matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from DBConfig import DBConnection

class Testing2:

    def detecting(test_file, model):

        ##train_news = pd.read_csv(train_file)
        test_ = pd.read_csv("Datasets//"+test_file)
        test_=test_.dropna() 
        
        testdata=test_['macromoleculeType']

        labels=set(testdata)
        #print(labels)
        train = pickle.load(open("models//"+model, 'rb'))
        res=[]
        for label in labels:
            dct={}

            subset = test_[test_['macromoleculeType'] == label]
            print(len(subset))

            predicted_class = train.predict(subset['sequence'])

            testdata=subset['macromoleculeType']
            

            r=Testing2.model_assessment(testdata,predicted_class)
            print(r,label, len(subset))
            dct['res']=r
            dct['label']=label
            dct['count']=len(subset)

            res.append(dct)
            


            






        
        # train = pickle.load(open("models//"+model, 'rb'))
        # predicted_class = train.predict(test_['sequence'])
        # print('start')

        # r=Testing.model_assessment(testdata,predicted_class)

        # print(r)

        return res

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
        
        cursor.execute("delete from evaluations2 ")
        sql = "insert into evaluations2 values(%s,%s,%s,%s,%s,%s)"

        d=Testing2.detecting(file,'lr.sav')

        for d1 in d:
            res_list=d1['res']
            count=d1['count']
            label=d1['label']

            values = ("LR", res_list[0], res_list[1], res_list[2], label, count)
            cursor.execute(sql, values)


        d=Testing2.detecting(file,'rf.sav')
        for d1 in d:
            res_list=d1['res']
            count=d1['count']
            label=d1['label']

            values = ("RF", res_list[0], res_list[1], res_list[2], label, count)
            cursor.execute(sql, values)

        
        d=Testing2.detecting(file,'dt.sav')
        for d1 in d:
            res_list=d1['res']
            count=d1['count']
            label=d1['label']

            values = ("DT", res_list[0], res_list[1], res_list[2], label, count)
            cursor.execute(sql, values)

        
        d=Testing2.detecting(file,'nn.sav')
        for d1 in d:
            res_list=d1['res']
            count=d1['count']
            label=d1['label']

            values = ("NN", res_list[0], res_list[1], res_list[2], label, count)
            cursor.execute(sql, values)

        
        
        d=Testing2.detecting(file,'svm.sav')
        for d1 in d:
            res_list=d1['res']
            count=d1['count']
            label=d1['label']

            values = ("SVM", res_list[0], res_list[1], res_list[2], label, count)
            cursor.execute(sql, values)

        db.commit()
        
          
    
if __name__ == '__main__':
    Testing2.main('Testset1.csv')

    


