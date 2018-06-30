from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
import nltk
from nltk import ngrams
from operator import itemgetter



with open('input.txt' , 'r') as inputfile:
    fileread = inputfile.read()

#Sentence tonization and work tokenization
senttokens = nltk.sent_tokenize(fileread)
wordtokens = nltk.word_tokenize(fileread)

#lemmatization on word tokens
print("Lemmatizer \n")
lemmatizer = WordNetLemmatizer()
for l in wordtokens:
    print(lemmatizer.lemmatize(str(l)))

#Applying Bigram on the text
n = 2
gram=[]
bigrams = ngrams(wordtokens, n)
for b in bigrams:
    gram.append(b)
print("Bigram output: \n", gram)

#Top five word frequency")
frequency = nltk.FreqDist(gram)
common = frequency.most_common()
top = sorted(common,key=itemgetter(0))
print("Word frequency: \n",top)

top_five = frequency.most_common(5)
print("top five word frequency :\n",top_five)


#sentences containing the most common words
repeated_sentences = []
for sent in senttokens:
    for word,words in gram:
        for ((c,m), l) in top_five:
            if (word,words == c,m):
                repeated_sentences.append(sent)
print ("Sentence of top five Bigrams \n")
print(max(repeated_sentences,key=len))