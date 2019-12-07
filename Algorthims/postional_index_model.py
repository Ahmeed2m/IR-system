import json
import sys
import string, re
from os.path import dirname, abspath, join
import glob
from back import clean
class Positional_index():
    
    def __init__(self,path=dirname(dirname(abspath(__file__)))):
        self.main_path=path
        self.postional_index={}
        self.load_Data()
    def getwordPosting(self,word):
        pass
    def getQueryPosting(self,query):
        query_posting=[]
        query = clean.preprocessQuery(query)
        for word in query:
            query_posting.append(word)
        return query_posting    
    def load_Data(self):
        with open(self.main_path+"/back/postional_index.json","r") as json_file:
            self.postional_index=json.load(json_file)