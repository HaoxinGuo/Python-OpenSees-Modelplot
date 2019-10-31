# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:22:36 2019

@author: 12101
"""
from plot_your_model import plot_your_model 
eig = 0 # 你要分析的模态数
Xamp = 10 # X轴放大比例
Yamp = 10 # Y轴放大比例
Zamp = 10 # Z轴放大比例
vw = '3d' # 视图类型 包括'xy' 'yz' 'xz' '3d'
plot_your_model(Xamp,Yamp,Zamp,eig,vw)