from pdfplumber_func import *
from pickle_func import *
from plot_func import *
from text_func import *

text = extract_text_from_pdf("data/mitch_albom_-_tuesdays_with_morrie.pdf")
lst_wrds = clean_text(text, language="english")
freq_wrd = top_20_words(lst_wrds)
#plot_most_freq_wrds(data = freq_wrd)
#freq_wrds = biagram(lst_wrds)
#plot_most_freq_wrds(data = freq_wrds)
#plot_wrd_cloud(lst_wrds)
