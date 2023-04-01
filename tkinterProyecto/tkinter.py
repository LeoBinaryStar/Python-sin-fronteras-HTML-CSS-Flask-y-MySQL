from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')

l1 = Label(root, text='Hola mundo mi primera etiqueta en TK')
l2 = Label(root, text='Bye mundo mi segunda etiqueta en TK')
l3 = Label(root, text='spacespacespace')

l1.grid(row=0, column=0)#Grid llama dentro de una fila y columna especifica.
l3.grid(row=1, column=1)
l2.grid(row=10, column=10)

#label.pack()#Llama a lo que ordenes ejemplo.pack()
root.mainloop()
