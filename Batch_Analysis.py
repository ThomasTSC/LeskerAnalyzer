# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 14:41:12 2018

@author: chou
"""


import Get_Batch_Info
import re
import Log_File_Info
import Count_Layer_Number
import numpy


class Layer_Info:
        
    
    def __init__(self, Batch_Number):
        self.Layer_Number = Count_Layer_Number.Count_Layer_Number(Batch_Number)
        self.Batch = Batch_Number
        self.Log_File_Name = Log_File_Info.Log_File_Info(Batch_Number).Log_File_Info()['Log_File_List'] 
        self.Batch_Info = Get_Batch_Info.Get_Batch_Info(Batch_Number)
        
        
    def Layer_Name(self):
            
        Layer_Name = {}
          
    
        for i in range(0,self.Layer_Number): #need to change
            
            Layer_Name['Layer_%d' %(i+1)] = (str(self.Log_File_Name[i].split()[1])+' '+str(self.Log_File_Name[i].split()[2]))
            
        
        #print (Layer_Name)
        
        return Layer_Name
    


    def Layer_Ratio(self):
        
        
        Layer_Info = {}
        Source_Number_per_Layer = {}
        for i in range(0, self.Layer_Number):

            Layer_Info['Layer_%d' %(i+1)] = self.Log_File_Name[i]
            Source_Number_per_Layer['Layer_%d' %(i+1)]=(len(self.Log_File_Name[i].split(' ')[2].split(',')))
        
       
        
        Layer_Ratio = {}
        
        
        for i in range(0, self.Layer_Number):

            if Source_Number_per_Layer['Layer_%d' %(i+1)] == 1:
                Layer_Ratio['Layer_%d_Ratio' %(i+1)] = [1 , 0, 0, 0]
            if Source_Number_per_Layer['Layer_%d' %(i+1)] > 1:
                Rate_Ratio = self.Log_File_Name[i].split()[3].split('&')    
                Rate_Ratio =[item.replace('#','.') for item in Rate_Ratio]
                Layer_Ratio['Layer_%d_Ratio' %(i+1)] = [ x/sum(list(map(float,Rate_Ratio))) for x in (list(map(float,Rate_Ratio)))]
         
        Ratio = list(Layer_Ratio.values())
        Ratio = [numpy.round(x,2) for x in Ratio]
        Ratio= [x.tolist() for x in Ratio]
        for i in range(0, self.Layer_Number):
            Layer_Ratio['Layer_%d_Ratio' %(i+1)] = Ratio[i]
        
        
        return Layer_Ratio



    def Layer_Ideal_Thickness(self):
        
        Layer_Ratio = Layer_Info.Layer_Ratio(self)
        
        Layer_Ideal_Thickness = self.Batch_Info['Architecture'] 
        
        
     
        
        Layer_Ideal_Thickness = [x for x in Layer_Ideal_Thickness if x is not None] 
        
        Layer_Ideal_Thickness = [s for s in Layer_Ideal_Thickness if "nm" in s]
        
        Layer_Ideal_Thickness = [int(re.search(r'\d+', x).group()) for x in Layer_Ideal_Thickness]
        
        
        
        Layer_Ideal_Thickness.reverse()
        
       
        
        del Layer_Ideal_Thickness[0]
  
        
    

        
        Ideal_Thickness = {}
        
        for i in range(0, self.Layer_Number):

            Ideal_Thickness['Layer_%d' %(i+1)] = ([Layer_Ideal_Thickness[i]*x for x in Layer_Ratio['Layer_%d_Ratio' %(i+1)][:]])
            
        
                 
        Thickness = list(Ideal_Thickness.values())
        Thickness = [numpy.round(x,2) for x in Thickness]
        Thickness = [x.tolist() for x in Thickness]
        
        Layer_Ideal_Thickness = {}
        
        for i in range(0, self.Layer_Number):
            Layer_Ideal_Thickness['Layer_%d_Ratio' %(i+1)] = Thickness[i]
        
   
    
       #print (Layer_Ideal_Thickness)
        
        return Layer_Ideal_Thickness
    


        
    def Data_Output(self):
        
            Layer_Name = Layer_Info.Layer_Name(self)
            Layer_Ratio = Layer_Info.Layer_Ratio(self)    
            Layer_Ideal_Thickness = Layer_Info.Layer_Ideal_Thickness(self)
    
            Batch_Info_Summary = {'Layer_Name':Layer_Name,'Layer_Ratio':Layer_Ratio, 'Layer_Ideal_Thickness':Layer_Ideal_Thickness}
            
            
            #print (Batch_Info_Summary)
    
            return Batch_Info_Summary
    



#Test#

#est = Layer_Info(643)
#Test.Layer_Name()
#Test.Layer_Ratio()
#Test.Layer_Ideal_Thickness()
#Test.Data_Output()