import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


class Prediction:

    def main(data):
        try:

            
            model = 'models/nn.sav'

            filename = model
            train = pickle.load(open(filename, 'rb'))
            print()
            predicted_classs = train.predict(data)
            print(predicted_classs)
            return predicted_classs
        except Exception as e:
            print(e)



if __name__ == "__main__":
    print(Prediction.main(['GUUCUGGGCUGUAGUGCGCUAUGC']))

