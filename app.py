import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# configuração
DATABASE = 'blog.db'
SECRET_KEY = 'pudim'

app = Flask(__name__)
app.config.from_object(__name__)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def antes_requisisao():
    g.bd = conectar_bd()

@app.teardown_request
def depois_request(exc):
    g.bd.close()

@app.route('/')
def exibir_entradas():
    return render_template('exibir_entradas.html')

@app.route('/hello')
def pagina_inicial():
    return "Hello World"
