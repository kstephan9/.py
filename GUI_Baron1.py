import tkinter as tk
tkinter._test()

root = tk()

button = ttk.Button(root, text='my button')
button.pack()
print(button['text'])  # show value of an attribute
button['text'] = 'Click Me.' # change the value of an attribute
print(button['text'])
button.config(text = 'Push Me')
print(button['text'])

print(button.config())


Label(root, text="Hello, Tkinter!").pack()
root.mainloop()

