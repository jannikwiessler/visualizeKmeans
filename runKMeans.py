# date: 2019-12-24
# author: jannik wiessler
# email: jannik.wiessler@googlemail.com
# Info: example with 250 normalized [0 1] datapoints (kMeansX.txt)

from KMeansClass import kMeansClass
import numpy as np 
import matplotlib.pyplot as plt

# specs
numOfCalcs = 2000
numOfCentInit = 3
loops = 20
numOfMostFrequent = 4

# progress bar in terminal
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
             
# load data
with open('kMeansX.txt', 'r') as filehandle:
    X = np.loadtxt(filehandle)

# show the distibution
color = ['blue','maroon','green','cyan','magenta','grey','purple',
    'crimson','darkgreen','saddlebrown']
axs = []
pltData = []
centers = []
fig = plt.figure(figsize=(12, 8), dpi=80, facecolor='w', edgecolor='k')
for i in range(numOfMostFrequent):
    axs.append(fig.add_subplot(2,2,i+1))
    axs[i].axis([-0.05, 1.05, -0.05, 1.05]) 
    pltData.append(plt.scatter(X[:,0],X[:,1],c='black',marker='.'))
plt.pause(0.01)

# create the starting centers
C = [None] * numOfCalcs
for i in range(numOfCalcs):
    C1 = np.random.rand(numOfCentInit,2)
    C[i] = C1

# create the objects
objs = [kMeansClass(X,C[i],loops) for i in range(numOfCalcs)]

#progress bar for sim
printProgressBar(0, numOfCalcs, prefix = 'kMeans:', suffix = 'Complete', length = 50)

# run KMeans and store the resulting centers
finalCs = [None] * numOfCalcs
finalIdx = [None] * numOfCalcs
for i in range(numOfCalcs):
    printProgressBar(i + 1, numOfCalcs, prefix = 'kMeans:', suffix = 'Complete', length = 50)
    objs[i].runKMeans()
    finalCs[i] = objs[i].C
    finalIdx[i] = objs[i].Xout[:,2].astype(int)

# check for final double clusters
#progress bar for sorting
printProgressBar(0, len(finalCs)*0.99, prefix = 'sorting clusters:', suffix = 'Complete', length = 40)
numOfEqualCenters = []
numOfEqualCentersTemp = []
i = 0
while i < len(finalCs):
    printProgressBar(i + 1, len(finalCs)*0.99, prefix = 'sorting clusters:', suffix = 'Complete', length = 40)
    counter = 1
    j = 0
    while j < len(finalCs):
        if (np.array_equal(finalCs[i],finalCs[j])) and (i!=j):
            counter = counter + 1
            finalCs.pop(j) # remove double array if found
            finalIdx.pop(j) # also shorting the idx list to be consistent for plotting the results
            j=j-1 # by removing one we need to check j-th entry again (there is new data now)
        j=j+1  
    numOfEqualCenters.append(counter)
    numOfEqualCentersTemp.append(counter)
    i=i+1
printProgressBar(1, 1, prefix = 'sorting clusters:', suffix = 'Complete', length = 40)   
# draw most frequent cluster
for i in range(numOfMostFrequent):
    colSamples = []
    mostFrequIDX = numOfEqualCentersTemp.index(max(numOfEqualCentersTemp))
    idx = finalIdx[mostFrequIDX]
    for j in range(X.shape[0]):
        colSamples.append(color[idx[j]]) 
    pltData[i].remove() 
    pltData[i] = axs[i].scatter(X[:,0],X[:,1],c=colSamples,marker='.')
    axs[i].set_title(str(i+1)
              +'. most frequent: #equal clusters = '
              +str(numOfEqualCentersTemp[mostFrequIDX])
              +' ('
              +str(round(numOfEqualCentersTemp[mostFrequIDX]*100/numOfCalcs,2))
              +'%)'
              )
    numOfEqualCentersTemp.pop(mostFrequIDX)
    if(numOfEqualCentersTemp==[]):
        break


  


#samplesFig = plt.scatter(X[:,0],X[:,1],c='black',marker='.')
#centersFig = plt.scatter(C[:,0],C[:,1],c=color[0:numOfCentInit],marker='s',edgecolors='black')
plt.pause(0.001) 
plt.show()

 
