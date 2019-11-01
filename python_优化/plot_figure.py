# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:15:40 2019

@author: 12101
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def plot_figure(eig,mynode,myelement,lw1,lw2,phi,vw):
    fig=plt.figure();
    ax=fig.add_subplot(111, projection=vw);
    # Plot the nodes
    for i in range(len(mynode.num)):
    	# Get node color depending on the presence of mass or not
    	if mynode.Xmass[i]>0 or mynode.Ymass[i]>0 or mynode.Zmass[i]>0:
    		mynode_sz=30;
    		mynode_clr='r';
    		mynode_shp='o';
    	else:
    		mynode_clr='k';
    		mynode_sz=5;
    		mynode_shp='s';
    	ax.scatter(mynode.Xcoord[i]+mynode.Xamp*mynode.Xdisp[i],mynode.Ycoord[i]+mynode.Yamp*mynode.Ydisp[i],\
                mynode.Zcoord[i]+mynode.Zamp*mynode.Zdisp[i],color=mynode_clr,s=mynode_sz,marker=mynode_shp);
    # Plot the elements
    for i in range(len(myelement.num)):
    	# Set up the color of the myelement types
    	if (myelement.typ[i]=='ForceBeamColumn3d'):
    		clr='b';lw=lw1
    	elif (myelement.typ[i]=='ElasticBeam3d'):
    		clr='k';lw=lw2
    	elif (myelement.typ[i]=='ZeroLength'):
    		clr='r';lw=lw1
    	elif (myelement.typ[i]=='CorotTrussSection'):
    		clr='g';lw=lw1
    	elif (myelement.typ[i]=='Truss'):
    		clr='g';lw=lw1
    	elif (myelement.typ[i]=='TwoNodeLink'):
    		clr='m';lw=lw1
    	else: 
    		clr='k';lw=lw1
    	ax.plot([myelement.iXcoord[i],myelement.jXcoord[i]],[myelement.iYcoord[i],\
              myelement.jYcoord[i]],[myelement.iZcoord[i], myelement.jZcoord[i]],\
            linestyle='-',color=clr,linewidth=lw);   
    ax.set_xlabel('X');
    ax.set_ylabel('Y');
    ax.set_zlabel('Z');
    plt.show();    
    
    if eig > 0:
    	for mds in range(eig):
    		fig = plt.figure(str(mds+1))
    		ax = Axes3D(fig)
    		ax.grid(True, linestyle='-.')
    		ax.set_zlabel('Z')
    		plt.xlabel('X-Coordinates')
    		plt.ylabel('Y-Coordinates')		
    		for i in range(len(myelement.typ)):
    			if (myelement.typ[i]=='ForceBeamColumn3d'):
    				clr='b';lw=lw1
    			elif (myelement.typ[i]=='ElasticBeam3d'):
    				clr='k';lw=lw2
    			elif (myelement.typ[i]=='ZeroLength'):
    				clr='r';lw=lw1
    			elif (myelement.typ[i]=='CorotTrussSection'):
    				clr='g';lw=lw1
    			elif (myelement.typ[i]=='Truss'):
    				clr='g';lw=lw1
    			elif (myelement.typ[i]=='TwoNodeLink'):
    				clr='m';lw=lw1
    			else: 
    				clr='k';lw=lw1
    			idi=mynode.num.index(myelement.iNode[i]);
    			idj=mynode.num.index(myelement.jNode[i]);
    			x1 = mynode.Xcoord[idi]+(phi[mds][idi,0])*mynode.Xamp
    			y1 = mynode.Ycoord[idi]+(phi[mds][idi,1])*mynode.Yamp
    			z1 = mynode.Zcoord[idi]+(phi[mds][idi,2])*mynode.Zamp
    			x2 = mynode.Xcoord[idj]+(phi[mds][idj,0])*mynode.Xamp
    			y2 = mynode.Ycoord[idj]+(phi[mds][idj,1])*mynode.Yamp
    			z2 = mynode.Zcoord[idj]+(phi[mds][idj,2])*mynode.Zamp
    #				xmp= np.mean([x1, x2])
    #				ymp= np.mean([y1, y2])
    #				zmp= np.mean([z1, z2])
    			ax.plot([x1,x2],[y1,y2],[z1,z2],'o-',color = clr,linewidth = lw)
    
            # Plot the nodes
    		for i in range(len(mynode.num)):
    			# Get node color depending on the presence of mass or not
    			if mynode.Xmass[i]>0 or mynode.Ymass[i]>0 or mynode.Zmass[i]>0:
    				mynode_sz=30;
    				mynode_clr='r';
    				mynode_shp='o';
    			else:
    				mynode_clr='k';
    				mynode_sz=5;
    				mynode_shp='s';
    			ax.scatter(mynode.Xcoord[i]+(phi[mds][i,0])*mynode.Xamp,mynode.Ycoord[i]+(phi[mds][i,1])*mynode.Yamp,\
                  mynode.Zcoord[i]+(phi[mds][i,2])*mynode.Zamp,color=mynode_clr,s=mynode_sz,marker=mynode_shp);