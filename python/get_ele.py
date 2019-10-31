# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:15:22 2019

@author: 12101
"""
import re

def get_element(file_path):
    """
    把单元信息进行汇总,elms = [element,iNd,jNd]
    nelms = 单元长度
    Typ = 单元类型 包括ElasticBeam3d CorotTrussSection TrussSection FlatSliderSimple3d TwoNodeLink 
    ZeroLength ForceBeamColumn3d
    elms = 单元号 i节点 j节点
    """
    with open(file_path,'r',encoding = 'utf-8') as f:
        out = f.readlines()#当最后两行为空行时，其中最后一行不读取
    n = len(out) #读入文件长度
    ## 得到单元信息
    eles=[];ele = [];iNd=[]; #节点i
    jNd=[]; # 节点j
    Typ=[]; #单元类型
    for i in range(n):
        #查找ElasticBeam3d单元
        pattern = r"ElasticBeam3d"
        matchobj = re.match(pattern,out[i])
        if matchobj:
            eles.append([(re.findall(r"\d+\.?\d*",out[i]))[-1],re.findall(r"\d+\.?\d*",out[i+1])])
            Typ.append('ElasticBeam3d')
            #print((re.findall(r"\d+\.?\d*",out[i]))[-1])
        #查找CorotTrussSection单元
        pattern1 = r"CorotTrussSection"
        matchobj1 = re.match(pattern1,out[i])
        if matchobj1:
            eles.append([re.findall(r"\d+\.?\d*",out[i]),re.findall(r"\d+\.?\d*",out[i+1])])
            Typ.append('CorotTrussSection')
        #查找TrussSection单元
        pattern2 = r"TrussSection"
        matchobj2 = re.search(pattern2,out[i])
        if matchobj2:
            eles.append([(re.findall(r"\d+\.?\d*",out[i]))[0],
                         [(re.findall(r"\d+\.?\d*",out[i]))[1],
                         (re.findall(r"\d+\.?\d*",out[i]))[2]]])
            Typ.append('TrussSection')
        #查找FlatSliderSimple3d单元
        pattern3 = r"FlatSliderSimple3d"
        matchobj3 = re.search(pattern3,out[i])
        if matchobj3:
            eles.append([(re.findall(r"\d+\.?\d*",out[i]))[0],
                         [(re.findall(r"\d+\.?\d*",out[i]))[2],
                         (re.findall(r"\d+\.?\d*",out[i]))[3]]])
            Typ.append('FlatSliderSimple3d')     
        #查找TwoNodeLink单元
        pattern4 = r"TwoNodeLink"
        matchobj4 = re.search(pattern4,out[i])
        if matchobj4:
            eles.append([(re.findall(r"\d+\.?\d*",out[i-1]))[0],
                         [(re.findall(r"\d+\.?\d*",out[i+1]))[0],
                         (re.findall(r"\d+\.?\d*",out[i+1]))[1]]])
            Typ.append('TwoNodeLink')  
        #查找ForceBeamColumn3d单元
        patternlast = r"Element"
        matchobjlast = re.match(patternlast,out[i])
        if matchobjlast:
            pattern5 = r"ForceBeamColumn3d"
            matchobj5 = re.search(pattern5,out[i])
            if matchobj5:
                eles.append([(re.findall(r"\d+\.?\d*",out[i]))[0],
                             [(re.findall(r"\d+\.?\d*",out[i]))[2],
                             (re.findall(r"\d+\.?\d*",out[i]))[3]]])
                Typ.append('ForceBeamColumn3d')   
            #查找TrussSection单元
            pattern6 = r"ZeroLength"
            matchobj6 = re.search(pattern6,out[i])
            if matchobj6:
                eles.append([(re.findall(r"\d+\.?\d*",out[i]))[0],
                             [(re.findall(r"\d+\.?\d*",out[i]))[1],
                             (re.findall(r"\d+\.?\d*",out[i]))[2]]])
                Typ.append('ZeroLength')
        pattern7 = r'DispBeamColumn3d'
        matchobj7 = re.match(pattern7,out[i])
        if matchobj7:
            eles.append([(re.findall(r"\d+\.?\d*",out[i]))[1],
                         [(re.findall(r"\d+\.?\d*",out[i+1]))[0],
                         (re.findall(r"\d+\.?\d*",out[i+1]))[1]]])
            Typ.append('DispBeamColumn3d')
    #处理得到的数据
    for _ in eles:
        ele.append(int(_[0]))
        iNd.append(int(_[1][0]))
        jNd.append(int(_[1][1]))
    elms = []
    for node,i,j in zip(ele,iNd,jNd):
        elms.append([node,i,j])
    nelms = len(elms)
    return nelms,Typ,elms