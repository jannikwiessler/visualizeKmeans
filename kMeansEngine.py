#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:09:09 2019

@author: jannik wiessler
V1 dirty implementation to visualize Kmeans (unsupervised learning)
"""

import numpy as np
import matplotlib.pyplot as plt

# functions
# ---------
def rmvDataPoints(samples,centers):
    if samples != -1:
        samples.remove()
    if centers != -1:
        centers.remove()

def calcDist(X,C):
#   L_2-Norm
    temp = X-C
    temp = temp*temp
    temp = temp.sum(axis=1)
    temp = np.sqrt(temp) # to be L2 confirm, but not nedded
    return temp
    
def calcCluster(X,C):
    dist = np.zeros((X.shape[0],C.shape[0]))
    for i in range(C.shape[0]): 
        dist[:,i] = calcDist(X,C[i,:])
    idx = np.argmin(dist,axis=1)
    return idx
    
def colCluster(X,C,samplesFig,centersFig):
    idx = calcCluster(X,C)
    colSamples = []
    for i in range(X.shape[0]):
        colSamples.append(color[idx[i]]) 
    rmvDataPoints(samplesFig,centersFig)    
    samples = plt.scatter(X[:,0],X[:,1],c=colSamples,marker='.')
    centers = plt.scatter(C[:,0],C[:,1],c=color[0:numOfCentInit],marker='s',edgecolors='black')  
    plt.pause(pauseTimer)
    return samples, centers, idx

def calcCenter(X,idx):
    center = np.zeros((numOfCentInit,2))
    for i in range(max(idx)+1):
        cluster = X[(idx == i),:]
        center[i] = sum(cluster)/cluster.shape[0]
    return center

def avgDist(C,oldC):
    dist = calcDist(C,oldC) # dist of every entry is always pos !
    return sum(dist)/C.shape[0]
    
def moveCenter(X,C,idx,centersFig):
    FLAGG = 0
    oldC = C #remember old center-values
    C = calcCenter(X,idx)
    for i in range(C.shape[0]):
        plt.plot((oldC[i][0],C[i][0]),(oldC[i][1],C[i][1]),
                 color='grey', marker='', linestyle='dashed',linewidth=1, markersize=0)
    rmvDataPoints(-1,centersFig)
    centers = plt.scatter(C[:,0],C[:,1],c=color[0:numOfCentInit],marker='s',edgecolors='black')
    plt.pause(pauseTimer) 
    averageMove = avgDist(C,oldC)
    if averageMove==0:
        FLAGG = 1
    return centers, C, FLAGG, averageMove
    
    
# main 
# ----
pauseTimer = 0.05
numOfSamples = 10
numOfCentInit = 5
loops = 20
try:
    with open('kMeanSpecs.txt', 'r') as filehandle:
        specs = filehandle.readlines()
    try:
        numOfSamples = int(specs[0])
        numOfCentInit = int(specs[1])
        loops = int(specs[2])
        pauseTimer = 0.5/float(specs[3])
        # (assume zero execute time for code)
        # 1 (update/sec) => pauseTimer = 0.5, as there are 2 plt.pause 
        # ==> pauseTimer = 0.5/(#updates/sec)
    except: pass
except: pass

print('numOfSamples: '+str(numOfSamples)) 
print('numOfCentInit: '+str(numOfCentInit))
print('numOfLoops: '+str(loops))
print('pauseTimer: '+str(pauseTimer))

color = ['blue','maroon','green','cyan','magenta','grey','purple',
    'crimson','darkgreen','saddlebrown']
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.axis([-0.05, 1.05, -0.05, 1.05])    

X = np.random.rand(numOfSamples,2)
C = np.random.rand(numOfCentInit,2)

Xout = np.zeros((X.shape[0],2+1))
Cout = np.zeros((C.shape[0]*(loops+1),2))

samplesFig = plt.scatter(X[:,0],X[:,1],c='black',marker='.')
centersFig = plt.scatter(C[:,0],C[:,1],c=color[0:numOfCentInit],marker='s',edgecolors='black')
plt.pause(1) 

for i in range(loops):   
    Cout[0+i*numOfCentInit:numOfCentInit+i*numOfCentInit,:] = C 
    samplesFig,centersFig,idx = colCluster(X,C,samplesFig,centersFig)
    centersFig,C,returnFLAGG, averageMove = moveCenter(X,C,idx,centersFig)
    plt.title('Iteration: '+str(i)+' | avgCenterMove: '+str(round(averageMove,4)), loc='center')
    plt.pause(0.000001)
    if returnFLAGG:
        break
    
Xout[:,0:2] = X
Xout[:,2] = idx
Cout[0+(i+1)*numOfCentInit:numOfCentInit+(i+1)*numOfCentInit,:] = C
plt.show()

