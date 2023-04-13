
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

print("Choice number 1: print tokenized words \n Choice number 2: print tokenized sentences \n Choice number 3: print original text \n Choice number 4: stemming")
a = int(input('choose a number:'))
text = 'information'
ps = PorterStemmer()
words = []
words = text.split()
s_stremmer = SnowballStemmer(language='english')
if a == 1:
    print(word_tokenize(text))
elif a ==2:
    print(sent_tokenize(text))
elif a ==3:
    print(text)
elif a == 4:
    print('Choice 4.1: porter Stemmer \n Choice 4.2: Snowball Stemmer')
    b = int(input('choose a number:'))
    if b ==1:
        for w in words:
         print(w,':', ps.stem(w))
    else:
        for w in words :
         print(w, ':' , s_stremmer.stem(w))
else:
   print('please choose valid No.')