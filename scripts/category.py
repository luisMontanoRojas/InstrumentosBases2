ffrom pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['musicalInstrumentsShop']

collectionCategory = db['category']

collectionCategory.insert_many([
{
    "nombre": "Piano Digital",

};
{
    "nombre": "Guitarra Electrica"

};
{
    "nombre":"Bateria Completa"

};
{
    "nombre":"Flauta"

};
{
    "nombre":"Violin"

};

])
