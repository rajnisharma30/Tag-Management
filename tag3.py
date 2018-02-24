stop_words = nltk.corpus.stopwords.words('english') + [
    '.',
    ',',
    '--',
    '\'s',
    '?',
    ')',
    '(',
    ':',
    '\'',
    '\'re',
    '"',
    '-',
    '}',
    '{',
    ]

for post in blog_data:
    sentences = nltk.tokenize.sent_tokenize(post)
    print sentences
    words = []
    for sentence in sentences:
        for w in nltk.tokenize.word_tokenize(sentence):
            words.append(w.lower())

    fdist = nltk.FreqDist(words)
    print words
****************************************************
import nltk
from nltk import WordNetLemmatizer

lemma = nltk.WordNetLemmatizer()
text = "Women in technology are amazing at coding"
ex = [i.lower() for i in text.split()]

lemmas = [lemma.lemmatize(i) for i in ex]
print lemmas

t1 = "one car many cars"
ex = [i.lower() for i in t1.split()]
lemmas1 = [lemma.lemmatize(i) for i in ex]
print lemmas1
*********************************************************
#working---extracting noun and saving it in a output file
import nltk

essays = u"""today is monday, tuesday, forest, delhi"""
tokens = nltk.word_tokenize(essays)
tagged = nltk.pos_tag(tokens)
nouns = [word for word,pos in tagged \
	if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
downcased = [x.lower() for x in nouns]
joined = " ".join(downcased).encode('utf-8')
into_string = str(nouns)
print into_string

output = open("output.txt", "w")
output.write(joined)
output.close()
**********************************************************
#extracting noun and tagging them with tokens
import nltk
from nltk import word_tokenize, pos_tag

sentence = "At eight o'clock on Thursday film morning word line test best beautiful Ram Aaron design"
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
length = len(tagged) - 1
a = list()
#print tagged
for item in tagged:
    if item[1] == 'NN':
      a.append(item[0])
print a

***********************************************************

