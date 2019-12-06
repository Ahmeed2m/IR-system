import json
import sys
import string, re
from os.path import dirname, abspath, join
import glob


main_path=dirname(dirname(abspath(__file__)))
path_to_json = main_path+"/DataCollection/"
json_pattern = join(path_to_json,'*.json')
file_list = glob.glob(json_pattern)
DataCollection = dict()
stop_words = []


def _loadData():
    global file_list,DataCollection
    for index,file in enumerate(file_list):
        with open(file,'r') as json_file:
            data = json.load(json_file)
            DataCollection[index]=data
    with open('stopwords.txt','r') as input_file:
        file_content = input_file.readlines()
        for line in file_content:
            line = line[:-1]
            stop_words.append(line)
    #print(stop_words)


def _preprocess():
    global DataCollection,stop_words

    for i,doc in DataCollection.items():
        text = doc['text']
        # re.split requires '|' between delimiters and to be escaped properly.
        regexPattern = '|'.join(map(re.escape, string.punctuation+" "))  
        words = re.split(regexPattern,text)
        cleaned_tokens = []
        for i,word in enumerate(words):
            # alpha-numric and not stopword
            if(word.isalnum() and (word.lower() not in stop_words)):
                word = word.lower()
                cleaned_tokens.append(word)
        # print(words)
        doc['toks'] = cleaned_tokens

def _invertedIndex():
    global DataCollection
    inverted_index = {}
    for i,doc in DataCollection.items():
        raw = doc['toks']
        for word in raw:
            if(word not in inverted_index):
                inverted_index[word]=set([i+1])
            else:
                inverted_index[word].add(i+1)
    print(inverted_index)

def _postionalIndex():
    global DataCollection
    postional_index = {}
    for i,doc in DataCollection.items():
        raw = doc['toks']
        for word in raw:
            if(word not in postional_index):
                postional_index[word]={i+1:[]}
            else:
                postional_index[word][i+1]=[]
        for index,word in enumerate(raw):
            postional_index[word][i+1].append(index)

    # print(postional_index)


def main(argv):
    """global mainPath, data
    mainPath  = dirname(dirname(abspath(__file__)))
    if argv[0] == 'load':
        fileName = argv[1]
        data = _loadData(join(mainPath, fileName))"""

if __name__ == "__main__":
    #main(sys.argv[1:])
    _loadData()
    _preprocess()
    _postionalIndex()
    _invertedIndex()