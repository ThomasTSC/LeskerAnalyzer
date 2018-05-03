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
    
    
    
    def Summary(self):
        
        
        
        
        
        
        
        return
    
    
    def stackImage(self):
        
        os.chdir(self.Lesker_Folder_Path)
    
        for file_name in os.listdir(self.Lesker_Folder_Path):
            if fnmatch.fnmatch(file_name, '* Batch %d' %self.Batch_Number):
                os.chdir('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s' %(file_name))
                for file_name in glob.glob('*-sheet.xlsx'):
                    excel2img.export_img(file_name, "Batch %s.png" %self.Batch_Number, "", "fabSheet!D14:I31")
    
    


    def Plot(self):
        
        return
    
    
    
    def Report(self):
        
        return    
    
    
    
    
    
if __name__ == "__main__":
    
    