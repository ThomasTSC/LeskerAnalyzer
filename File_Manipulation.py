# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 12:20:19 2018

@author: chou
"""


import seaborn
import Log_File_Info
import Load_Log_File

class File_Manipulation:
    
    
    def __init__(self, Batch_Number, Layer_Order):
        self.Batch = Batch_Number
        self.Layer_Order = Layer_Order
    
    
    def Data_Classification(self):
        
        Layer_Data = Load_Log_File.Load_Log_File( self.Batch,self.Layer_Order).Load_Log_File()
        
        
        
        Layer_Data = Layer_Data[Layer_Data['ShSubstrate']=='ON']
        
                
        Deposition_Details = {'OLED_1':Layer_Data.iloc[:]['OLED1'], 
                          'OLED_2':Layer_Data.iloc[:]['OLED2'],
                          'OLED_3':Layer_Data.iloc[:]['OLED3'], 
                          'OLED_4':Layer_Data.iloc[:]['OLED4'],
                          'OLED_5':Layer_Data.iloc[:]['OLED5'], 
                          'OLED_6':Layer_Data.iloc[:]['OLED6'],
                          'OLED_7':Layer_Data.iloc[:]['OLED7'], 
                          'OLED_8':Layer_Data.iloc[:]['OLED8'],
                          'OLED_9':Layer_Data.iloc[:]['OLED9'], 
                          'OLED_10':Layer_Data.iloc[:]['OLED10'],
                          'Rate_1':Layer_Data.iloc[:]['Rate1'],
                          'Rate_2':Layer_Data.iloc[:]['Rate2'],
                          'Rate_3':Layer_Data.iloc[:]['Rate3'],
                          'Rate_4':Layer_Data.iloc[:]['Rate4'],
                          'Rate_5':Layer_Data.iloc[:]['Rate5'],
                          'Rate_6':Layer_Data.iloc[:]['Rate6'],
                          'Thickness_1':Layer_Data.iloc[:]['Thickness1'],
                          'Thickness_2':Layer_Data.iloc[:]['Thickness2'],
                          'Thickness_3':Layer_Data.iloc[:]['Thickness3'],
                          'Thickness_4':Layer_Data.iloc[:]['Thickness4'],
                          'Thickness_5':Layer_Data.iloc[:]['Thickness5'],
                          'Thickness_6':Layer_Data.iloc[:]['Thickness6'],
                          'RecDate':Layer_Data.iloc[:]['RecDate'],
                          'RecTime':Layer_Data.iloc[:]['RecTime'],
                          'ShSubstrate':Layer_Data.iloc[:]['ShSubstrate'],
                          }
        
        
        
        return Deposition_Details 
    
    


Test = File_Manipulation(648, 0)
Test.Data_Classification()
