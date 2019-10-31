# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:22:03 2019

@author: 12101
"""
import re
def node_plot_3Df(file_path):
    """
    此函数用来的得到节点的相关信息
    Nd 节点数量
    Coord 节点坐标
    Disp 节点初始化位移
    Mass 节点质量
    """
    with open(file_path,'r',encoding = 'utf-8') as f:
        out = f.readlines()#当最后两行为空行时，其中最后一行不读取
    n = len(out)
    Nd=[]; Coord=[]; Disp=[]; Mass=[];
    for i in range(n):
        #匹配节点
        pattern = r" Node"
        matchobj = re.match(pattern,out[i])
        if matchobj:
            Nd.append(int((re.findall(r"\d+\.?\d*",out[i]))[0]))
            #匹配质量，未未配置质量的点加上质量000000
            pattern3 = r"Mass :"
            matchobj3 = re.search(pattern3,out[i+6])
            if matchobj3:
                Mass.append([
                        float((re.findall(r"\d+\.?\d*",out[i+7]))[0]),
                        float((re.findall(r"\d+\.?\d*",out[i+8]))[1]),
                        float((re.findall(r"\d+\.?\d*",out[i+9]))[2]),
                        float((re.findall(r"\d+\.?\d*",out[i+10]))[3]),
                        float((re.findall(r"\d+\.?\d*",out[i+11]))[4]),
                        float((re.findall(r"\d+\.?\d*",out[i+12]))[5])])
            else:
                Mass.append([0,0,0,0,0,0])
        # 匹配坐标
        pattern1 = r"Coordinates"
        matchobj1 = re.search(pattern1,out[i])
        if matchobj1:
            Coord.append([float((re.findall(r"-?\d+\.?-?\d*",out[i]))[0]),
            float((re.findall(r"-?\d+\.?-?\d*",out[i]))[1]),
            float((re.findall(r"-?\d+\.?-?\d*",out[i]))[2])])
        # 匹配初始化位移
        pattern2 = r"Disps:"
        matchobj2 = re.search(pattern2,out[i])
        if matchobj2:
            Disp.append([int((re.findall(r"\d+\.?\d*",out[i]))[0]),
            int((re.findall(r"\d+\.?\d*",out[i]))[1]),
            int((re.findall(r"\d+\.?\d*",out[i]))[2])])      
    return Nd,Coord,Disp,Mass