'''

'''
import collections
import os.path
import glob
import nltk

wdict = {}
path = "/home/rajni/Downloads/mycorpus.txt"


#this function cleans up a doc (removes stopwords etc)
def cleanDoc(doc):
    stopset = set(nltk.corpus.stopwords.words('english'))
    stemmer = nltk.PorterStemmer()
    tokens = nltk.WordPunctTokenizer().tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 3 and token.isalpha() and not 'reuter']
    final = [stemmer.stem(word) for word in clean]
    return final

for text in glob.glob(path):
    f = open(text)
    data= f.read()
    words = cleanDoc(data)
    print words
    wdict = set()
    wdict = wdict.update(words)
    print wdict
