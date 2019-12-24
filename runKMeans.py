# date: 2019-12-24
# author: jannik wiessler
# email: jannik.wiessler@googlemail.com
# Info: example with 250 normalized [0 1] datapoints (kMeansX.txt)

from KMeansClass import kMeansClass
import numpy as np 


numOfCalcs = 500
numOfCentInit = 5
loops = 20

# load data
with open('kMeansX.txt', 'r') as filehandle:
    X = np.loadtxt(filehandle)

# create the starting centers
C = [None] * numOfCalcs
for i in range(numOfCalcs):
    C1 = np.random.rand(numOfCentInit,2)
    C[i] = C1

# create the objects
objs = [kMeansClass(X,C[i],loops) for i in range(numOfCalcs)]

# run KMeans and store the resulting centers
finalCs = [None] * numOfCalcs
for i in range(numOfCalcs):
    objs[i].runKMeans()
    finalCs[i] = objs[i].C
    
#for center in finalCs:
#    if center not in finalCs:
#        return False
#return True

finalCsTemp = finalCs
numOfEqualCenters = [1] * numOfCalcs
i = 0
while i < len(finalCsTemp):
    counter = 0
    j = 0
    while j < len(finalCsTemp):
        if (np.array_equal(finalCsTemp[i],finalCsTemp[j])) and (i!=j):
            counter = counter + 1
            finalCsTemp.pop(j) # remove double array if found
        j=j+1  
    numOfEqualCenter = counter      
    i=i+1