# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:32:50 2023

@author: bruno
"""
from pyecharts import options as opts
from pyecharts.charts import Graph

#导入数据
#point计算每个人物出现的次数，link计算人物和其他人物共同出现的次数
point = open('人物出现次数.csv', 'r') 
link = open('人物共同出现次数.csv', 'r')

point_data = point.readlines()
point.close()
del point_data[0]#删除标题

link_data = link.readlines()
link.close()
del link_data[0]

#处理数据
point_graph = []
for line in point_data:
    line = line.strip('\n') #删除换行符号
    line_list = line.split(',') #以“，”为分隔符分割数据，储存在列表中
    point_graph.append(opts.GraphNode(
            name=line_list[0],  #列表第一位是人名，用人名命名图表
            value=int(line_list[1]),  #列表第二位是人名出现次数，
            symbol_size=int(line_list[1])/20))  #图像中点的尺寸据人名出现次数变化

link_graph = []
for line in link_data:
    line = line.strip('\n')
    line_list = line.split(',')
    link_graph.append(opts.GraphLink(
            source=line_list[0], 
            target=line_list[1], 
            value=int(line_list[2])))

#绘制图片
draw = Graph()
draw.add("", 
      point_graph, 
      link_graph, 
      edge_length=[10,50], 
      repulsion=5000,
      layout="force",  # "force"-力引导布局，"circular"-环形布局
      )
draw.set_global_opts(title_opts=opts.TitleOpts(title="蜀汉主要人物共现分析图"))
draw.render('蜀汉主要人物共现分析图.html')
