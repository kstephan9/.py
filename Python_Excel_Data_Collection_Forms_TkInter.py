#!/usr/bin/env python
# coding: utf-8

# # https://www.youtube.com/watch?v=w36yng8BTUU
#

# # Python_Excel_Data_Collection_Forms_TkInter
import os
from tkinter import *
import pandas as pd
from DefaultItems import OutputFolder

path  = os.path.join(OutputFolder,"eee.xlsx")
print("Path: ", path)

class MyFirstGUI:
    def submit_fields():
    #    path = fff
        print("Line 18: ", path)
        df1 = pd.read_excel(path)
        SeriesA = df1['Operator']
        SeriesB = df1['Number']

        A = pd.Series(entry1.get())
        B = pd.Series(entry2.get())

        print("Line 26: ", A)

        SeriesA = SeriesA.append(A)
        SeriesB = SeriesB.append(B)
        df2 = pd.DataFrame({"Operator" : SeriesA, "Number": SeriesB})

        print("line 28: ", df2.head())
        df2.to_excel(path, index=False)

        entry1.delete(0, END)
        entry2.delete(0, END)


    def __init__(self, master):
        self.master = master
        master.title("A Simple GUI")

        self.label = Label(master, text="label text")
        self.label.pack()

        self.submit_button = Button(master, text="submit", command=submit_fields)
        self.close_button = Button(master, text="Quit", command=master.quit)
#    master = Tk()

    Label(master, text = "Operator").grid(row=0)

    Label(master, text = "Number").grid(row=1)

    entry1 = Entry(master)
    entry2 = Entry(master)

    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    Button(master, text='Quit', command="master.quit").grid(row=3, column=0, pady=4)
    Button(master, text='Submit', command="submit_fields").grid(row=3, column=1, pady=4)

master = Tk()
my_gui = MyFirstGUI(master)
master.mainloop()



