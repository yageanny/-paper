import os  ##跟工作路径相关的包
import networkx as nx   ##python中network分析的基础包
import matplotlib.pyplot as plt  ##画图的包
import unicodecsv as csv  ##写入EXCEL文件的包
import numpy as np  ##数据处理包
import pandas as pd  ##数据处理包
import scipy.stats as ss  ## 统计函数的包
from networkx.algorithms import community  ##社区分析的专用函数

guu = nx.Graph()
guu.add_edges_from(
    [
        ('A', 'K'),
        ('A', 'B'),
        ('B', 'K'),
        ('B', 'C'),
        ('C', 'F'),
        ('C', 'E'),
        ('F', 'E'),
        ('F', 'G'),
        ('D', 'E'),
        ('E', 'H'),
        ('E', 'I'),
        ('I', 'J')
    ]
)
guu
nx.draw_networkx(guu)
plt.show()

data=pd.read_csv("example.csv")
data

guu2 = nx.from_pandas_edgelist(data,"from","to")
guu2
nx.draw_networkx(guu2)
plt.show()

pos = nx.spring_layout(guu)  # 使用弹簧布局算法来确定节点位置
nx.draw_networkx(guu, pos=pos)
plt.show()

nx.draw_networkx(guu, pos=pos, with_labels=True)
plt.show()

nx.draw_networkx(guu, pos=pos, with_labels=True, width=2.0)
plt.show()

ER = nx.random_graphs.erdos_renyi_graph(100,0.062)  #生成包含20个节点、以概率0.2连接的随机图
pos = nx.shell_layout(ER)          #定义一个布局，此处采用了shell布局方式
nx.draw(ER,pos,with_labels=False,node_size = 30) 
plt.show()
