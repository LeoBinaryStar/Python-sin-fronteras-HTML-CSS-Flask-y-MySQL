from flask import Flask, request, url_for, redirect, abort, render_template
import mysql.connector

app = Flask(__name__)

midb = mysql.connector.connect(  # Se ingresan 4 valores de la BD host, user, password y database.
    host='localhost',
    user='LeoMontes',
    password='BaseLeo03@',
    database='prueba'
)

cursor = midb.cursor(dictionary=True)


@ app.route('/')
def index():
    return "Hola Mundo"

# Get, Post, Put, Delete


@ app.route('/post/<post_id>', methods=['GET', 'POST'])
def Uno(post_id):
    if request.method == 'GET':
        return "El post del id es: " + post_id
    else:
        return 'Este es otro metodo y no GET'


@ app.route('/Dos', methods=['POST', 'GET'])
def Dos():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    print(usuarios)
    # abort(401) #Para abortar acciones del ususario
    # 401 El servidor no pudo verificar que usted está autorizado para acceder a la URL solicitada. O proporcionó las credenciales incorrectas (por ejemplo, una contraseña incorrecta) o su navegador no sabe cómo proporcionar las credenciales requeridas.
    # 403 No tienes permiso para acceder al recurso solicitado. Está protegido contra lectura o el servidor no lo puede leer.
    # return redirect(url_for('index', post_id=2))  # retorna a un url indicado.
    # return render_template('Otro.html') #Retorna una pagina establecida en la carpeta.
    """ Archivo Json
    return {
         "username": 'Leonardo Montes',
         "email": 'leonardo.montes.barajas@gmail.com'
     }
    """
    return render_template('Otro.html', usuarios=usuarios)


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', mensaje='Hola Bienvenido')


@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        edad = request.form['edad']
        # Se separa por seguridad a que el cliente realice consultas sql.
        sql = "insert into Usuario (username, email, edad) values (%s, %s, %s)"
        values = (username, email, edad)
        cursor.execute(sql, values)
        midb.commit()
        return redirect(url_for('Dos'))
    return render_template('crear.html')
