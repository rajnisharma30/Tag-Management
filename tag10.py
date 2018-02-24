#Extracting Noun
import nltk
from nltk import word_tokenize, pos_tag

sentence = "At eight o'clock on Thursday film morning word line test best beautiful Ram Aaron design"
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
length = len(tagged) - 1
a = list()
print tagged

for item in tagged:
    if item[1] == 'NN':
      a.append(item[0])
print a
print "********"

nouns = [token for token, pos in pos_tag(word_tokenize(sentence)) if pos.startswith('N')]
print nouns

print "********"
tokens = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(tokens)

length = len(tagged) - 1
print tagged

a = list()

for tpl in tagged:
    if tpl[1] == 'NN':
        a.append(tpl[0])
print a

for i in range(0, length):
    log = (tagged [i][1][0] == 'N')
    if log == True:
        a.append(tagged [i][0])
print a

is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
tokenized = nltk.word_tokenize(sentence)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]

print nouns