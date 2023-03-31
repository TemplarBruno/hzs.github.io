# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 17:39:13 2023

@author: bruno
"""

from pyecharts import options as opts
from pyecharts.charts import Map

GDP_data = [('Egypt',3898),('Iraq',4686),('Jordan',4058),
            ('Lebanon',6785),('Saudi Arabia',23186),('Yemen',302),
            ('Syria',925),('Sudan',786),('Somalia',447),
            ('Morocco',3853),('Tunisia',3807),('Kuwait',32150),
            ('Algeria',3700),('United Arab Emirates',43295),('Bahrain',26563),
            ('Qatar',66799),('Oman',19509),('Mauritania',2166),
            ('Libya',5791),('Palestine',3514),('Djibouti',3348),
            ('Comoros',1631)]

c = (
    Map()
    .add("人均GDP", 
         GDP_data,
         maptype="world",
         is_map_symbol_show=False,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2021年联合国统计阿拉伯国家人均GDP"),
        visualmap_opts=opts.VisualMapOpts(max_=66800, is_piecewise=False),
    )
)

c.render('./阿拉伯国家2021年人均GDP.html')