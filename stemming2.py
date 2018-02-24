from six import iteritems
from gensim import corpora
# collect statistics about all tokens
stoplist = set('for a of the and to in'.split())
dictionary = corpora.Dictionary(line.lower().split() for line in open('/home/rajni/Downloads/mycorpus.txt'))
# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids)  # remove stop words and words that appear only once
dictionary.compactify()  # remove gaps in id sequence after words that were removed
print(dictionary)

'''
Word lemmatizing is similar to stemming, but the difference is the result of lemmatizing 
is a real word.
'''

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

print (stemmer.stem('increases'))

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print lemmatizer.lemmatize('increases')
