from app import db, Usuarios, Categorias, Carrito, Articulos
#If need to drop
#db.drop_all()
#If need to create
#db.create_all()

usuario1 = Usuarios(username="diego",password="abcd1234",nombre="Diego",email="diego@example.com",admin=1)
usuario2 = Usuarios(username="carlos",password="abcd1234",nombre="Carlos",email="test@example.com")

db.session.add(usuario1)
db.session.add(usuario2)

categoria1 = Categorias(nombre="Prueba1")
categoria2 = Categorias(nombre="Prueba2")

db.session.add(categoria1)
db.session.add(categoria2)

articulo1 = Articulos(nombre="Prueba1", precio=10000, iva=0.19, descripcion="Producto de prueba 1", image="URL NOT FOUND", stock=20, id_categorias=1)
articulo2 = Articulos(nombre="Prueba2", precio=25000, iva=0, descripcion="Producto de prueba 2", image="URL NOT FOUND", stock=120, id_categorias=2)

db.session.add(articulo1)
db.session.add(articulo2)
db.session.commit()