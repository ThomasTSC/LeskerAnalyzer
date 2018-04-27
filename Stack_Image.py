# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:31:35 2018

@author: chou
"""


import os
import excel2img
import fnmatch
import glob

def Stack_Image(Batch):
    
    Lesker_Folder_Path = 'P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker'
    
    os.chdir(Lesker_Folder_Path)
    
    for file_name in os.listdir(Lesker_Folder_Path):
        if fnmatch.fnmatch(file_name, '* Batch %d' %Batch):
            os.chdir('P:\Forschungs-Projekte\OLED-measurements Bruchsal\B 2018 Lesker\%s' %(file_name))
            for file_name in glob.glob('*-sheet.xlsx'):
                excel2img.export_img(file_name, "Batch %s.png" %Batch, "", "fabSheet!D14:I31")

