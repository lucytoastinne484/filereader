import pyautogui as auto
import pandas as pd
import os as OS
import sys as system
import sysconfig as setup
import tkinter as tk 
import openpyxl as excel
import webbrowser as web
import os as Os

#features#

def fileReader():
    file_path = path.get()
    open_cmd = web.open(file_path)
    
    


#windowsetup
script_window = tk.Tk()#

script_window.title("File Automation script to input data")

script_window.geometry("800x500")

script_window.resizable(False,True)

put_thepath = tk.Label(script_window,text="Ponha o caminho do seu arquivo/pasta aqui")

put_thepath.pack()

path = tk.StringVar()

input_path = tk.Entry(script_window,textvariable=path)

input_path.pack()

open_file = tk.Button(script_window,text="Open File",command=fileReader,compound='left')

open_file.pack(ipadx=12,ipady=12)

script_window.mainloop()
#-------------#




    
