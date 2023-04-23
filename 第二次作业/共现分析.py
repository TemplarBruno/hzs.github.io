# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:13:34 2023

@author: bruno
"""

import jieba as jb
import jieba.posseg as jp

#从文本中导入数据
jb.load_userdict('./userdict.txt') #自定义字典
ignore = [] #设置排除词语
text = open('三国演义.txt', 'r', encoding='utf-8') #打开文件
paragraphs = text.readlines() #每段保存为一个列表元素
text.close()

#将自定义字典里的人物保存为列表dic_names
dic = open('userdict.txt','r',encoding='utf-8')
dic_names =[]
for line in dic:
    dic_names.append(line.split(' ')[0])
dic.close()

#根据文本生成基础数据
name_paragraph = [] #存储每段出现的人物
name_count = {} #计算人物出现数量
for paragraph in paragraphs: # 逐个段落循环处理
    words = jp.cut(paragraph) #对段落进行分词处理，用words将每个词和词性保存起来
    #在列表中，新生成一个子列表，用来储存下一段的数据
    name_paragraph.append([])
    for w in words: #分析words里的每个词
        #w.word 提取出词语内容，返回为一个字符串word
        #w.flag #提取出词语词性，保存在flag中
        if len(w.word) == 1: #单字的词不纳入考虑
            continue
        if w.word in ignore:
            continue
        if w.word == '卧龙' or w.word == '孔明':
            word_set = ('诸葛亮')
        elif w.word == '皇叔' or w.word == '刘皇叔' or w.word == '玄德':
            word_set = '刘备'
        elif w.word == '关公' or w.word == '云长' or w.word == '关某':
            word_set = '关羽'
        elif w.word == '翼德':
            word_set = '张飞'
        elif w.word == '子龙':
            word_set = '赵云'
        if w.flag == 'nr' and w.word in dic_names: #判断词性是否为人名
            name_paragraph[-1].append(word_set)  #将word加入每段出现的人名中
            #[-1]表示保证人名加入的是最新生成的list
            if word_set in name_count.keys(): #计数字典中，该人名数量加1 
                name_count[word_set] = name_count[word_set] + 1
            else:
                name_count[word_set] = 1 #若人名未统计过，将其在计数字典中记为1



print('每段出现人物储存完成\n')

#根据生成数据，统计共现次数
co_occur = {} #用于统计共现次数的字典
for name_set in name_paragraph:
    if len(name_set) == 0:
        continue
    else:
        for name1 in name_set:  # 判断该人物name1是否在字典中
            if name1 in co_occur.keys():
                pass  # 如果已经在字典中，继续后面的统计工作
            else:
                co_occur[name1] = {}  # 把name1加入字典“键”，作为连接的起点
        # 统计name1与本段的所有人名（除了name1自身）的共现数量
            for name2 in name_set:
                if name2 == name1:   # 不统计name1自身
                    continue
            # 检查name1的值列表（即连接的终点）中是否已经有name2
                if name2 in co_occur[name1].keys():
                    co_occur[name1][name2] = co_occur[name1][name2] + 1
                else:
                    co_occur[name1][name2] = 1
print('人物共现次数分析完成\n')

#将统计结果输出为表格文件
output_point = open('人物出现次数.csv', 'w') 
output_point.write('Name,Times\n')
for name,times in name_count.items(): 
    output_point.write(name + ',' + str(times) + '\n')
output_point.close()

output_link = open('人物共同出现次数.csv', 'w')
output_link.write('Object,Subject,Times\n')
for name1,link in co_occur.items():
    for name2,times in link.items():
        output_link.write(name1 + ',' + name2 + ',' + str(times) + '\n')
output_link.close()
print('结果输出完成')

