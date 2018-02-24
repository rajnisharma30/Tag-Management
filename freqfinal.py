
from collections import Counter
import re


def openfile(filename):
    fh = open(filename, "r+")
    str = fh.read()
    fh.close()
    return str


def removegarbage(str):
    # Replace one or more non-word (non-alphanumeric) chars with a space
    str = re.sub(r'\W+', ' ', str)
    str = str.lower()
    return str


def getwordbins(words):
    cnt = Counter()
    for word in words:
        if len(word)>4:
            cnt[word] += 1
    return cnt


def main(filename, topwords):
    txt = openfile(filename)
    txt = removegarbage(txt)
    words = txt.split(' ')
    bins = getwordbins(words)
    for key, value in bins.most_common(topwords):
        print key, value


main('mycorpus.txt', 50)