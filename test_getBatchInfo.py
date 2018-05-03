'''
Created on 03.05.2018

@author: chou
'''


import openpyxl
import glob
import os
import json




class Get_Batch_Info:
    
    def __init__(self, Batch_Number):
        self.Lesker_Tool_Plan_Path = (r"P:\Production and Physics Communication\Tool Plan\Lesker")
        self.Batch_Number = Batch_Number
    
    def getBatchLocation(self):
        
        os.chdir(self.Lesker_Tool_Plan_Path)
        
        for file_name in glob.glob('Lesker tool planning *.xlsm'):
            Tool_Plan_name_Lesker = file_name
                        

            print(Tool_Plan_name_Lesker)
            Plan_Lekser = openpyxl.load_workbook(Tool_Plan_name_Lesker)

    
            Plan_Lekser_sheet = Plan_Lekser.get_sheet_by_name('Planning Tool')


            #Specify the batch#

            for location in range(10000, 20000):
                if Plan_Lekser_sheet.cell(row=location, column=2).value == self.Batch_Number :
                    Batch_Location_Index = location
                    print (Batch_Location_Index)
                        
        
        return Batch_Location_Index
    
    #def saveLocationJSON(self):
        
        #SearchLocation = 
        
        #with open('SearchLocation.txt', 'w') as outfile:
            #json.dump(data, outfile)
        
        
    
    
        
    def getBatchInfo(self):
        
        
        
        return
       
        
if __name__ == "__main__":
    Get_Batch_Info(668).getBatchLocation()
    