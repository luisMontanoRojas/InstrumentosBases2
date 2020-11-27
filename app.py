from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.musicalInstrumentsShop
products = db.products
carrito=[]

@app.route('/')
def listaTodos():
    products_l = products.find()
    return render_template('home.html', products=products_l)

@app.route('/pianos')
def listaPianos():
    products_l = products.find({"categoria":"Piano Digital"})
    return render_template('home.html', products=products_l)

@app.route('/guitarras')
def listaGuitarras():
    # //esto se cambiara y se pondra sin acentp
    products_l = products.find({"categoria":"Guitarra Eléctrica"})
    return render_template('home.html', products=products_l)

@app.route('/baterias')
def listaBaterias():
    # //esto se cambiara y se pondra sin acentp
    products_l = products.find({"categoria":"Batería Completa"})
    return render_template('home.html', products=products_l)

@app.route('/flautas')
def listaFlautas():
    products_l = products.find({"categoria":"Flauta Travesera"})
    return render_template('home.html', products=products_l)

@app.route('/violines')
def listaViolines():
    products_l = products.find({"categoria":"Violin"})
    return render_template('home.html', products=products_l)

@app.route('/contact')
def about():
    return render_template('contact.html')

@app.route('/AddCarrito',methods=['POST'])
def addCarrito():
    name =request.values.get("name")
    carrito.append(products.find({"name":name}))
    products_l = products.find()
    print (name)
    return render_template('home.html', products=products_l)

if __name__ == '__main__':
    app.run(debug=True)