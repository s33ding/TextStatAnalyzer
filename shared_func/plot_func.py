import matplotlib.pyplot as plt
import plotly.graph_objects as go


def plot_most_freq_wrds(workdfreq_words):
    fig=go.Figure(go.Bar(x=words_tokens, y=freq_tokens, text=freq_tokens, textposition='outside'))
    fig.update_layout(
        autosize=False,
        width=1000,
        height=500,
        title_text='20 palavras mais utilizadas no relatório')
    fig.update_xaxes(tickangle = -45)
    fig.show( )
