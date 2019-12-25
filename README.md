# visualizeKmeans

2019-12-19:
This is the very first shot of a python script to visualize k-means algorithm.

Via terminal one can start:
  - kMeansEngine.py: for a quick launch with default settings (use: pythonw kMeansEngine.py on mac)
  - kMeansUI.py: for running the engine with user defined settings (use: pythonw kMeansUI.py on mac)
  
(As the UI is build on wxPython one need >>pythonw kMeansUI.py<< for starting the UI on mac)
  
  
settings:
 - number of samples, 
 - number of initial (random) centers
 - number of max iterations
 - updates per second
                 
2019-12-25:

Evaluation of statistical impact of random centers start distribution on the final clusters result.

Via terminal one can start:
  - python runKMeans.py (specs to be done in script so far)
