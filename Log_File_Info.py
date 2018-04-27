# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:59:29 2018

@author: chou
"""


import os
import glob
import fnmatch


class Log_File_Info:
    
    def __init__(self, Batch_Number):
        
        self.Batch = Batch_Number
        self.Lesker_Folder_Path = 'P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker'
    
    def Log_File_Info(self):
    
        #Change Destination#

        os.chdir(self.Lesker_Folder_Path)
    
        Log_File_List = []

        for file_name in os.listdir(self.Lesker_Folder_Path):
            if fnmatch.fnmatch(file_name, '* Batch %d' %self.Batch):
                Batch_File_Path = ('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s' %file_name)
                Lesker_Batch_Log_File_Path = ('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s\Deposition Log Files' %file_name)
                
                os.chdir(Lesker_Batch_Log_File_Path)
            
        for file_name in glob.glob('*.csv'):
           Log_File_List.append(file_name)

    
    
        Log_File_Info = {'Log_File_Path':Lesker_Batch_Log_File_Path, 'Log_File_List':Log_File_List, 'Batch_File_Path': Batch_File_Path}
    
        #print (Log_File_Info)
    
        return Log_File_Info

        


#Test=Log_File_Info(654)
#Test.Log_File_Info()

