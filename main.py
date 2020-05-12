#=======================================================================================================================
#
# MACHINE LEARNING PROJECT
#
#       IMAGE INPAINTING - Yacine Tchabi & Maxime Denoncin
#
#=======================================================================================================================

# Sources:
# https://www.geeksforgeeks.org/introduction-machine-learning-using-python/

#============= Imports ==============

import numpy as np
import pickle
import tkinter
from win32api import GetSystemMetrics
import systemFunc
from tkinter.ttk import *
import CIFARextract




#============= GET THE DATAS ===============

def buttonLaunch():
    global dataSet
    dataSet = choice1.get()
    dataWindow.destroy()


dataSet = 0
dataWindow = tkinter.Tk()
dataWindow.title("Texas Fail & Co. presents Original Image Inpainting ULTRA")
dataWindow.geometry("300x200")
lab1 = tkinter.Label(dataWindow, text="Welcome to the Original Image Inpainter!")
lab1.grid(column=1, row=0)

lab2 = tkinter.Label(dataWindow, text="Dataset:")
lab2.grid(column=0, row=3)

choice1 = Combobox(dataWindow)
choice1['values'] = ("CIFAR-10")
choice1.grid(column=1, row=3)


exitbtn = tkinter.Button(dataWindow, text="Launch!", command=buttonLaunch)
exitbtn.grid(column=1, row=4)


dataWindow.mainloop()

