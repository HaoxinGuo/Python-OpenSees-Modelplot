# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:26:36 2019

@author: 12101
"""
import re
import numpy as np
def polt_3D_eigen(file_path_en,eig):
    if eig > 0:
        with open(file_path_en,'r',encoding = 'utf-8') as f:
            out = f.readlines()#当最后两行为空行时，其中最后一行不读取
    n = len(out)
    
    Nd = []
    Coord = []
    uDisp = []
    eDisp = []
    a = []
    
    for i in range(n):
        pattern = r" Node"
        matchobj = re.match(pattern,out[i])
        if matchobj:
            Nd.append(int((re.findall(r"\d+\.?\d*",out[i]))[0]))
        pattern1 = r"Coordinates"
        matchobj1 = re.search(pattern1,out[i])
        if matchobj1:
            Coord.append([float((re.findall(r"-?\d+\.?-?\d*",out[i]))[0]),
            float((re.findall(r"-?\d+\.?-?\d*",out[i]))[1]),
            float((re.findall(r"-?\d+\.?-?\d*",out[i]))[2])])
    
    for ii in range(eig):
        uDisp_bak = []
        for i in range(n): 
            pattern3 = r"Eigenvectors:"
            matchobj3 = re.search(pattern3,out[i])
            if matchobj3:          
                    uDisp_bak.append([float(out[i+1].split()[ii]),
                    (float(out[i+2].split()[ii])),
                    (float(out[i+3].split()[ii])),
                    (float(out[i+4].split()[ii])),
                    (float(out[i+5].split()[ii])),
                    (float(out[i+6].split()[ii]))])
        a = (np.array(uDisp_bak))
        uDisp.append(a)         
    del uDisp_bak
    
    eDisp = []
    
    for i in range(eig):
        eDisp_bak = []
        q1 = np.max(uDisp[i])
        q2 = np.min(uDisp[i])
        if q1 >= abs(q2):
            eDisp_bak = uDisp[i]/q1
        elif abs(q2) > q1:
            eDisp_bak = uDisp[i]/q2
        eDisp.append(eDisp_bak)
    del eDisp_bak
    return eDisp