# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:06:27 2019

@author: 12101
"""
from functools import reduce
import operator
import numpy as np
def get_phi(eig,nodes,mynode):
    uDisp = []
    for ii in range(1,eig+1):
        Eig = [];
        for nodee in nodes:
            Eig.append(nodee['Eigenvectors'][str(ii)])   
        tE = np.array(Eig)
        uDisp.append(tE) 
    del tE,ii,Eig
    phi = []    
    for i in range(eig):
        eDisp_bak = []
        q1 = np.max(uDisp[i])
        q2 = np.min(uDisp[i])
        if q1 >= abs(q2):
            eDisp_bak = uDisp[i]/q1
        elif abs(q2) > q1:
            eDisp_bak = uDisp[i]/q2
        phi.append(eDisp_bak)
    del eDisp_bak,q1,q2
    
    lmass = len(mynode.Xmass)
    mass = []
    for i in range(lmass):
        mass.append([mynode.Xmass[i],mynode.Ymass[i],mynode.Zmass[i],\
                  mynode.RXmass[i],mynode.RYmass[i],mynode.RZmass[i]])
    m = np.array(mass)
    tm = np.diag(np.array(reduce(operator.add, mass))) #对角化质量矩阵
    mtotal = np.sum(np.array(reduce(operator.add, mass))) #计算总质量
    np.seterr(divide='ignore',invalid='ignore')
    temp=m/m; # get the dofs with mass
    where_are_nan = np.isnan(temp)#查找temp矩阵中存在的nan
    temp[where_are_nan] = 0 #把nan替换为0
    r = temp.reshape(lmass*6,1) #重构temp,成为行向量    
    mn = [] #正则化后的质量
    ln = [] #正则化后的模态
    mnstar = [] #计算归一化有效模态质量
    for i in range(eig):
    # Compute the modal mass
        mn_bak = (np.dot(np.dot(phi[i].reshape(1,lmass*6),tm)
        ,phi[i].reshape(lmass*6,1)))
        #    Compute modal participation factor
        ln_bak = (np.dot(np.dot(phi[i].reshape(1,lmass*6),tm),r))
        #   Compute the normalised effective modal mass   
        mnstar_bak = (ln_bak**2/mn_bak/mtotal)
        mn.append(mn_bak)
        ln.append(ln_bak)
        mnstar.append(mnstar_bak)
    return phi,mnstar