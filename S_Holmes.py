'''
Created on 02.05.2018

@author: chou
'''

from tkinter import messagebox
import tkinter as tkinter 




class Sherlock(tkinter.Frame):
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        tkinter.Frame.__init__(self, parent)
        self.parent=parent
        self.Sherlock_Interface()
    
    def Sherlock_Interface(self):
    

        self.parent.title("Baker Street 221B")       
        self.parent.grid_rowconfigure(0,weight=1)
        self.parent.grid_columnconfigure(0,weight=1)
        self.parent.geometry('350x100')
        
            
        #Enter the number of batch#
        self.Batch_Label = tkinter.Label(self.parent, text = ' Batch # ', font = ("Arial", 12), width = 5,  height = 1).place (x = 90, y = 20)
        self.var_Batch_Number = tkinter.IntVar()
        self.Batch_Entry = tkinter.Entry(self.parent, textvariable = self.var_Batch_Number, width = 10,show = None).place(x = 90, y = 50)


        #Choose a machine#
        self.Option_Machine = ['','Lesker 1', 'Lesker 2']
        self.Option_Machine_var = tkinter.StringVar()
        self.Option_Machine_Window = tkinter.OptionMenu(self.parent, self.Option_Machine_var , *self.Option_Machine).place(x = 170, y = 45)
        


        #Create the folder, file with all information#
        
        def Observation():
            
            
            #Jumping window#
            messagebox.showinfo(title = "From Sherlock", message = "You see, but you do not observe.")
            
            
        
        self.Observation_Button = tkinter.Button(self.parent, text = " Observe ", width = 10, command = Observation).place(x = 255, y = 48)
        
        
def main():
    root=tkinter.Tk()
    Sherlock(root)
    root.mainloop()

if __name__=="__main__":
    main()










if __name__ == '__main__':
    pass