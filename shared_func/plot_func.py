import matplotlib.pyplot as plt
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import pandas as pd


def plot_most_freq_wrds(data):
    words_tokens = [wrd[0] for wrd in data[:20]]
    freq_tokens = [wrd[1] for wrd in data[:20]]
    fig=go.Figure(go.Bar(x=words_tokens, y=freq_tokens, text="MOST FREQUENTED WORDS", textposition='outside'))
    fig.update_layout(
        autosize=False,
        width=1000,
        height=500,
        title_text='20 palavras mais utilizadas no relatório')
    fig.update_xaxes(tickangle = -45)
    fig.show( )
    return fig

def plot_wrd_cloud(data):
    data = " ".join(s for s in data)
    wordcloud = WordCloud(background_color="#f5f5f5").generate(data)

    # mostrar a imagem final
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation='bilinear')

    plt.tight_layout()
    return fig
