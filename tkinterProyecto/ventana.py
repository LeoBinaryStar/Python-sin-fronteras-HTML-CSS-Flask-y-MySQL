from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')

#Metodo 1
"""
def open():
    img = ImageTk.PhotoImage(Image.open('marnie.png'))
    top = Toplevel()
    top.title('Hola mundo, nueva  ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()
"""

#Metodo 2
"""
def open():
    global img
    img = ImageTk.PhotoImage(Image.open('marnie.png'))
    top = Toplevel()
    top.title('Hola mundo, nueva  ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
"""

#Metodo 3

def open(img):
    top = Toplevel()
    top.title('Hola mundo, nueva  ventana')
    l = Label(top, text='Soy un texto en una segunda ventana')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open('marnie.png'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()

root.mainloop()
