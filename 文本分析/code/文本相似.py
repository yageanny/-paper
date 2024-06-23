##加载相关包
import jieba
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.metrics import silhouette_score ,calinski_harabasz_score,davies_bouldin_score
plot_kwds = {'alpha' : 0.7, 's': 40, 'linewidths':0,'cmap':'Set3'}

#导入数据
data=pd.read_excel('D:\wenben\8月12下午 文本分析\data\社研.xls')
data=list(data['Summary-摘要'])

def get_stop_word(stop_word_dir):
    stop_words = []

    with open(stop_words_dir, 'r', encoding='utf-8')as f_reader:
        for line in f_reader:
            line = delete_r_n(line)
            stop_words.append(line)
    
    stop_words = set(stop_words)
    return stop_words


# 去掉空字符
def delete_r_n(line):
    return line.replace('\r', '').replace('\n', '').strip()