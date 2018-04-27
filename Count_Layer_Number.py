# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 14:57:11 2018

@author: chou
"""

import os
import Log_File_Info
import glob

def Count_Layer_Number(Batch_Number):
    
        #Change Destination#
        Lesker_Folder_Path = Log_File_Info.Log_File_Info(Batch_Number).Log_File_Info()['Log_File_Path']
        
        os.chdir(Lesker_Folder_Path)
                    
        Layer_Number = 0
        for file_name in glob.glob('*.csv'):
           Layer_Number = Layer_Number +1


       
        #print (Layer_Number)
        
        return Layer_Number
    



#Count_Layer_Number(654)