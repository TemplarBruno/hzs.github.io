# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:45:40 2023

@author: bruno
"""

from pyecharts import options as opts
from pyecharts.charts import Bar,Timeline
tl = Timeline()

fname_urban = './Urban.txt'
fname_rural = './Rural.txt'
with open(fname_urban,'r',encoding='utf-8') as u:
   ldatas_u = u.readlines()[1:] #跳过第一行表头
with open(fname_rural,'r',encoding='utf-8') as r:
   ldatas_r = r.readlines()[1:]

years = ["{}年".format(i) for i in range(2015, 2022)]#x轴的数据
           
for i in range(0,10):
    line_u = ldatas_u[i].strip('\n').split('\t')#对每行数据进行拆分
    line_r = ldatas_r[i].strip('\n').split('\t')
    data_u = line_u[1:]
    data_r = line_r[1:]
    data_u.reverse()
    data_r.reverse()
    bar = (
            Bar()
            .add_xaxis(years)
            .add_yaxis("城市居民", data_u)
            .add_yaxis("农村居民", data_r)
            .set_global_opts(title_opts=opts.TitleOpts(line_u[0][4:]))
            )
    tl.add(bar, line_u[0][2:])
tl.render('./food_consumption.html')