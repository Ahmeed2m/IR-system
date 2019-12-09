import json
import sys
import string
import re
from os.path import dirname, abspath, join
import pandas as pd
import numpy as np
import glob
# to support relative import
sys.path.append(dirname(dirname(abspath(__file__))))
from back import clean


class VectorSpace():
    def __init__(self):
        self.invertedIndex = {}
        self.positionalIndex = {}
        self.path = dirname(dirname(abspath(__file__)))
        self.df = {}
        self.tf = {}
        self.tfidf = {}
        self.getData()
        self.calculateDF()
        self.calculateTF()
        self.calculateTF_IDF()


    def getData(self):
        with open(self.path+"/back/inverted_index.json", "r") as json_file:
            self.invertedIndex = json.load(json_file)
        with open(self.path+"/back/postional_index.json", "r") as json_file:
            self.positionalIndex = json.load(json_file)
    
    def calculateDF(self):
        for dic,posting in self.invertedIndex.items():
            self.df[dic] = len(posting)
        # print(self.df)
    
    def calculateTF(self):
        keys=set()
        for x in self.positionalIndex.values():
            for y in x.keys():
                keys.add(y)
        cols = sorted(list(keys))
        # construct dataframe from dict with rows names as the keys
        self.tf = pd.DataFrame.from_dict(self.positionalIndex,orient='index')
        x,y = self.tf.shape
        # fil NaNs with zeros
        self.tf = self.tf.fillna(0)
        for i in range(0,x):
            for j in range(0,y):
                if self.tf.iat[i,j] !=0:
                    self.tf.iat[i,j] = len(self.tf.iat[i,j]) 
        # print(self.tf)

    def calculateTF_IDF(self):
        self.tfidf = self.tf
        x,y = self.tfidf.shape
        rows = list(self.tfidf.index)
        for i in range(0,x):
            for j in range(0,y):
                self.tfidf.iat[i,j] = np.log10(1+self.tf.iat[i,j]) * np.log10(y/self.df[rows[i]])
        print(self.tfidf)
        

if __name__ == "__main__":
    x= VectorSpace()
