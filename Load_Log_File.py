# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 11:59:29 2018

@author: chou
"""

import pandas
import os
import Log_File_Info


class Load_Log_File:
    
    def __init__(self, Batch_Number, Layer_Order):
        
        self.Batch = Batch_Number
        self.Layer_Order = Layer_Order
        self.Lesker_Folder_Path = 'P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker'
    

    def Load_Log_File(self):

        #Change Destination#
        os.chdir(self.Lesker_Folder_Path)
    
    
        Log_File_Path = (os.listdir(Log_File_Info.Log_File_Info(self.Batch).Log_File_Info()['Log_File_Path'])[self.Layer_Order])
        
        
        Load_File = pandas.read_csv(Log_File_Path, error_bad_lines=False)

    
        return Load_File



