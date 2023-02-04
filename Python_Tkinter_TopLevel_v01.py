#!/usr/bin/python3
# hello_local.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

class HelloApp:

    def __init__(self, master):

        frame01 = ttk.Frame(master)

        frame01.pack()

        frame01.config(height = 90, width=160)
        frame01.config(relief = RIDGE)

        self.label = ttk.Label(frame01, text = "Hello, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        ttk.Button(frame01, text = "Texas",
            command = self.texas_hello).grid(row = 1, column = 0)

        frame01.config(padding = (9,16))

        ttk.LabelFrame(master, height = 100, width = 200, text = 'LableFrame Text').pack()

        #ttk.Button(master, text = "Hawaii",
        #           command = self.hawaii_hello).grid(row = 1, column = 1)

        #ttk.Button(master, text = "Escondido",
        #           command = self.callback).grid(row = 1, column = 2)

        #ttk.Button(master, text = "MyButton",
        #           command = self.callback).grid(row = 3, column = 1)

    def callback(self):
        print("Reached callback()")

    def texas_hello(self):
        self.label.config(text = 'Howdy, Tkinter!')

    def hawaii_hello(self):
        self.label.config(text = 'Aloha, Tkinter!')


def main():            
    
    root = Tk()
    root.title('Root Window')
    window = Toplevel(root)
    window.title('New Window')
    window.lower()
    window.lift(root)
    #window.state('zoomed')
    #window.state('withdrawn')
    window.state('iconic')
    window.state('normal')
    window.state()

    window.iconify()
    window.deiconify()

    window.geometry('640x480+50+100')

    window.resizable(False, False)
    window.maxsize(640,480)
    window.minsize(200,200)
    window.resizable(True,True)

    root.destroy()
    
    app = HelloApp(root)
    print("just after HelloApp.")
    root.mainloop()
    
if __name__ == "__main__": main()
