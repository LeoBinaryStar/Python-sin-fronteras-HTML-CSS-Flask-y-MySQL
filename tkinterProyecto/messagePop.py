from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')

#def click():
    #messagebox.showwarning('Popup', 'Hola mundo!')

#def click():
    #messagebox.showinfo('Popup', 'Hola mundo!')

#def click():
    #messagebox.showerror('Popup', 'Hola mundo! :c')

#Devuelve si o no, pero no en Boolean
#def click():
    #respuesta = messagebox.askquestion('Popup', 'Hola mundo!')
    #if respuesta == 'yes':
        #messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
    #else:
         #messagebox.showinfo('Respuesta', 'la respuesta fue :c ' + respuesta)

#Devuelve boolean
def click():
     respuesta = messagebox.askokcancel('Hola mundo!', 'Desea realizar acción?')
     if respuesta:
         messagebox.showinfo('Respuesta', 'la respuesta fue OK')
     else:
         messagebox.showinfo('Respuesta', 'la respuesta fue cancelar')


btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()
