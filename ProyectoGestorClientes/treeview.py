from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Hola mundo: Treeview')

tree = ttk.Treeview('root')
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')

#Se especifican las columnas
#tree.column('#0')
#Para no mostrar el ID
tree.column('#0', width=0, stretch=NO)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

#tree.heading('#0', text='id')
tree.heading('#0')
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=0)

tree.insert('', END, 'IdentificadorUno', values=('Uno','Dos','Tres'), text='Cliente feliz')
tree.insert('', END, 'IdentificadorDos', values=('Cuatro','Cinco','Seis'), text='Cliente premium')
tree.insert('', END, 'IdentificadorTres', values=('4','5','6'), text='Hijo')
