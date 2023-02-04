from tkinter import *

from tkinter import ttk

def main():


    print("abc")


    root = Tk()



    button = ttk.Button(root, text = 'my button')

    button.pack()


    def callback():
        print('Clicked')

    button.config(command=callback)

if __name__ == "__main__":
    main()

