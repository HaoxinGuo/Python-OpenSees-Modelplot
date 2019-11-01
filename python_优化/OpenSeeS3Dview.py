# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:52:38 2019

@author: 12101
"""

print("Begin")
print("===========================")

# Import some libraries
import json

import tkinter as tk
from tkinter import filedialog

from node_class import node
from element_class import element
from get_phi_fx import get_phi
from plot_figure import plot_figure


# Input variables
# ------------------------------------------------------------------------------------------------
vw='3d';	#	Viewpoint for plotting ('3d', )
Npf=0; 		# 	Node label plot flag (1 for labels, 0 for none)
Epf=0; 		# 	Element label plot flag (1 for labels, 0 for none)
LPpf=1; 	# 	Load pattern plot flag (1 for labels, 0 for none)
eig=7; 		#	number of mode shapes, 0 to do nothing
lw1 = 1
lw2 = 2

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfilename()    

#file = 'mybridge.json'
with open(file) as f:
    d = json.load(f)
nodes = d['StructuralAnalysisModel']['geometry']['nodes']
elements = d['StructuralAnalysisModel']['geometry']['elements']

mynode = node();
for nodee in nodes:
    Xcoord, Ycoord,Zcoord = nodee['crd']
    node_num = nodee['name']
    Xdisp,Ydisp,Zdisp,RXdisp,RYdisp,RZdisp = nodee['Disps']
    Xmass,Ymass,Zmass,RXmass,RYmass,RZmass = nodee['mass']
    mynode.add_node(node_num,Xcoord,Ycoord,Zcoord,Xdisp,Ydisp,Zdisp,RXdisp,RYdisp,RZdisp,\
                    Xmass,Ymass,Zmass,RXmass,RYmass,RZmass);
    del Xdisp,Ydisp,Zdisp,RXdisp,RYdisp,RZdisp,Xmass,Ymass,Zmass,RXmass,RYmass,RZmass,Xcoord, Ycoord,Zcoord,node_num,nodee        
        
myelement = element()
for elementt in elements:
    i, j = elementt['nodes']
    myelement.add_element(elementt['type'],elementt['name'], i, j)
del elementt

#处理单元结点的坐标
myelement.def_ele_coord(mynode); 
if eig >0:
    phi,mnstar = get_phi(eig,nodes,mynode)
else:
    phi = 0;
    mnstar = 0;
    print("eigen=0")

plot_figure(eig,mynode,myelement,lw1,lw2,phi,vw)

print("This is the end of the file")
print("===========================")