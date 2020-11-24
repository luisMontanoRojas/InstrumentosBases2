from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['musicalInstrumentsShop']
collectionProducts = db['products']

collectionProducts.insert_many([
{
    "nombre" : "Yamaha P-45B",
    "precio" : 408,
    "descripcion" : "El Piano Digital Yamaha P-45 cuenta con un teclado de martillos graduados estándar (GHS). El tacto y la sensibilidad del teclado cambia gradualmente.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/77001-thickbox_default/yamaha-p45b.jpg",
    "imageurl2" : "https://multisononline.com/77003-thickbox_default/yamaha-p45b.jpg",
    "categoria" : "Piano Digital",
    "vistas" : 100,
    "cantidad_vendidas" : 15 
},
{
    "nombre" : "Yamaha Dgx-660 Wh",
    "precio" : 748,
    "descripcion" : "El Piano digital YAMAHA DGX660WH es un piano digital de 88 teclas con entrada de micro y sonidos de excelente calidad Yamaha.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/48373-thickbox_default/yamaha-dgx660-wh.jpg",
    "imageurl2" : "https://multisononline.com/48374-thickbox_default/yamaha-dgx660-wh.jpg",
    "categoria" : "Piano Digital",
    "vistas" : 100,
    "cantidad_vendidas" : 15
},
{
    "nombre" : "Fender Vintera Road Worn 60S Stratocaster PF LPB",
    "precio" : 1145,
    "descripcion" : "La serie Vintera Road Worn de Fender recrea los módelos clásicos de la marca, que destacaban por su aspecto, sensación, construcción y sonido incomparables.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/80563-thickbox_default/fender-vintera-road-worn-60s-stratocaster-pf-lpb.jpg",
    "imageurl2" : "https://multisononline.com/80562-thickbox_default/fender-vintera-road-worn-60s-stratocaster-pf-lpb.jpg",
    "categoria" : "Guitarra Electrica",
    "vistas" : 100,
    "cantidad_vendidas" : 15 
},
{
    "nombre" : "Fender Vintera Road Worn 60S Stratocaster PF FMG ",
    "precio" : 1149,
    "descripcion" : "La serie Vintera Road Worn de Fender recrea los módelos clásicos de la marca, que destacaban por su aspecto, sensación, construcción y sonido incomparables.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/80567-thickbox_default/fender-vintera-road-worn-60s-stratocaster-pf-fmg.jpg",
    "imageurl2" : "https://multisononline.com/80566-thickbox_default/fender-vintera-road-worn-60s-stratocaster-pf-fmg.jpg",
    "categoria" : "Guitarra Electrica",
    "vistas" : 100,
    "cantidad_vendidas" : 15  
},
{
    "nombre" : "Pearl Exl725S Export Lacquer Rock Cherry 22",
    "precio" : 839,
    "descripcion" : "Nuestro set de baterias Pearl Export Lacquer Rock de 22 se ajusta a las necesidades mas exigentes. Acabado en madera natural en tonos rojos.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/46000-thickbox_default/pearl-exl725s-export-lacquer-rock-cherry-22.jpg",
    "imageurl2" : "https://multisononline.com/46001-thickbox_default/pearl-exl725s-export-lacquer-rock-cherry-22.jpg",
    "categoria" : "Bateria Completa",
    "vistas" : 100,
    "cantidad_vendidas" : 15
},
{
    "nombre" : "Yamaha Rydeen RDP0F5 Silver Glitter ",
    "precio" : 459,
    "descripcion" : "Yamaha Rydeen. Es el kit ideal para cualquier baterista principiante o de nivel intermedio, obtendrás un sonido mejorado y equilibrado.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/62783-thickbox_default/yamaha-rydeen-rdp0f5-silver-glitter.jpg",
    "imageurl2" : "https://multisononline.com/62784-thickbox_default/yamaha-rydeen-rdp0f5-silver-glitter.jpg",
    "categoria" : "Bateria Completa",
    "vistas" : 100,
    "cantidad_vendidas" : 15
},
{
    "nombre" : "Yamaha Yfl-262",
    "precio" : 577,
    "descripcion" : "YAMAHA YFL-262 es el nuevo modelo mejorado de la gama de flautas para estudiantes de esta reconocida marca Japonesa. Platos Abiertos, Desalineada.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/51056-thickbox_default/yamaha-yfl262.jpg",
    "imageurl2" : "https://multisononline.com/54806-thickbox_default/yamaha-yfl262.jpg",
    "categoria" : "Flauta",
    "vistas" : 100,
    "cantidad_vendidas" : 15
},
{
    "nombre" : "J.Michael Flu-450-S",
    "precio" : 225,
    "descripcion" : "Flauta travesera con pata de DO, recomendada para niños en temprana edad, con platos cerrados y desalineados.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/501-thickbox_default/jmichael-flu450s.jpg",
    "imageurl2" : "https://multisononline.com/15700-thickbox_default/jmichael-flu450s.jpg",
    "categoria" : "Flauta",
    "vistas" : 100,
    "cantidad_vendidas" : 15
},
{
    "nombre" : "Gewa Germania 10 4/4",
    "precio" : 820,
    "descripcion" : "GEWA GERMANIA 10 4/4 es un violín Luthier de gran calidad, fabricado en Alemania.",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/50442-thickbox_default/gewa-germania-10-44.jpg",
    "imageurl2" : "https://multisononline.com/50443-thickbox_default/gewa-germania-10-44.jpg",
    "categoria" : "Violin",
    "vistas" : 100,
    "cantidad_vendidas" : 15
},
{
    "nombre" : "Sielam Espressivo 1/2 Violín",
    "precio" : 215,
    "descripcion" : "SIELAM ESPRESSIVO 1/2. Violín de Estudio.Viólin de madera maciza, acabado sombra, diapasón de ébano, montado. Accesorios de azufaifa (clavijas, barbada y boton)..",
    "cantidad" : 20,
    "imageurl1" : "https://multisononline.com/44435-thickbox_default/sielam-espressivo-12-violin.jpg",
    "imageurl2" : "https://multisononline.com/44436-thickbox_default/sielam-espressivo-12-violin.jpg",
    "categoria" : "Violin",
    "vistas" : 100,
    "cantidad_vendidas" : 15
}
])