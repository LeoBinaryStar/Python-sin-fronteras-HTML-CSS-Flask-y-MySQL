from tkinter import *

root = Tk()
root.title('Hola Botón')

l = Label(root,text='Hola Mundo')
def click():
    l.pack()
    
btn = Button(root, text="Click aquí", command=click, fg='#ff0000', bg='blue')
btn.pack()

root.mainloop()
