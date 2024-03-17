import re
from collections import Counter
import nltk

def top_20_words(s, language="english")
    txt = re.sub(r"/W"," ",s)
    lst_wrds = [s.lower() for s in txt.split()]
    lst_wrds = lst.Counter()
    rmv_stop_wrds(lst_wrds, language)
    freq_words = words.most_common(20)
    return freq_words

def rmv_stop_wrds(s, language):
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words(language)
    tokens_limpos=[]
    for item in tokens:
        if (item not in stopwords) & (len(item) > 2):
            tokens_limpos.append(item)
    return stopwords



