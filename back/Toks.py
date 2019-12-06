import json
import sys
import string, re
from os.path import dirname, abspath, join

data = {}
mainPath = ""

def _loadData(path):
    data = json.loads(open(path).read())
    return data

def _preprocess():
    global data
    for i,doc in enumerate(data):
        text = doc['text']
        # re.split requires '|' between delimiters and to be escaped properly.
        regexPattern = '|'.join(map(re.escape, string.punctuation+" "))  
        words = re.split(regexPattern,text)
        # print(words)
        for i,word in enumerate(words):
            # alpha-numric and not stopword
            if word.isalnum() and (word.lower() not in  ['the', 'of', 'a', 'an']):
                word = word.lower()
                words[i] = word
            else:
                words.remove(word)
        # print(words)
        doc['toks'] = words
    
    print(data)

def _tokenize():
    global data
    toks = []
    for doc in data:
        raw = doc['text']
        
        
def main(argv):
    global mainPath, data
    mainPath  = dirname(dirname(abspath(__file__)))
    if argv[0] == 'load':
        fileName = argv[1]
        data = _loadData(join(mainPath, fileName))

if __name__ == "__main__":
    main(sys.argv[1:])
    _preprocess()
    # _tokenize()