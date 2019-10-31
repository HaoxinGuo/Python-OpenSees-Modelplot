# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:14:12 2019

@author: 12101
"""
import tkinter as tk
from tkinter import filedialog
import numpy as np
import operator
from functools import reduce
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from node_plot_3Df import node_plot_3Df
from polt_3D_eigen import polt_3D_eigen
from get_ele import get_element

def find_martrix_min_value(data_matrix,row):
    '''
    功能：找到二维矩阵最小值
    data_matrix 矩阵名
    row 列数
    '''
    new_data=[]
    for i in range(len(data_matrix)):
        new_data.append((data_matrix[i][row]))
    return min(new_data)
def find_martrix_max_value(data_matrix,row):
    '''''
    功能：找到二维矩阵最大值
    data_matrix 矩阵名
    row 列数
    '''
    new_data=[]
    for i in range(len(data_matrix)):
        new_data.append((data_matrix[i][row]))
    return max(new_data)

def plot_your_model(Xamp,Yamp,Zamp,eig,vw):
    """
    Xamp:X方向放大系数
    Yamp:Y方向放大系数
    Zamp:Z方向放大系数
    eig:求解的特征值数
    vw:视野方向 3d vx vy vz
    """
    lw1 = 2.0; lw2 = 1.5 #线宽
    ms1 = 0.5; ms2 = 1   #点的大小
    root = tk.Tk()
    root.withdraw()
    #读入model文件
    print("选择model文件")
    file_path = filedialog.askopenfilename()
    # 如果求解模态，则打开另外两个文件
    if eig>0:
        print("选择eigen文件")
        file_path_en = filedialog.askopenfilename()
        print("选择period文件")
        file_path_p = filedialog.askopenfilename()
        # 周期和振型
        with open(file_path_p,'r',encoding = 'utf-8') as f:
            T = f.readlines()#当最后两行为空行时，其中最后一行不读取
        phi = polt_3D_eigen(file_path_en,eig)
    node_list = []
    if eig >0 and (len(node_list)==0):
        phi_mds = []    
    #得到单元信息
    nelms,Typ,elms = get_element(file_path)
    #此函数用来的得到节点的相关信息
    node, coord, disp, mass = node_plot_3Df(file_path)
    
    ## 计算模型的特性
    # 处理质量矩阵
    lmass = len(mass) #质量矩阵的长度
    m = np.array(mass) #矩阵化质量矩阵
    tm = np.diag(np.array(reduce(operator.add, mass))) #对角化质量矩阵
    mtotal = np.sum(np.array(reduce(operator.add, mass))) #计算总质量
    
    #Get the influence vector
    np.seterr(divide='ignore',invalid='ignore')
    temp=m/m; # get the dofs with mass
    # remove nans
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
    
    # 绘图
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.grid(True, linestyle='-.')
    ax.set_zlabel('Z')
    plt.xlabel('X-Coordinates')
    plt.ylabel('Y-Coordinates')
    plt.xlim(find_martrix_min_value(np.array(coord)+ np.array(disp)*Xamp,0)-0.0001,\
            find_martrix_max_value(np.array(coord)+ np.array(disp)*Xamp,0)+0.0001)
    plt.xlim(find_martrix_min_value(np.array(coord)+ np.array(disp)*Xamp,1)-0.0001,\
            find_martrix_max_value(np.array(coord)+ np.array(disp)*Xamp,1)+0.0001)
    ax.set_zlim(find_martrix_min_value(np.array(coord)+ np.array(disp)*Zamp,2)-0.0001,\
                find_martrix_max_value(np.array(coord)+ np.array(disp)*Zamp,2)+0.0001)
    if vw == 'xz':
        elev = 0;azim = 90
    elif vw == 'yz':
        elev = 0;azim = 0
    elif vw == 'xy':
        elev = 90;azim = 90
    elif vw == '3d':
        elev = 30;azim = -140
    ax.view_init(elev=elev,azim=azim)#改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴    
    #ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 1, 1, 1]))
    for i in range(nelms):
        if (Typ[i]=='ForceBeamColumn3d'):
            clr='b';lw=lw1
        elif (Typ[i]=='ElasticBeam3d'):
            clr='k';lw=lw2
        elif (Typ[i]=='ZeroLength'):
            clr='r';lw=lw1
        elif (Typ[i]=='CorotTrussSection'):
            clr='g';lw=lw1
        elif (Typ[i]=='Truss'):
            clr='g';lw=lw1
        elif (Typ[i]=='TwoNodeLink'):
            clr='m';lw=lw1
        else: 
            clr='k';lw=lw1
        k1 = node.index(elms[i][1])  
        k2 = node.index(elms[i][2])     
        x1 = coord[k1][0]+(disp[k1][0])*Xamp
        y1 = coord[k1][1]+(disp[k1][1])*Yamp
        z1 = coord[k1][2]+(disp[k1][2])*Zamp
        x2 = coord[k2][0]+(disp[k2][0])*Xamp
        y2 = coord[k2][1]+(disp[k2][1])*Yamp
        z2 = coord[k2][2]+(disp[k2][2])*Zamp
#        xmp= np.mean([x1, x2])
#        ymp= np.mean([y1, y2])
#        zmp= np.mean([z1, z2])
        ax.plot([x1,x2],[y1,y2],[z1,z2],'o-',color = clr,linewidth = lw)
    mass_bak = np.array(mass)
    for i in range(len(node)):
        if np.sum(mass_bak[i]) == 0:
            clrn='b';msn=ms1
        else:
            if np.sum(mass_bak[i])>0:
                clrn='r';msn=ms2
        ax.scatter(coord[i][0]+(disp[i][0])*Xamp,
                coord[i][1]+(disp[i][1])*Yamp,
                coord[i][2]+(disp[i][2])*Zamp,'o',color = clrn,linewidths=msn)
                
    if eig > 0:
        for mds in range(eig):
            fig = plt.figure(str(mds+1))
            #ax = plt.gca(projection='3d')
            ax = Axes3D(fig)
            ax.grid(True, linestyle='-.')
            ax.set_zlabel('Z')
            plt.xlabel('X-Coordinates')
            plt.ylabel('Y-Coordinates')        
            for i in range(nelms):
                if (Typ[i]=='ForceBeamColumn3d'):
                    clr='b';lw=lw1
                elif (Typ[i]=='ElasticBeam3d'):
                    clr='k';lw=lw2
                elif (Typ[i]=='ZeroLength'):
                    clr='r';lw=lw1
                elif (Typ[i]=='CorotTrussSection'):
                    clr='g';lw=lw1
                elif (Typ[i]=='Truss'):
                    clr='g';lw=lw1
                elif (Typ[i]=='TwoNodeLink'):
                    clr='m';lw=lw1
                else: 
                    clr='k';lw=lw1
                k1 = node.index(elms[i][1])  
                k2 = node.index(elms[i][2])     
                x1 = coord[k1][0]+(phi[mds][k1,0])*Xamp
                y1 = coord[k1][1]+(phi[mds][k1,1])*Yamp
                z1 = coord[k1][2]+(phi[mds][k1,2])*Zamp
                x2 = coord[k2][0]+(phi[mds][k2,0])*Xamp
                y2 = coord[k2][1]+(phi[mds][k2,1])*Yamp
                z2 = coord[k2][2]+(phi[mds][k2,2])*Zamp
#                xmp= np.mean([x1, x2])
#                ymp= np.mean([y1, y2])
#                zmp= np.mean([z1, z2])
                ax.plot([x1,x2],[y1,y2],[z1,z2],'o-',color = clr,linewidth = lw)
            for i in range(len(node)):
                if np.sum(mass_bak[i]) == 0:
                    clrn='b';msn=ms1
                else:
                    if np.sum(mass_bak[i])>0:
                        clrn='r'; msn=ms2
                ax.scatter(coord[i][0]+(phi[mds][i,0])*Xamp,
                        coord[i][1]+(phi[mds][i,1])*Yamp,
                        coord[i][2]+(phi[mds][i,2])*Zamp,'o',color = clrn,linewidths=msn)
            plt.xlim(find_martrix_min_value((np.array(coord) + [x[0:3] * Xamp for x in phi[mds]]),0)-0.0001,\
                         find_martrix_max_value((np.array(coord) + [x[0:3] * Xamp for x in phi[mds]]),0)+0.0001)
            plt.ylim(find_martrix_min_value((np.array(coord) + [x[0:3] * Yamp for x in phi[mds]]),1)-0.0001,\
                         find_martrix_max_value((np.array(coord) + [x[0:3] * Yamp for x in phi[mds]]),1)+0.0001)
            ax.set_zlim(find_martrix_min_value((np.array(coord) + [x[0:3] * Zamp for x in phi[mds]]),2)-0.0001,\
                            find_martrix_max_value((np.array(coord) + [x[0:3] * Zamp for x in phi[mds]]),2)+0.0001)
            plt.title('model %d T = %1.3f f = %1.3fHz %%M=%.1f'\
                      %(mds+1,float(T[mds]),1/(float(T[mds])),mnstar[mds][0][0]*100))
            if vw == 'xz':
                elev = 0;azim = 90
            elif vw == 'yz':
                elev = 0;azim = 0
            elif vw == 'xy':
                elev = 90;azim = 90
            elif vw == '3d':
                elev = 30;azim = -140
            ax.view_init(elev=elev,azim=azim)#改变绘制图像的视角,即相机的位置,azim沿着z轴旋转，elev沿着y轴
    #        a = find_martrix_min_value((np.array(coord) + [x[0:3] * Xamp for x in phi[mds]]),0)-0.0001
    #        b = find_martrix_max_value((np.array(coord) + [x[0:3] * Xamp for x in phi[mds]]),0)+0.0001
    #        aa = find_martrix_min_value((np.array(coord) + [x[0:3] * Yamp for x in phi[mds]]),1)-0.0001
    #        bb = find_martrix_max_value((np.array(coord) + [x[0:3] * Yamp for x in phi[mds]]),1)+0.0001
    #        aaa = find_martrix_min_value((np.array(coord) + [x[0:3] * Zamp for x in phi[mds]]),2)-0.0001
    #        bbb = find_martrix_max_value((np.array(coord) + [x[0:3] * Zamp for x in phi[mds]]),2)+0.0001
    #        ax.auto_scale_xyz([a,b],[aa,bb],[aaa,bbb])