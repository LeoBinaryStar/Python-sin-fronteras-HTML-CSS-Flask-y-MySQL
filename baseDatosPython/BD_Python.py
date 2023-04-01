import mysql.connector  # importa la librería de mysql
midb = mysql.connector.connect(  # Se ingresan 4 valores de la BD host, user, password y database.
    host='localhost',
    user='LeoMontes',
    password='BaseLeo03@',
    database='prueba'
)

"""Es el comando esencial para manipular la base de datos."""
cursor = midb.cursor()


"""Listar datos."""
# Se indica de donde tomará los datos.
cursor.execute('select * from Usuario')
# fetchone imprime el primer registro vs fetchall que muestra todos.
resultado = cursor.fetchall()
# Imprime el resultado.
print(resultado)


"""Listar datos."""
# Se indica de donde tomará los datos.
cursor.execute('select * from Usuario limit 1')
# fetchone imprime el primer registro vs fetchall que muestra todos.
resultado = cursor.fetchall()
# Imprime el resultado.
print(resultado)


"""Ver el contenido de las tablas. Es decir los datos que solicitan."""
#cursor.execute('show create table Usuario')


"""Insertar datos."""
# Se asigna que se solicitará a continuación.
#sql = 'insert into Usuario(email, username, edad) values (%s, %s, %s)'
# se solicitan los valores.
#values = ('correo@correo.com', 'nombreUsuario', 45)


""""Actualizar los datos."""
#sql = 'update Usuario set email = %s where id=%s'
#values = ('correito@correo.com', 4)
# Se ingresaran los datos a partir de la variable declarada "values".
#cursor.execute(sql, values)

""""Ejecuta la función."""
# commit() Es un método para tomar los datos y ejecutará la consulta de SQL a la base de datos.Si no se agrega no tendrá valides la ejecución
# midb.commit()
# print(cursor.rowcount)  # Indicará que el dato ha sido creado.


"""Eliminar datos."""
#sql = 'delete from Usuario where id = %s'
#values = (5, )
#cursor.execute(sql, values)
# midb.commit()
