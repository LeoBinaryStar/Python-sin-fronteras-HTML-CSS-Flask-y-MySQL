from tkinter import *
import sqlite3

root = Tk()
root.title('Hola mundo: Todo-list')
root.geometry('500x500')

conn = sqlite3.connect('todo.db')

c = conn.cursor()

#A continuación se crea una tabla en caso de no existir esta misma,
#Y la hora de creación.
c.execute("""
    CREATE TABLE if not exists todo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description TEXT NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

conn.commit()


def remove(id):
    def _remove():
        c.execute("DELETE FROM todo WHERE id = ?", (id, ))
        conn.commit()
        render_todos()
    return _remove

#Evita que el id sea siempre el ultimo. Se encapsulan.
#Currying!
def complete(id):
    def _complete():
        todo = c.execute("SELECT * from todo WHERE id = ?", (id, )).fetchone()
        c.execute("UPDATE todo SET completed = ? WHERE id = ?", (not todo[3], id))
        conn.commit()
        render_todos()
    return _complete

#Extraer todas las tareas que ya han sido guardados.
def render_todos():
    #Se recibe la lista de elementos.
    rows = c.execute("SELECT * FROM todo").fetchall()
    print(rows)

    for widget in frame.winfo_children():
        widget.destroy()
        
    for i in range(0, len(rows)):
        id = rows[i][0]
        completed = rows[i][3]
        description = rows[i][2]
        #Anchor alinea hacia la dirección establecida.
        color = '#555555' if completed else'#ffffff'
        l = Checkbutton(frame, text=description, fg=color, width=42, anchor='w', command=complete(id))
        l.grid(row=i, column=0, sticky='w')
        btn = Button(frame, text='Eliminar', command=remove(id))
        btn.grid(row=i, column=1)
        l.select() if completed else l.deselect()

#Se define la función con la que agregará tareas.
def addTodo():
    todo = e.get()
    #Este ciclo if evita repetir un todo existente.
    if todo and todo!=" ":
        c.execute("""
                  INSERT INTO todo (description, completed) VALUES (?, ?)
                  """, (todo, False))
        conn.commit()
        e.delete(0, END)
        render_todos()
    else:
        pass
l= Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar')
btn.grid(row=0, column=2)

frame = LabelFrame(root, text='Mis tareas :D', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', pady=5)

e.focus()

root.bind('<Return>', lambda x: addTodo())
render_todos()
root.mainloop()
