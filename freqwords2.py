import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import WordNetLemmatizer
from collections import Counter

document_text = open('mycorpus.txt', 'r')
text_string = document_text.read().lower()
word_tokens = word_tokenize(text_string)
frequency = {}
filtered_sentence = []
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])


def do_lemmitizing(filtered_sentence):
    lemma = nltk.WordNetLemmatizer()
    lemmas = []
    for i in filtered_sentence:
        lemmas.append(lemma.lemmatize(i))
    return lemmas


for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

lemmitize_tokens = do_lemmitizing(filtered_sentence)

for word in lemmitize_tokens:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print words, frequency[words]
    if frequency[words]==4:
        print words, frequency[word]

