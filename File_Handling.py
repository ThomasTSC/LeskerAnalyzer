'''
Created on 27.04.2018

@author: chou
'''


import os
import glob
import fnmatch
import pandas

class FileHandling:
    
    def __init__(self, Batch_Number):
        
        self.Batch_Number = Batch_Number
        self.Lesker_Folder_Path = 'P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker'
        

    def getLogFileList(self):
        
        
        os.chdir(self.Lesker_Folder_Path)
    
        Log_File_List = []

        for file_name in os.listdir(self.Lesker_Folder_Path):
            if fnmatch.fnmatch(file_name, '* Batch %d' %self.Batch_Number):
                Lesker_Batch_Log_File_Path = ('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s\Deposition Log Files' %file_name)
                os.chdir(Lesker_Batch_Log_File_Path)
            
        for file_name in glob.glob('*.csv'):
            Log_File_List.append(file_name)
            
        
        
        #print(Log_File_List)
        
        return Log_File_List

    def getFolderPath(self):
        
        os.chdir(self.Lesker_Folder_Path)
        

        for file_name in os.listdir(self.Lesker_Folder_Path):
            if fnmatch.fnmatch(file_name, '* Batch %d' %self.Batch_Number):
                Batch_File_Path = ('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s' %file_name)
                Batch_Log_File_Path = ('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s\Deposition Log Files' %file_name)
    
        
        FolderPath = {'BatchFolderPath' : Batch_File_Path, 'LogFileFolderPath': Batch_Log_File_Path}
        
        #print (FolderPath)
        
        
        return FolderPath


    def countLayerNumber(self):
        
        #Change Destination#
        os.chdir(self.Lesker_Folder_Path)
        
        Log_File_List = FileHandling(self.Batch_Number).getLogFileList()        
        
        Layer_Number = len(Log_File_List)
    
        #print(Layer_Number)
        
        
        return Layer_Number


    def loadLogFileLayer(self, Layer_Order):
        
        
        Batch_Log_File_Folder_Path = FileHandling(self.Batch_Number).getFolderPath()['LogFileFolderPath']
        
        #Change Destination#
        os.chdir(Batch_Log_File_Folder_Path)
           
        Batch_Log_File_Path = (os.listdir(Batch_Log_File_Folder_Path)[Layer_Order])
        
        Load_Log_File_per_Layer = pandas.read_csv(Batch_Log_File_Path , error_bad_lines=False)
  
    
        return Load_Log_File_per_Layer



    
    
    
    
    