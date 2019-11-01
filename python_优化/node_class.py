# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:49:02 2019

@author: 12101
"""

# Define the classes
# ------------------------------------------------------------------------------------------------
class node():
	Xamp=10; # 	Amplification on Xcoord disps
	Yamp=10; # 	Amplification on Ycoord disps
	Zamp=10; # 	Amplification on Zcoord disps
	num=[];
	Xcoord=[];
	Ycoord=[];
	Zcoord=[];
	Xdisp=[];
	Ydisp=[];
	Zdisp=[];
	RXdisp=[];
	RYdisp=[];
	RZdisp=[];
	Xmass=[];
	Ymass=[];
	Zmass=[];
	RXmass=[];
	RYmass=[];
	RZmass=[];
	# Create class method to append new nodes
	@classmethod        
	def add_node(self,num,Xcoord,Ycoord,Zcoord,Xdisp,Ydisp,Zdisp,RXdisp,RYdisp,RZdisp,\
              Xmass,Ymass,Zmass,RXmass,RYmass,RZmass):
		self.num.append(num);
		self.Xcoord.append(Xcoord);
		self.Ycoord.append(Ycoord);
		self.Zcoord.append(Zcoord);
		self.Xdisp.append(Xdisp);
		self.Ydisp.append(Ydisp);
		self.Zdisp.append(Zdisp);
		self.Xmass.append(Xmass);
		self.Ymass.append(Ymass);
		self.Zmass.append(Zmass);
		self.RXdisp.append(RXdisp);
		self.RYdisp.append(RYdisp);
		self.RZdisp.append(RZdisp);
		self.RXmass.append(RXmass);
		self.RYmass.append(RYmass);
		self.RZmass.append(RZmass);
	@classmethod
	def print_node(self):
		for x in self.Xcoord:
			print(str(x))