class medicamentos:
       def __init__(self, id, nombre, precio, descripcion, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad

       def getId(self):
        return self.id

       def getnombre(self):
        return self.nombre

       def getPrecio(self):
        return self.precio


       def getDescripcion(self):
        return self.descripcion


       def getCantidad(self):
        return self.cantidad

 # metodos set----------------------------------------------


       def setId(self, id):
        self.id = id


       def setnombre(self, nombre):
        self.nombre = nombre


       def setPrecio(self, precio):
        self.nacimiento = precio

       def setDescripcion(self, descripcion):
        self.descripcion = descripcion

       def setCantidad(self, cantidad):
        self.cantidad= cantidad
   
        
