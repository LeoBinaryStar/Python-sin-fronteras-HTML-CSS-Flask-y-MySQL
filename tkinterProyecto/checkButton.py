from tkinter import *

root = Tk()
root.title('Hola mundo: checkbox')

root.geometry('500x500')

var = StringVar()
var.set('Hey que tal?')

def mostrar():
    l = Label(root, text=var.get())
    l.pack()

c = Checkbutton(root, text='Soy un checkbox', variable=var, onvalue='Si', offvalue='Hey di que si!')
c.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()
