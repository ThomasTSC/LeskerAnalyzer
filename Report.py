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
import Data



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
        
        
        #Layer_Data = File_Handling.FileHandling(self.Batch_Number).loadLogFileLayer()
        #print (Layer_Data['Layer_1'])
        
        Sensor_Info=Data.LayerAnalysis(self.Batch_Number).Corresponding_Sensor(Layer_Order)
        print (Sensor_Info)    
        #Time = Layer_Analysis.Layer_Analysis(self.Batch).TimeDuration(Layer_Order)
     
            #make it clear#
            #if Layer_Order == self.Layer_Number-1:
                #Sensor_Info[1][0]= 6 
                
            #dictSensor_Info = {"source":Sensor_Info[0], "sensor": Sensor_Info[1]}
            
            
            #plt.figure()
            #for sensor in dictSensor_Info["sensor"]:
                #Reg_Plot = seaborn.regplot(x=numpy.array(Time), y=Layer_Data['Rate_%d' % sensor])
             
             
             
                
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
            
            
            
            
            
            
            
            
            
            #plt.title('Layer_%d' %(Layer_Order+1) )
            #plt.ylabel('Rate (A/s)')
            #plt.xlabel('Time (s)')
            #plt.savefig(Log_File_Info.Log_File_Info(self.Batch).Log_File_Info()['Batch_File_Path']+"\ "+"Layer_%d" %(Layer_Order+1))
            
            
            
    
    
    
    def Report(self):
        
        return    
    
    
    
    
    
if __name__ == "__main__":
    
    Report(672).Plot()
    print('done')
    
    
    
    