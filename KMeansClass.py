# date: 2019-12-24
# author: jannik wiessler
# email: jannik.wiessler@googlemail.com
# added automatic reduction of centers if there is no cluster for it

import numpy as np

class kMeansClass():
    def __init__(self,data,centers,maxIter):

        # errorhandling
        if(type(data)!=np.ndarray): # shape is feature of np.dnarray
            print('Error: please pass data as type numpy.dnarray')
            return None
        if(type(centers)!=np.ndarray):
            print('Error: please pass centers as type numpy.dnarray')
            return None
        if(type(maxIter)!=int):
            print('Error: please pass maxIter as type int')
            return None

        # data storage
        self.X = data
        self.C = centers
        self.Cold = self.C
        self.maxIter = maxIter
        self.Xout = np.zeros((self.X.shape[0],2+1))
        self.Cout = np.zeros((self.C.shape[0]*(self.maxIter+1),2))
        self.FLAGG = 0 # flagg for end algorithm
        
    def runKMeans(self):
        numOfCentInit = self.C.shape[0]
        # algorithms loop
        for i in range(self.maxIter):   
            self.Cout[0+i*numOfCentInit:numOfCentInit+i*numOfCentInit,:] = self.C # remember path of centers
            self.calcCluster()
            self.calcCenter()
            if self.FLAGG:
                self.Iters = i
                break
        # set the returnings
        self.Xout[:,0:2] = self.X
        self.Xout[:,2] = self.idx
        self.Cout[0+(i+1)*numOfCentInit:numOfCentInit+(i+1)*numOfCentInit,:] = self.C   

    def calcDist(self,X,C): # L2-Norm
        temp = X-C
        temp = temp*temp
        temp = temp.sum(axis=1)
        temp = np.sqrt(temp) # to be L2 confirm, but not nedded
        return temp

    def avgDist(self,X,Y):
        dist = self.calcDist(X,Y) # dist of every entry is always pos !
        return sum(dist)/self.C.shape[0]

    def calcCluster(self):
        dist = np.zeros((self.X.shape[0],self.C.shape[0]))
        for i in range(self.C.shape[0]): 
            dist[:,i] = self.calcDist(self.X,self.C[i,:])
        self.idx = np.argmin(dist,axis=1)

    def calcCenter(self):
        self.Cold = self.C
        self.C = np.zeros((self.C.shape[0],2))
        for i in range(max(self.idx)+1):
            self.cluster = self.X[(self.idx == i),:]
            if self.cluster.shape[0] != 0:
                self.C[i] = sum(self.cluster)/self.cluster.shape[0]
            else: 
                self.C[i] = -np.ones((1,2)) # [-1 -1] maximise dist of center, so this center will never get a cluster anymore
        averageMove = self.avgDist(self.C,self.Cold) # check if centers are still moving
        if averageMove==0:
            self.FLAGG = 1
 