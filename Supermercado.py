"""
Un supermercado maneja el catálogo de los productos que vende. 
De cada producto se conoce su nombre, precio, y si el mismo es parte del programa Precios Cuidados o no. 
Por defecto, el producto no es parte del programa, a menos que se especifique lo contrario.

Para ayudar a los clientes, el supermercado quiere realizar descuentos en productos de Primera Necesidad. 
Es por eso que al calcular el precio de un producto de Primera Necesidad, se aplica un descuento del 10%. 

Es decir:

precioProductoPrimeraNecesidad = precio * 0.9

El supermercado, del cual se conoce el nombre y la dirección, desea conocer la cantidad total de 
productos que comercializa y la suma total de los precios de los mismos.
"""

class Producto:
    def __init__(self, nombre, precio, preciosCuidados = False, primeraNecesidad = False):
        self.nombre = nombre
        self.precio = precio
        self.pC = preciosCuidados
        self.pN = primeraNecesidad
    
    def __str__(self):
        return f'{self.nombre} | $ {self.precio} | {"Precios Cuidados: SI" if self.pC else "Precios Cuidados: NO"} | {"Primera Necesidad: SI" if self.pN else "Primera Necesidad: NO"}'

    def precioFinal(self):
        if self.pN:
            return self.precio * 0.9
        else:
            return self.precio
# desea conocer la cantidad total de 
# productos que comercializa y la suma total de los precios de los mismos.

class Supermercado:
    def __init__(self, nombre, direccion) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.productos = []

    def __str__(self):
        return f'{self.nombre} | {self.direccion}'
    
    def agregarProducto(self, nombre, precio, preciosCuidados = False, primeraNecesidad = False):
        producto = Producto(nombre, precio, preciosCuidados, primeraNecesidad)
        self.productos.append(producto)
    
    def mostrarTotal(self):
        cantidad = 0
        sumaTotal = 0
        for producto in self.productos:
            cantidad += 1
            sumaTotal += int(producto.precioFinal())
        print(f'Cantidad: {cantidad} | Suma Total: {sumaTotal}')


gaseosa = Producto('Sprite', 500, True, True)
los_chinos = Supermercado('Los Chinos', 'Av. Hernandarias 1950')

print(gaseosa)
print(gaseosa.precioFinal())

print(los_chinos)
los_chinos.agregarProducto('Sprite', 500, True, True)
los_chinos.agregarProducto('CocaCola', 500, True)
los_chinos.agregarProducto('Pan', 200)

los_chinos.mostrarTotal()
