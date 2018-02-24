import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def get_tokens():
    with open("/home/rajni/Downloads/mycorpus.txt") as stem:
        tokens = nltk.word_tokenize(stem.read())
    return tokens


def do_stemming(filtered):
    stemmed = []
    for f in filtered:
        stemmed.append(PorterStemmer().stem(f))

    return stemmed


def remove_stopwords(filtered):
    stop_words = set(stopwords.words('english'))


def do_lemmitizaton(filtered):
    lemma = WordNetLemmatizer()
    lem = []
    for f in filtered:
        lem.append(lemma.lemmatize(f, pos='v'))
        #verbs.append(word.lemmatize())
        #print lem

    return lem


if __name__ == "__main__":
    tokens = get_tokens()
    print("tokens = %s") % (tokens)

    stemmed_tokens = do_stemming(tokens)
    print("stemmed_tokens = %s") % stemmed_tokens

    lemmitise_tokens = do_lemmitizaton(tokens)
    print("lemmitised tokens=") % lemmitise_tokens

    lemma = nltk.WordNetLemmatizer()
    lemmas = [lemma.lemmatize(i) for i in tokens]
    print lemmas
