from tkinter import *

root = Tk()
root.title('Hola Mundo')

r = IntVar()
r.set('2')

Equipo = [
    ('Natsuki', 'Natsuki'),
    ('Sayori', 'Sayori'),
    ('Monika', 'Monika'),
    ('Yuri', 'Yuri')
]

equipo = StringVar()
equipo.set('Elige')

for text, integrante in Equipo:
    Radiobutton(root, text=text, variable=equipo, value=integrante).pack()

l = Label(root, textvariable=equipo)
l.pack()

root.mainloop()
