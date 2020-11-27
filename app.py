from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.musicalInstrumentsShop
products = db.products
carrito=db.carrito
ventas=db.ventas
idVenta=0

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
    nombre =request.values.get("nombre")
    carrito.insert(products.find({"nombre":nombre}))
    products.update({"nombre":nombre},{'$inc':{'cantidad':-1}})
    products_l = products.find()
    return render_template('home.html', products=products_l)

@app.route('/verCarrito')
def listarTodoCarrito():
    products_l = carrito.find()
    return render_template('carrito.html', products=products_l)

@app.route('/vaciarCarrito')
def vaciarCarrito():
    carrito.remove()
    return listaTodos()

@app.route('/Compra')
def venta():
    idVenta= + 1
    #producto2=list(carrito.find())
    ventas.insert([
    {
     "idVenta" :idVenta,
     "listaProductos": [list(carrito.find())]
    }])
    
    venta_1=ventas.find()
    carrito.aggregate([{"$group":{"_id":None, "totalPagar":{"$sum":"$precio"}}}])
    products_l=carrito.find()
    carrito_1=carrito.find()
    return render_template('venta.html', ventas=venta_1,products=products_l,carritos=carrito_1)


if __name__ == '__main__':
    app.run(debug=True)