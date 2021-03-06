'''
Created on 02.05.2018

@author: chou
'''
import reportlab
import os
import operator
import excel2img
import fnmatch
import glob
import File_Handling
import Data
import seaborn
import numpy
import matplotlib.pyplot as plt



class Report:
    '''
    classdocs
    '''


    def __init__(self, Batch_Number):
        '''
        Constructor
        '''
        self.Batch_Number = Batch_Number
        self.Layer_Number = File_Handling.FileHandling(self.Batch_Number).countLayerNumber()
        self.Lesker_Folder_Path = 'P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker'
    
    
    def stackImage(self):
        
        os.chdir(self.Lesker_Folder_Path)
    
        for file_name in os.listdir(self.Lesker_Folder_Path):
            if fnmatch.fnmatch(file_name, '* Batch %d' %self.Batch_Number):
                os.chdir('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s' %(file_name))
                for file_name in glob.glob('*-sheet.xlsx'):
                    excel2img.export_img(file_name, "Batch %s.png" %self.Batch_Number, "", "fabSheet!D14:I31")
    


    def Plot(self):
        
        
        Layer_Data = Data.DataManipulation(self.Batch_Number).classifiedData()
        #print (Layer_Data['Layer_1']['Rate_5'])
        
        Sensor_Info=Data.LayerAnalysis(self.Batch_Number).correspondingSource()
        #print (Sensor_Info['Corresponding_Sensor']['Layer_1_Source'])    
        Time = Data.LayerAnalysis(self.Batch_Number).timeDuration()
     
        
        for Layer_Order in range(self.Layer_Number):   
            
            plt.figure()
            
            for Sensor in (Sensor_Info['Corresponding_Sensor']['Layer_%d_Source' %(Layer_Order+1)] ):
            
                Reg_Plot = seaborn.regplot(x=(Time['Layer_%d' %(Layer_Order+1)]), y=Layer_Data['Layer_%d' %(Layer_Order+1)]['Rate_%d' %(Sensor)])
            
            
            
            
            plt.title('Layer_%d' %(Layer_Order+1) )
            plt.ylabel('Rate (A/s)')
            plt.xlabel('Time (s)')
            #plt.show()
            plt.savefig(File_Handling.FileHandling(self.Batch_Number).getFolderPath()['BatchFolderPath']+"\ "+"Layer_%d" %(Layer_Order+1))
            
            
    
    
    def Report(self):
        
        return    
    
    
    
    
    
if __name__ == "__main__":
    
    Report(691).Plot()
    print('done')
    
    
    
    