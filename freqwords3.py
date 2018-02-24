import string

file = open ( "mycorpus.txt", "r" )
text = file.read ( )
file.close ( )
word_freq ={ }
word_list = string.split ( text )
for word in word_list:
    count = word_freq.get ( string.lower ( word ), 0 )
    word_freq[string. lower ( word )] = count + 1
keys = word_freq.keys ( )
keys.sort ( )
for word in keys:
    print word, word_freq[word]