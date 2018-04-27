# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:58:05 2018

@author: chou
"""

import File_Manipulation
import pandas
import math
import Log_File_Info
import Count_Layer_Number
import numpy
import time
import datetime



class Layer_Analysis:
    
    def __init__(self, Batch_Number):
        self.Batch = Batch_Number
        self.Log_File_Name = Log_File_Info.Log_File_Info(Batch_Number).Log_File_Info()['Log_File_List'] 
        self.Layer_Number = Count_Layer_Number.Count_Layer_Number(Batch_Number)
        
        #print (self.Layer_Number)
        
    def Deposited_Thickness(self, Layer_Order):
        
        Deposition_Details = File_Manipulation.File_Manipulation(self.Batch, Layer_Order).Data_Classification()
        
        #print (Deposition_Details)
        
        Source_Number = {}
        
        Source_Number['Layer_%d_Source' %(Layer_Order+1)] = self.Log_File_Name[Layer_Order].split(' ')[2].split(',')
        
        
        Deposited_Thickness = {}
        
        kA_to_nm = 100
        
      
        
        B = (list(map(float,Source_Number['Layer_%d_Source' %(Layer_Order+1)])))                
        A = [x / 2 for x in B]             
        Cor_Sensor = ([ math.ceil(x) for x in A])
                 
        if Layer_Order == self.Layer_Number-1:
            Cor_Sensor = [6]
            
        #layerThickness = 'Layer_%d' %(Layer_Order+1)
       # reallayerThickness = 'Thickness_%d' %Cor_Sensor[0]
        
        #Deposited_Thickness[layerThickness] = [0,0,0,0]
        #for sensorIndex in range(len(Cor_Sensor)):
           # Deposited_Thickness[layerThickness][sensorIndex] = (pandas.Series(Deposition_Details[reallayerThickness]).values[-1]*kA_to_nm)
        
        if len(Cor_Sensor) == 1:
            
           # Deposited_Thickness[layerThickness] = [(pandas.Series(Deposition_Details[reallayerThickness]).values[-1]*kA_to_nm),0,0,0]

            Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [(pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm),0,0,0]
        if len(Cor_Sensor) == 2:
            Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm,pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[1]]).values[-1]*kA_to_nm,0,0]
        
        if len(Cor_Sensor) == 3:
           Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[1]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[2]]).values[-1]*kA_to_nm,0]
        
        if len(Cor_Sensor) == 4:
            Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[1]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[2]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Thickness_%d' %Cor_Sensor[3]]).values[-1]*kA_to_nm]

        #print(Deposited_Thickness)
        
        return Deposited_Thickness
    
    
    def Corresponding_Sensor(self, Layer_Order):
        
        Source_Number = {}
        
        Source_Number['Layer_%d_Source' %(Layer_Order+1)] = self.Log_File_Name[Layer_Order].split(' ')[2].split(',')
        
        
        
        B = (list(map(float,Source_Number['Layer_%d_Source' %(Layer_Order+1)])))                
        A = [x / 2 for x in B]             
        Cor_Sensor = ([ math.ceil(x) for x in A])
                 
        if Layer_Order == self.Layer_Number-1:
            Cor_Sensor= [6]
            
        
        Sensor = [Source_Number, Cor_Sensor]
        
        
        #print (Sensor)
        return Sensor
    
    
    def TimeDuration(self, Layer_Order):
        
        Deposition_Details = File_Manipulation.File_Manipulation(self.Batch, Layer_Order).Data_Classification()
    
        Init_Date = (pandas.Series(Deposition_Details['RecDate']).values[0]).split('/')
    
        Init_Time = (pandas.Series(Deposition_Details['RecTime']).values[0]).split(':')
    
        Time_Series = []
    
        for i in range(0, len(pandas.Series(Deposition_Details['RecDate']))):
            Instant_Date = (pandas.Series(Deposition_Details['RecDate']).values[i]).split('/')
            Instant_Time = (pandas.Series(Deposition_Details['RecTime']).values[i]).split(':')
        
            b = datetime.datetime(int(Instant_Date[2]),int(Instant_Date[1].strip("0")),int(Instant_Date[0]),int(Instant_Time[0]),int(Instant_Time[1]),int(Instant_Time[2]))

            a = datetime.datetime(int(Init_Date[2]),int(Init_Date[1].strip("0")),int(Init_Date[0]),int(Init_Time[0]),int(Init_Time[1]),int(Init_Time[2]))
            diffSeconds = (b-a).total_seconds() 
    
            Time_Series.append(diffSeconds)
        
        Time_Series = list(map(int, Time_Series))
      
        
        return Time_Series
    
    def Data_Output(self):
        
        Deposited= {}
        
        for i in range(0,self.Layer_Number):   
           
            Deposited['Layer_%d' %(i+1)] = Layer_Analysis(self.Batch).Deposited_Thickness(i)['Layer_%d' %(i+1)]
    

        Deposited = list(Deposited.values())
        Deposited = [numpy.round(x,2) for x in Deposited]
        Deposited = [x.tolist() for x in Deposited]
    


        Layer_Info = {'Deposited': Deposited}



        return Layer_Info
    
if __name__ == "__main__":
    Layer_Analysis(652).Deposited_Thickness(0)
    #Layer_Analysis(652).Corresponding_Sensor(11)
    #Layer_Analysis(648).TimeDuration(0)
    #Layer_Analysis(652).Data_Output()
