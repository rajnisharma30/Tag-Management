import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import WordNetLemmatizer

example_sent = "This is a sample sentence , showing off the stop words filtration !!!!."


def do_stemming(filtered):
    stemmed = []
    for f in filtered:
        stemmed.append(PorterStemmer().stem(f))
    return stemmed

def do_lemmitizing(filtered):
    lemma = nltk.WordNetLemmatizer()
    lemmas = [lemma.lemmatize(i) for i in filtered]
    return lemmas

stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

word_tokens = word_tokenize(example_sent)

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print "After tokenizing the sentence"
print(word_tokens)


print "After removing stop words"
print(filtered_sentence)


print "After steming"
stemmed_tokens = do_stemming(filtered_sentence)
print("stemmed_tokens = %s") % stemmed_tokens

print "After Lemmitizing"
lemmitize_tokens = do_lemmitizing(filtered_sentence)
print("Lemmitized_tokens = %s") % lemmitize_tokens


