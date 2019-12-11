import json
import sys
import string
import re
from os.path import dirname, abspath, join
import glob
# to support relative import
sys.path.append(dirname(dirname(abspath(__file__))))
from back import clean


class Positional_index():

    def __init__(self, path=dirname(dirname(abspath(__file__)))):
        self.main_path = path
        self.postional_index = {}
        self.load_Data()

    def getWordPosting(self, word):
        return self.postional_index[word]

    def getQueryPosting(self, query):
        # query_posting = []
        # query = clean.preprocessQuery(query)
        # for word in query:
        #     query_posting.append(word)
        query_posting = clean.preprocessQuery(query)
        return query_posting

    def intersectPI(self, p1, p2, offset):
        posting1 = self.getWordPosting(p1)
        posting2 = self.getWordPosting(p2)
        result = {}
        for key in sorted(posting1.keys() & posting2.keys()):
            #     print("DOC",key)
            #     print(p1,posting1[key])
            #     print(p2,posting2[key])
            #     print("***")
            final = [x for x in posting1[key] for y in posting2[key] if y-x == offset]
            if final != []:
                result[key] = final
        return(result)

    def load_Data(self):
        with open(self.main_path+"/back/postional_index.json", "r") as json_file:
            self.postional_index = json.load(json_file)

    def phraseQuery(self, query):
        posting = self.getQueryPosting(query)
        print(posting)

        # empty Query posting after normalization (single letters etc..)
        if (posting == []):
            return 500
        # expected case
        elif(len(posting) == 1 and posting[0] in self.postional_index.keys()):
            return [key for key in self.postional_index[posting[0]]]
        # word not in the index
        for word in posting:
            if word not in self.postional_index.keys():
                return 500

        posting_pairs = [(posting[i], posting[i+1])
                         for i in range(0, len(posting)-1)]
        final = []
        for a, b in posting_pairs:
            # print(a,b)
            final.append(self.intersectPI(a, b, 1))
        print(final)
        if {} in final:
            return 500
        elif len(final) == 1:
            return [key for key in list(final[0].keys())]
        
        
        l = []

        for key in final[0].keys():
            for i in range(1, len(final)):
                if key not in final[i].keys():
                    break
                else:
                    l.append((key, [(y-x) == 1 for x in final[0][key]
                                    for y in final[i][key]]))
        return [x[0] for x in l]

    def phraseQueryWrapper(self, query):
        """
        phraseQueryWrapper 
        wrapper function to return proper structed to the UI

        Parameters
        ----------
        query : string
            the query to be performed

        Returns
        -------
        dict

        """
        result = self.phraseQuery(query)
        data = clean.getData()
        final = {}
        if result == 500:
            return {"error": "500"}
        for res in result:
            final[res] = data[int(res)-1]
        return final


if __name__ == "__main__":
    x = Positional_index()
    print(x.phraseQuery("google"))
