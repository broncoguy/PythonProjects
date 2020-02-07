# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 19:08:49 2020

@author: Larry
"""

import tkinter as tk
from googletrans import Translator
import os

def getLetters():
    
    f=open("languages.txt", "r")

    if f.mode == 'r':
    
        contents = f.read()
        language = contents.splitlines()
        
    
    f.close()
    return language


def getText(str):
    f = str + ".txt"
   
    t=open(f,"r")

    if t.mode == 'r':
        contents = t.read()
    
    
    t.close()
    return contents
 

#
win = tk.Tk() 
win.title("Translator")
win.geometry("500x100")

translated = []
path = os.getcwd()


def translation():
    word = entry.get()
    translator = Translator(service_urls=['translate.google.com'])
    TextFile = getText(word)
    languages = getLetters()
    for i in range(len(languages)):
        translator = Translator(service_urls=['translate.google.com'])
        translation1 = translator.translate(TextFile,dest=languages[i])
        translated.append(translation1.text)
     
     
    with open('myfile.txt', 'w', encoding="utf-8") as filehandle:
        for listitem in translated:
            filehandle.write('%s\n' % listitem)
    
    label1 = tk.Label(win,text=f"Text created!",bg="yellow")
    label1.grid(row=2,column=0)
    label2 = tk.Label(win,text="File is located in " + path,bg="yellow")
    label2.grid(row=3,column=0)
#    
label = tk.Label(win,text="Enter Word : ")
label.grid(row=0,column=0,sticky="W")
#    
entry = tk.Entry(win)
entry.grid(row=1,column=0)
    
button = tk.Button(win,text="Translate", command= translation)
button.grid(row=1,column=2)
 

win.mainloop()
