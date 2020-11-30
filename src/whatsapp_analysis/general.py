import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from urllib.parse import urlparse
from collections import Counter
from nltk.corpus import stopwords
from wordcloud import WordCloud

def group_messages(df, group_by = 'author'):
    df_grouped = df.groupby(group_by).sum()
    df_grouped['pct_of_messages'] = 100 * df_grouped['message_count'] / sum(df_grouped['message_count'])
    df_grouped['non_media_message_count'] = df_grouped['message_count'] - df_grouped['media_count']
    df_grouped['message_with_emoji_pct'] = 100 * df_grouped['message_with_emoji'] / df_grouped['message_count']
    df_grouped['message_with_link_pct'] = 100 * df_grouped['message_with_link'] / df_grouped['message_count']
    df_grouped['message_with_media_pct'] = 100 * df_grouped['media_count'] / df_grouped['message_count']
    df_grouped['emojis_per_message'] = df_grouped['emoji_count'] / df_grouped['message_count']
    df_grouped['emojis_per_word'] = df_grouped['emoji_count'] / df_grouped['word_count']
    df_grouped['words_per_message'] = df_grouped['word_count'] / df_grouped['non_media_message_count']
    df_grouped['letters_per_message'] = df_grouped['letter_count'] / df_grouped['non_media_message_count']
    return(df_grouped)

def print_message_stats(grouped_df):
    print('--- Message Stats ---')
    print('Most messages: ', grouped_df['message_count'].idxmax())
    print('Most emojis: ', grouped_df['message_with_emoji_pct'].idxmax())
    print('Most links: ', grouped_df['message_with_link_pct'].idxmax())
    print('Most media: ', grouped_df['message_with_media_pct'].idxmax())
    print('Shortest messages: ', grouped_df['words_per_message'].idxmin())
    print('Longest messages: ', grouped_df['words_per_message'].idxmax())
    print('Best messages: ESS')

def top_n_emojis(df, n = None):
    total_emojis_list = list([a for b in df.emoji for a in b])
    emoji_dict = dict(Counter(total_emojis_list))
    emoji_dict = sorted(emoji_dict.items(), key = lambda x: x[1], reverse = True)
    emoji_df = pd.DataFrame(emoji_dict, columns = ['emoji', 'count'])
    emoji_df['pct_of_emojis'] = 100 * emoji_df['count'] / emoji_df['count'].sum()
    return(emoji_df.head(n))

def top_n_domains(df, n = None):
    links = list(df['link'].explode())
    domain = [urlparse(link).netloc for link in links[1:]]
    counts = np.unique(domain, return_counts=True)
    counts = pd.DataFrame(np.array(counts).T, columns = ['domain', 'count'])
    counts['count'] = counts['count'].astype('int64')
    counts = counts.sort_values(by = 'count', ascending = False)
    return(counts.head(n))
    