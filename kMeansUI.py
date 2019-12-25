"""
Created on Mon Dec 19 13:09:12 2019

@author: jannik wiessler
UI for Kmeans
"""
import sys, os
import wx
import subprocess

class UI(wx.Frame): 
    def __init__(self, parent, title): 
        super(UI, self).__init__(parent, title = title, size = (220, 200)) 
             
        self.InitUI()
        self.Centre() 
        self.Show()     
   
    def InitUI(self): 
        panel = wx.Panel(self)
		
        hbox = wx.BoxSizer(wx.HORIZONTAL)
		
        fgs = wx.FlexGridSizer(5, 2, 10,10)
            
        UI_samples = wx.StaticText(panel, label = "samples") 
        UI_centers = wx.StaticText(panel, label = "initail centers") 
        UI_iters = wx.StaticText(panel, label = "max iterations")
        UI_updates = wx.StaticText(panel, label = "updates/second")
        UI_button1 = wx.Button(panel,label="Run")
        UI_button1.Bind( wx.EVT_BUTTON, self.OnButton1)
        UI_button2 = wx.Button(panel,label="Cancel")
        UI_button2.Bind( wx.EVT_BUTTON, self.OnButton2)

        self.tc1 = wx.SpinCtrl(panel,initial=100,max=9999,min=5) 
        self.tc2 = wx.SpinCtrl(panel,initial=4,max=100,min=1) 
        self.tc3 = wx.SpinCtrl(panel,initial=30,max=9999,min=1)
        self.tc4 = wx.SpinCtrl(panel,initial=5,max=9999,min=1)

        fgs.AddMany([(UI_samples), (self.tc1, 1, wx.EXPAND), (UI_centers),(self.tc2, 1, wx.EXPAND), 
            (UI_iters, 1, wx.EXPAND), (self.tc3, 1, wx.EXPAND), (UI_updates, 1, wx.EXPAND), (self.tc4, 1, wx.EXPAND),
            (UI_button2, 1, wx.EXPAND), (UI_button1, 1, wx.EXPAND)])  
        #fgs.AddGrowableRow(2, 1) 
        #fgs.AddGrowableCol(1, 1)  
        hbox.Add(fgs, proportion = 2, flag = wx.ALL|wx.EXPAND, border = 15) 
        panel.SetSizer(hbox) 
		
    def OnButton1(self,push):
        # get current directory: exe must be in same folder !
        if getattr(sys, 'frozen', False): 
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.abspath(__file__)
            application_path = application_path[0:-(len(os.path.basename(__file__))+1)]
        callStr = 'python '+application_path+'/kMeansEngine.py'
        self.writeSpecs()
        os.popen(callStr)
        
    def OnButton2(self,push):
        print('cancel')  
        self.Close()   

    def writeSpecs(self):
        with open('kMeanSpecs.txt', 'w') as filehandle:
            filehandle.write(
            str(self.tc1.GetValue())+'\n'+
            str(self.tc2.GetValue())+'\n'+
            str(self.tc3.GetValue())+'\n'+
            str(self.tc4.GetValue())
            )    

app = wx.App() 
UI(None, title = 'kMeans specs') 
app.MainLoop()