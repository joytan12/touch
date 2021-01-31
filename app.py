from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/touch.db' 

db = SQLAlchemy(app)
 
"""
port = "5000"
ip_run = "192.168.0.4"
ip = "http://192.168.0.4:5000"
"""
#-------database---------#

class Usuarios (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    correo = db.Column(db.String(120), nullable=False)
    clave = db.Column(db.String(20), nullable=False)

class Productos (db.Model):
    ip = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False) 
    descripcion = db.Column(db.String(200), unique=True,)
    precio = db.Column(db.Integer)


@app.route('/', methods=['GET'])
def index():
    return render_template('principal.html')

@app.route('/busqueda', methods=['GET']) 
def busqueda():
    return render_template('articulos.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/editor',)

if __name__ == '__main__':
    app.run(debug=True)