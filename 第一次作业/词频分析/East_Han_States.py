# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:07:58 2023

@author: bruno
"""

import jieba as j
import matplotlib.pyplot as plt

text = open('三国演义.txt', encoding='utf-8').read() #打开三国演义文本
print('文本读取完毕，文本长度为', len(text), '字符\n')
words = []
words = j.lcut(text) #对文本进行词语拆分
print('文本拆分完毕，文本词语数量为', len(words), '词\n')#将文本拆分为词语

dic = {'幽州':0,'冀州':0,'并州':0,'兖州':0,'司州':0,'豫州':0,'徐州':0,
               '荆州':0,'青州':0,'扬州':0,'凉州':0,'雍州':0,'益州':0,'交州':0} #生成字典

for word in dic.keys():
        dic[word] = list.count(words, word)#查找文本中各州名数量，并赋值给字典

print('词频分析完毕\n')
print(dic,'\n')
print('数据分析完成，开始制表')


plt.title("三国演义东汉州名词频")
plt.rcParams['font.sans-serif']=['SimHei']#防止中文乱码
x = dic.keys()
y = dic.values()
plt.bar(x,y)
plt.show

print('绘图完成\n')
plt.savefig("./三国演义东汉州名词频.png")
print('图像已保存\n')