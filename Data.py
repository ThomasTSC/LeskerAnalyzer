'''
Created on 27.04.2018

@author: chou
'''


import File_Handling
import numpy
import re
import Get_Batch_Info
import pandas
import math
import datetime

class DataManipulation:
    '''
    classdocs
    '''

    def __init__(self, Batch_Number):
        self.Batch_Number = Batch_Number
        self.Layer_Number = File_Handling.FileHandling(self.Batch_Number).countLayerNumber()
        
        
    def classifiedData(self):
        
        Layer_Data = {}
        
        for Layer_Order in range (0, self.Layer_Number):
        
            Layer_Raw_Data = File_Handling.FileHandling(self.Batch_Number).loadLogFileLayer()['Layer_%d' %(Layer_Order+1)]
        
        
            Layer_Raw_Data = Layer_Raw_Data[Layer_Raw_Data['ShSubstrate']=='ON']
        
    
    
            Deposition_Details = {'OLED_1':Layer_Raw_Data.iloc[:]['OLED1'], 
                          'OLED_2':Layer_Raw_Data.iloc[:]['OLED2'],
                          'OLED_3':Layer_Raw_Data.iloc[:]['OLED3'], 
                          'OLED_4':Layer_Raw_Data.iloc[:]['OLED4'],
                          'OLED_5':Layer_Raw_Data.iloc[:]['OLED5'], 
                          'OLED_6':Layer_Raw_Data.iloc[:]['OLED6'],
                          'OLED_7':Layer_Raw_Data.iloc[:]['OLED7'], 
                          'OLED_8':Layer_Raw_Data.iloc[:]['OLED8'],
                          'OLED_9':Layer_Raw_Data.iloc[:]['OLED9'], 
                          'OLED_10':Layer_Raw_Data.iloc[:]['OLED10'],
                          'Rate_1':Layer_Raw_Data.iloc[:]['Rate1'],
                          'Rate_2':Layer_Raw_Data.iloc[:]['Rate2'],
                          'Rate_3':Layer_Raw_Data.iloc[:]['Rate3'],
                          'Rate_4':Layer_Raw_Data.iloc[:]['Rate4'],
                          'Rate_5':Layer_Raw_Data.iloc[:]['Rate5'],
                          'Rate_6':Layer_Raw_Data.iloc[:]['Rate6'],
                          'Thickness_1':Layer_Raw_Data.iloc[:]['Thickness1'],
                          'Thickness_2':Layer_Raw_Data.iloc[:]['Thickness2'],
                          'Thickness_3':Layer_Raw_Data.iloc[:]['Thickness3'],
                          'Thickness_4':Layer_Raw_Data.iloc[:]['Thickness4'],
                          'Thickness_5':Layer_Raw_Data.iloc[:]['Thickness5'],
                          'Thickness_6':Layer_Raw_Data.iloc[:]['Thickness6'],
                          'RecDate':Layer_Raw_Data.iloc[:]['RecDate'],
                          'RecTime':Layer_Raw_Data.iloc[:]['RecTime'],
                          'ShSubstrate':Layer_Raw_Data.iloc[:]['ShSubstrate'],
                          }
        
            Layer_Data['Layer_%d' %(Layer_Order+1)]= Deposition_Details 
        
        #print (Layer_Data['Layer_1']['Rate_5'])
        
        return Layer_Data
    
   
class BatchAnalysis: 
    
    def __init__(self, Batch_Number):
        self.Batch_Number = Batch_Number
        self.Layer_Number = File_Handling.FileHandling(self.Batch_Number).countLayerNumber()
    
    def layerName(self):
        
        Layer_Name = {}
          
    
        for i in range(self.Layer_Number): #need to change
            
            Layer_Name['Layer_%d' %(i+1)] = (str(File_Handling.FileHandling(self.Batch_Number).getLogFileList()[i].split()[1])+' '+str(File_Handling.FileHandling(self.Batch_Number).getLogFileList()[i].split()[2]))
        
        #print (Layer_Name)
        
        return Layer_Name
        
        
    
    def layerRatio(self):
        

        Source_Number_per_Layer = {}
        for i in range(0, self.Layer_Number):
            Source_Number_per_Layer['Layer_%d' %(i+1)]=(len(File_Handling.FileHandling(self.Batch_Number).getLogFileList()[i].split(' ')[2].split(',')))
        
       
       
        Layer_Ratio = {}
        
        
        for i in range(self.Layer_Number):

            if Source_Number_per_Layer['Layer_%d' %(i+1)] == 1:
                Layer_Ratio['Layer_%d_Ratio' %(i+1)] = [1 , 0, 0, 0]
            if Source_Number_per_Layer['Layer_%d' %(i+1)] > 1:
                Rate_Ratio = File_Handling.FileHandling(self.Batch_Number).getLogFileList()[i].split()[3].split('&')    
                Rate_Ratio =[item.replace('#','.') for item in Rate_Ratio]
                Layer_Ratio['Layer_%d_Ratio' %(i+1)] = [ x/sum(list(map(float,Rate_Ratio))) for x in (list(map(float,Rate_Ratio)))]
         
        Ratio = list(Layer_Ratio.values())
        Ratio = [numpy.round(x,2) for x in Ratio]
        Ratio= [x.tolist() for x in Ratio]
        for i in range(0, self.Layer_Number):
            Layer_Ratio['Layer_%d_Ratio' %(i+1)] = Ratio[i]
        
        
        #print (Layer_Ratio)
        
        return Layer_Ratio
        
        
    def layerPlannedThickness(self):
        
        Layer_Ratio = BatchAnalysis(self.Batch_Number).layerRatio()
        
        Batch_Info = Get_Batch_Info.Get_Batch_Info(self.Batch_Number)
        
        
        Layer_Ideal_Thickness = Batch_Info['Architecture'] 
        
        
        Layer_Ideal_Thickness = [x for x in Layer_Ideal_Thickness if x is not None] 
        
        Layer_Ideal_Thickness = [s for s in Layer_Ideal_Thickness if "nm" in s]
        
        Layer_Ideal_Thickness = [int(re.search(r'\d+', x).group()) for x in Layer_Ideal_Thickness]
        
        
        Layer_Ideal_Thickness.reverse()
        
       
        del Layer_Ideal_Thickness[0]
  
        
        Ideal_Thickness = {}
        
        for i in range(self.Layer_Number):

            Ideal_Thickness['Layer_%d' %(i+1)] = ([Layer_Ideal_Thickness[i]*x for x in Layer_Ratio['Layer_%d_Ratio' %(i+1)][:]])
            
        
                 
        Thickness = list(Ideal_Thickness.values())
        Thickness = [numpy.round(x,2) for x in Thickness]
        Thickness = [x.tolist() for x in Thickness]
        
        Layer_Ideal_Thickness = {}
        
        for i in range(0, self.Layer_Number):
            Layer_Ideal_Thickness['Layer_%d_Ratio' %(i+1)] = Thickness[i]
        
   
        #print (Layer_Ideal_Thickness)
        
        return Layer_Ideal_Thickness
        
        
class LayerAnalysis:    
    
    def __init__(self, Batch_Number):
        self.Batch_Number = Batch_Number
        self.Layer_Number = File_Handling.FileHandling(self.Batch_Number).countLayerNumber()

    
    
    def depositedThickness(self):
        
        Deposition_Details = File_Handling.FileHandling(self.Batch_Number).loadLogFileLayer()
        
        #print (Deposition_Details)
        
        Source_Number = {}
        Deposited_Thickness = {}
        kA_to_nm = 100
        
        for Layer_Order in range(self.Layer_Number):
    
            Source_Number['Layer_%d_Source' %(Layer_Order+1)] = File_Handling.FileHandling(self.Batch_Number).getLogFileList()[Layer_Order].split(' ')[2].split(',')
        
            B = (list(map(float,Source_Number['Layer_%d_Source' %(Layer_Order+1)])))                
            A = [x / 2 for x in B]             
            Cor_Sensor = ([ math.ceil(x) for x in A])
                 
            if Layer_Order == self.Layer_Number-1:
                Cor_Sensor = [6]
            
            #print (Cor_Sensor)
       
        #layerThickness = 'Layer_%d' %(Layer_Order+1)
        # reallayerThickness = 'Thickness_%d' %Cor_Sensor[0]
        
        #Deposited_Thickness[layerThickness] = [0,0,0,0]
        #for sensorIndex in range(len(Cor_Sensor)):
        # Deposited_Thickness[layerThickness][sensorIndex] = (pandas.Series(Deposition_Details[reallayerThickness]).values[-1]*kA_to_nm)
        
            if len(Cor_Sensor) == 1:
            
        # Deposited_Thickness[layerThickness] = [(pandas.Series(Deposition_Details[reallayerThickness]).values[-1]*kA_to_nm),0,0,0]

                Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [(pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm),0,0,0]
            if len(Cor_Sensor) == 2:
                    Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm,pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[1]]).values[-1]*kA_to_nm,0,0]
        
            if len(Cor_Sensor) == 3:
                    Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[1]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[2]]).values[-1]*kA_to_nm,0]
        
            if len(Cor_Sensor) == 4:
                    Deposited_Thickness['Layer_%d' %(Layer_Order+1)] = [pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[0]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[1]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[2]]).values[-1]*kA_to_nm, pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['Thickness%d' %Cor_Sensor[3]]).values[-1]*kA_to_nm]

        #print(Deposited_Thickness)
    
        return Deposited_Thickness


    def correspondingSource(self):
        
        Source_Number = {}
        Cor_Sensor = {}
        
        
        for Layer_Order in range(self.Layer_Number):
        
            Source_Number['Layer_%d_Source' %(Layer_Order+1)] = File_Handling.FileHandling(self.Batch_Number).getLogFileList()[Layer_Order].split(' ')[2].split(',')
        
        
        
            B = (list(map(float,Source_Number['Layer_%d_Source' %(Layer_Order+1)])))                
            A = [x / 2 for x in B]             
            
            Cor_Sensor['Layer_%d_Source' %(Layer_Order+1)] = ([ math.ceil(x) for x in A])
                 
            if Layer_Order == self.Layer_Number-1:
                Cor_Sensor['Layer_%d_Source' %(Layer_Order+1)]= [6]
            
        
        Sensor_Info = {'Sensor_Number':Source_Number, 'Corresponding_Sensor':Cor_Sensor}
        
        
        #print (Sensor_Info)
        
        return Sensor_Info
        
        
    
    
    def timeDuration(self):
        
        Deposition_Details = DataManipulation(self.Batch_Number).classifiedData()
    
        Time_Duration = {}
    
        for Layer_Order in range(self.Layer_Number):
            
            Init_Date = (pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['RecDate']).values[0]).split('/')
    
            Init_Time = (pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['RecTime']).values[0]).split(':')
    
            Time_Series = []
        
        
        
            for i in range(len(pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['RecDate']))):
                Instant_Date = (pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['RecDate']).values[i]).split('/')
                Instant_Time = (pandas.Series(Deposition_Details['Layer_%d' %(Layer_Order+1)]['RecTime']).values[i]).split(':')
        
                b = datetime.datetime(int(Instant_Date[2]),int(Instant_Date[1].strip("0")),int(Instant_Date[0]),int(Instant_Time[0]),int(Instant_Time[1]),int(Instant_Time[2]))

                a = datetime.datetime(int(Init_Date[2]),int(Init_Date[1].strip("0")),int(Init_Date[0]),int(Init_Time[0]),int(Init_Time[1]),int(Init_Time[2]))
            
                diffSeconds = (b-a).total_seconds() 
    
                Time_Series.append(diffSeconds)
        
            
            Time_Series = numpy.array(list(map(int, Time_Series)))
            
            Time_Duration['Layer_%d' %(Layer_Order+1)] = Time_Series
        
        
      
        #print (Time_Duration)
        
        return Time_Duration

    def deviation(self):
        
        
        Deviation = []
        
        return Deviation


if __name__ == "__main__":
    
    DataManipulation(599).classifiedData()
    #BatchAnalysis(599).layerPlannedThickness()
    #LayerAnalysis(599).depositedThickness()
    #LayerAnalysis(599).correspondingSource()
    #LayerAnalysis(599).timeDuration()
    print ('done')









