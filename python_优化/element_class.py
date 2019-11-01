# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:56:03 2019

@author: 12101
"""
from node_class import node 
class element(node):
	# Initialise the lists within the class
	typ=[];
	num=[];
	iNode=[];
	jNode=[];
	iXcoord=[];
	iYcoord=[];
	iZcoord=[];
	jXcoord=[];
	jYcoord=[];
	jZcoord=[];

	# Create class method to append new elements
	@classmethod
	def add_element(self,typ,num,iNode,jNode):
		self.typ.append(typ);
		self.num.append(num);
		self.iNode.append(iNode);
		self.jNode.append(jNode);

	# Create class method to identify element co-ordinates
	@classmethod
	def def_ele_coord(self,node):
		for i in range(len(self.num)):
			idi=node.num.index(self.iNode[i]);
			idj=node.num.index(self.jNode[i]);

			self.iXcoord.append(node.Xcoord[idi]+node.Xamp*node.Xdisp[idi]);
			self.iYcoord.append(node.Ycoord[idi]+node.Yamp*node.Ydisp[idi]);
			self.iZcoord.append(node.Zcoord[idi]+node.Zamp*node.Zdisp[idi]);
			self.jXcoord.append(node.Xcoord[idj]+node.Xamp*node.Xdisp[idj]);
			self.jYcoord.append(node.Ycoord[idj]+node.Yamp*node.Ydisp[idj]);
			self.jZcoord.append(node.Zcoord[idj]+node.Zamp*node.Zdisp[idj]);