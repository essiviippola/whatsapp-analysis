from pathlib import Path
import numpy
import pandas as pd
import regex
import emoji
import plotly.express as px
import nltk
from wordcloud import WordCloud
from matplotlib import pyplot as plt
from collections import Counter
from nltk.corpus import stopwords

data_path = Path('../data/whatsapp.txt')