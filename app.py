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

    instrumentos=carrito.find()
    totalPagar = 0
    for i in instrumentos:
        totalPagar = totalPagar + i["precio"]
    print (totalPagar)
    products_l=carrito.find()
    return render_template('venta.html', ventas=totalPagar,products=products_l)

@app.route("/search", methods=["GET"])
def search():
    key=request.values.get("key")
    products_l=products.find({"nombre":(key)})
    return render_template('home.html',products=products_l)

@app.route('/mas_vistos')
def listaMasVistos():
    products_l = products.find()
    products_lO = sorted(products_l, key=lambda product: product['vistas'], reverse=True)
    return render_template('home.html', products=products_lO)

@app.route('/mas_vendidos')
def listaMasVendidos():
    products_l = products.find()
    products_lO = sorted(products_l, key=lambda product: product['cantidad_vendidas'], reverse=True)
    return render_template('home.html', products=products_lO)


if __name__ == '__main__':
    app.run(debug=True)