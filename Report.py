# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:25:23 2018

@author: chou
"""


import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import Stack_Image
import Log_File_Info
import datetime
import Get_Batch_Info
import glob
import Batch_Analysis
import Layer_Analysis
import operator
import numpy
import File_Manipulation
import Count_Layer_Number
import seaborn
import matplotlib.pyplot as plt



class Report:
    
    def __init__(self, Batch_Number):
        self.Batch = Batch_Number
        self.Layer_Number = Count_Layer_Number.Count_Layer_Number(Batch_Number)
    
    
    def Info_Summary(self):
        
        Batch_Info = Batch_Analysis.Layer_Info(self.Batch).Data_Output()
        Layer_Info = Layer_Analysis.Layer_Analysis(self.Batch).Data_Output()
        
       
        
        Layer_Name = list(Batch_Info['Layer_Name'].values())
        Layer_Ratio = list(Batch_Info['Layer_Ratio'].values())
        Layer_Ideal_Thickness = list(Batch_Info['Layer_Ideal_Thickness'].values())
        Deposited = (Layer_Info['Deposited'])
        
        
        Deviation = [list(map(operator.sub,(Deposited[i]),( Layer_Ideal_Thickness[i]))) for i in range(0,len(Deposited))]

        Deviation =  [numpy.round(x,2) for x in Deviation]
        Deviation =  [x.tolist() for x in Deviation]
        
               
        Data_For_Report = [Layer_Name, Layer_Ratio, Layer_Ideal_Thickness, Deposited, Deviation]
    
    
        return Data_For_Report
    
    
    def Plot(self):
        
        for Layer_Order in range (0, self.Layer_Number):
            Layer_Data = File_Manipulation.File_Manipulation(self.Batch, Layer_Order).Data_Classification()
            Sensor_Info=Layer_Analysis.Layer_Analysis(self.Batch).Corresponding_Sensor(Layer_Order)
            Time = Layer_Analysis.Layer_Analysis(self.Batch).TimeDuration(Layer_Order)
     
            #make it clear#
            if Layer_Order == self.Layer_Number-1:
                Sensor_Info[1][0]= 6 
                
            dictSensor_Info = {"source":Sensor_Info[0], "sensor": Sensor_Info[1]}
            
            plt.figure()
            for sensor in dictSensor_Info["sensor"]:
                Reg_Plot = seaborn.regplot(x=numpy.array(Time), y=Layer_Data['Rate_%d' % sensor])
                
            #Time v.s. Rate Plot#
            #if len(Sensor_Info[1]) >1:
               # plt.figure()
                #for k in range (len(Sensor_Info[1])):
                 #   Reg_Plot = seaborn.regplot(x=numpy.array(Time), y=Layer_Data['Rate_%d' %Sensor_Info[1][k]])
            
            #else:

             #   plt.figure()
              #  Reg_Plot = seaborn.regplot(x=numpy.array(Time), y=Layer_Data['Rate_%d' %Sensor_Info[1][0]])
    #def plot():
    #        Reg_Plot = seaborn.regplot(x=numpy.array(Time), y=Layer_Data['Rate_%d' %Sensor_Info[1][0]])
            plt.title('Layer_%d' %(Layer_Order+1) )
            plt.ylabel('Rate (A/s)')
            plt.xlabel('Time (s)')
            plt.savefig(Log_File_Info.Log_File_Info(self.Batch).Log_File_Info()['Batch_File_Path']+"\ "+"Layer_%d" %(Layer_Order+1))
            
            
            
            
            #Temperatre v.s Rate Plot#
            #if len(Sensor_Info[1]) >1:
             #   plt.figure()
              #  for k in range (len(Sensor_Info[1])):
               #     Reg_Plot = seaborn.regplot(x=Layer_Data['OLED_%d' %(int((list(Sensor_Info[0].values())[0])[k]))], y=Layer_Data['Rate_%d' %Sensor_Info[1][k]])
            
            #else:
             #   plt.figure()
              #  Reg_Plot = seaborn.regplot(x=Layer_Data['OLED_%d' %(int((list(Sensor_Info[0].values())[0])[0]))], y=Layer_Data['Rate_%d' %Sensor_Info[1][0]])
                
            #plt.title('Layer_%d' %(Layer_Order+1) )
            #plt.savefig(Log_File_Info.Log_File_Info(self.Batch).Log_File_Info()['Batch_File_Path']+"\ "+"Layer_%d" %(Layer_Order+1))
            #A = Reg_Plot.get_lines()[0].get_xdata()
            #B = Reg_Plot.get_lines()[0].get_ydata()
        
            #print (A,B)
        
        
        
        
    
    def Report(self):
        
        
        Data_For_Report = Report(self.Batch).Info_Summary()
       
        
        Batch_Info = Get_Batch_Info.Get_Batch_Info(self.Batch)
        
        os.chdir(Log_File_Info.Log_File_Info(self.Batch).Log_File_Info()['Batch_File_Path'])
        
        Stack_Image.Stack_Image(self.Batch)
        
        for file_name in glob.glob('*.png'):
            Stack_Image_Path = (Log_File_Info.Log_File_Info(self.Batch).Log_File_Info()['Batch_File_Path']+ '\%s' %file_name)

        
        BatchReport= canvas.Canvas("Batch Report %d .pdf" %self.Batch, pagesize=letter)
        BatchReport.setLineWidth(.3)
        BatchReport.setFont('Helvetica', 12)
 
        BatchReport.drawString(30,750,'Batch %d Report' %self.Batch)
        BatchReport.drawString(30,735,'CYNORA Production Team')
        BatchReport.drawString(500,750, datetime.datetime.now().strftime("%y-%m-%d"))
        BatchReport.line(480,747,580,747)
 
        BatchReport.drawString(375,725,'Fabrication Tool:')
        
        BatchReport.drawString(500,725,"Lesker I")
        BatchReport.line(480,723,580,723)
 
        BatchReport.drawString(30,703,'Batch: %d' %self.Batch)
        BatchReport.drawString(225,703,"OLED: %s" %Batch_Info['Substrate_List'])
        BatchReport.drawString(30,675,'Experimental Goal: %s' %Batch_Info['Aim'])
    
        BatchReport.drawString(30,650,'Stack:')

        BatchReport.drawImage(Stack_Image_Path,30,340, 515,300)

        BatchReport.drawString(30,320,'Deposition Details:')

        BatchReport.drawString(30,300,'Layer')
    
        BatchReport.drawString(100,300,'Ratio')
    
        BatchReport.drawString(200,300,'Planned (nm)')
    
        BatchReport.drawString(330,300,'Deposited (nm)')
    
        BatchReport.drawString(490,300,'Deviation (nm)')
        
        
        [BatchReport.drawString(30, 285-i*15, Data_For_Report[0][i]) for i in range(0, len(Data_For_Report[0]))]
        [BatchReport.drawString(100, 285-i*15, '%s' %Data_For_Report[1][i]) for i in range(0, len(Data_For_Report[1]))]
        [BatchReport.drawString(200, 285-i*15, '%s' %Data_For_Report[2][i]) for i in range(0, len(Data_For_Report[2]))]
        [BatchReport.drawString(330, 285-i*15, '%s' %Data_For_Report[3][i]) for i in range(0, len(Data_For_Report[3]))]
        [BatchReport.drawString(490, 285-i*15, '%s' %Data_For_Report[4][i]) for i in range(0, len(Data_For_Report[4]))]

    

    
        
        
        
        
        BatchReport.save()

if __name__ == "__main__":
    #Report(643).Info_Summary()
    Report(665).Plot()    
    Report(665).Report()
    
    
    
    