import json
import sys
import string, re
from os.path import dirname, abspath, join
import glob
# to support relative import 
sys.path.append(dirname(dirname(abspath(__file__))))

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
    
    def intersectPI(self,p1,p2,offset):
        posting = self.postional_index
        posting1 = posting[p1]
        posting2 = posting[p2]
        result = {}
        for key in posting[p1].keys() & posting[p2].keys():
            print("DOC",key)
            print(p1,posting1[key])
            print(p2,posting2[key])
            print("***")
            final = [x for x in posting1[key] for y in posting2[key] if y-x==offset]
            if final != []:
                result[key]= final
        return(result)


    def load_Data(self):
        with open(self.main_path+"/back/postional_index.json","r") as json_file:
            self.postional_index=json.load(json_file)

    def phraseQuery(self,query):
        posting = self.getQueryPosting(query)
        print(posting)
        posting_pairs = [(posting[i],posting[i+1]) for i in range(0,len(posting)-1)]
        final =  []
        for a,b in posting_pairs:
            print(a,b)
            final.append(self.intersectPI(a,b,1))
        print(final)
        finalkeys=final[0].keys()
        for i in range(1,len(final)-1):
            for key in final[i].key():
                if key not in finalkeys:
                    return 0
                


if __name__ == "__main__":
    x = Positional_index()
    x.phraseQuery("apple watch apple")