from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['musicalInstrumentsShop']
collectionProducts = db['sales']

collectionProducts.insert_many([
{
    "saleId" : 1,
    "productsCount": 3,
    "listIdProducts" : [1,3,6],
    "totalPrice" : 256,
    "address" : "Av. America #25"
},
{
    "saleId" : 2,
    "productsCount": 5,
    "listIdProducts" : [1,2,3,6,9],
    "totalPrice" : 159,
    "address" : "Calle Tarija #59"
},
{
    "saleId" : 3,
    "productsCount": 2,
    "listIdProducts" : [1,6],
    "totalPrice" : 26,
    "address" : "Av. Blanco Galindo #53"
},
{
    "saleId" : 4,
    "productsCount": 1,
    "listIdProducts" : [6],
    "totalPrice" : 15,
    "address" : "Av. G. Rene Moreno y Av. America"
},
{
    "saleId" : 5,
    "productsCount": 7,
    "listIdProducts" : [2,5,7,9,11,15,22],
    "totalPrice" : 1290,
    "address" : "Torres Sofer"
}])