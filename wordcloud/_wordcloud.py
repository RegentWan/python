#coding=utf-8
import jieba
import wordcloud
from scipy.misc import imread
import matplotlib.pyplot  as plt

# 分词
text=open("gov.txt",'r',encoding='gbk').read()
ls=jieba.lcut(text)
words=" ".join(ls)

# 背景
#mask=imread("China.jpeg")
mask=plt.imread("China.jpeg")

# 词云
wc=wordcloud.WordCloud(font_path="msyh.ttc",width=800,height=600,background_color="white",mask=mask)
wc.generate(words)

#保存文件
wc.to_file("wc.png")

#界面显示
plt.imshow(wc)
plt.axis("off")
plt.show()
