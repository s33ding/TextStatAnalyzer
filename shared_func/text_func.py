import re
from collections import Counter

def top_20_words(s):
    s = re.sub(r"/W"," ",s)
    lst = s.split()
    words = lst.Counter()
    freq_words = words.most_common(20)
    return freq_wordss

