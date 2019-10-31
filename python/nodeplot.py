# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:45:34 2019

@author: 12101
"""
import tkinter as tk
from tkinter import filedialog
import re

print("选择model文件")
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
#读入model文件


def node_plot_3Df(file_path):
    """
    此函数用来的得到节点的相关信息
    """
    with open(file_path,'r',encoding = 'utf-8') as f:
        out = f.readlines()#当最后两行为空行时，其中最后一行不读取
    n = len(out)
    Nd=[];
    Coord=[];
    Disp=[];
    Mass=[];
    
    for i in range(n):
        pattern = r" Node"
        matchobj = re.match(pattern,out[i])
        if matchobj:
            Nd.append(int((re.findall(r"\d+\.?\d*",out[i]))[0]))
        
        pattern1 = r"Coordinates"
        matchobj1 = re.search(pattern1,out[i])
        if matchobj1:
            Coord.append(['Coord',(re.findall(r"\d+\.?\d*",out[i]))[0],
            (re.findall(r"\d+\.?\d*",out[i]))[1],
            (re.findall(r"\d+\.?\d*",out[i]))[2]])
        
        pattern2 = r"Disps:"
        matchobj2 = re.search(pattern2,out[i])
        if matchobj2:
            Disp.append(['Disp',(re.findall(r"\d+\.?\d*",out[i]))[0],
            (re.findall(r"\d+\.?\d*",out[i]))[1],
            (re.findall(r"\d+\.?\d*",out[i]))[2]])
        
        pattern3 = r"Mass :"
        matchobj3 = re.search(pattern3,out[i])
        if matchobj3:
            Mass.append(['Mass',(re.findall(r"\d+\.?\d*",out[i+1]))[0],
            (re.findall(r"\d+\.?\d*",out[i+1]))[1],
            (re.findall(r"\d+\.?\d*",out[i+2]))[2],
            (re.findall(r"\d+\.?\d*",out[i+3]))[3],
            (re.findall(r"\d+\.?\d*",out[i+4]))[4],
            (re.findall(r"\d+\.?\d*",out[i+5]))[5]])
    return Nd,Coord,Disp,Mass

Nd,Coord,Disp,Mass = node_plot_3Df(file_path)