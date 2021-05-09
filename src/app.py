from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@dataclass
class Usuarios(db.Model):
    id:int
    username:str
    password:str
    nombre:str
    email:str
    admin:int
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    admin = db.Column(db.Integer, nullable=False, default=0)


@dataclass
class Categorias(db.Model):
    id:int
    nombre:str
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)


@dataclass
class Articulos(db.Model):
    id:int
    nombre:str
    precio:float
    iva:float
    descripcion:str
    image:str
    stock:str
    id_categorias:int
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    iva = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(80), unique=True, nullable=False)
    image = db.Column(db.String(250), nullable=False)
    stock = db.Column(db.Float, nullable=False)
    id_categorias = db.Column(db.Integer, db.ForeignKey(Categorias.id))


@dataclass
class Carrito(db.Model):
    id_articulos:int
    id_usuarios:int
    cantidad:int
    id_articulos = db.Column(db.Integer, db.ForeignKey(Articulos.id), primary_key=True)
    id_usuarios = db.Column(db.Integer, db.ForeignKey(Usuarios.id), primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    
@app.route("/users",methods=["GET"])
def usuarios():
    return jsonify(Usuarios.query.all())

@app.route("/products",methods=["GET"])
def articulos():
    return jsonify(Articulos.query.all())

@app.route("/categories",methods=["GET"])
def categorias():
    return jsonify(Categorias.query.all())

@app.route("/cart",methods=["GET"])
def carrito():
    return jsonify(Carrito.query.all())

if __name__ == "__main__":
    app.run(port=5000,host="0.0.0.0",debug=True)