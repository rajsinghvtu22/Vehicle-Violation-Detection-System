import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import time
import os
from PIL import Image
#   import pygame
from tkinter import *
import tkinter as ttk

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("SAMPLE")
##window.config(bg='pink')

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
#answer = messagebox.askquestion(dialog_title, dialog_text)
 
window.geometry('900x500')
window.configure(background='Grey')
##BG = PhotoImage(file = 'Lotus-Flowers.png')
##label = ttk.Label(window, image = BG)
##PhotoImage(file = 'Lotus-Flowers.png')

lbl = tk.Label(window, text="Traffic Rules Violation Detection",width=30  ,height=2  ,fg="Black"  ,bg="Yellow" ,font=('Arial', 16, ' bold ') ) 
lbl.place(x=300, y=100)

lbl = tk.Label(window, text="Violation",width=20  ,height=2  ,fg="Black"  ,bg="Yellow" ,font=('Arial', 16, ' bold ') ) 
lbl.place(x=200, y=200)

lbl2 = tk.Label(window, text="No Parking",width=20  ,fg="Black"  ,bg="Yellow"    ,height=2 ,font=('Arial', 16, ' bold ')) 
lbl2.place(x=200, y=300)
 
def Button1():
    print("Button1 Pressed")
    os.system('python violation.py')
       
def Button2():
    print("Button2 Pressed")
    os.system('python noparking.py')   

Button1 = tk.Button(window, text="Button1", command=Button1  ,fg="Black"  ,bg="Yellow"  ,width=15  ,height=2 ,activebackground = "Green" ,font=('times', 15, ' bold '))
Button1.place(x=600, y=200)


Button2 = tk.Button(window, text="Button2", command=Button2  ,fg="Black"  ,bg="Yellow"  ,width=15  ,height=2, activebackground = "Green" ,font=('times', 15, ' bold '))
Button2.place(x=600, y=300)

window.mainloop()
