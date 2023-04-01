from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

#imagen = Image.open('marnie.png')
#imagen.show()

img = ImageTk.PhotoImage(Image.open('marnie.png'))
l = Label(image=img)
l.pack()

root.mainloop()
