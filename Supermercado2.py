"""
ejercicio de POO2

Suponga ahora que el descuento a aplicar en cada producto de primera necesidad puede ser distinto 
y se debe poder definir al momento de crear el mismo. 
Por ejemplo, el arroz puede ser un producto de primera necesidad con un descuento del 8%, 
mientras que leche podría ser otro producto de primera necesidad con un decuento del 11%. 
Esto es sólo un ejemplo. 
El descuento a aplicar en cada producto de primera necesidad debe ser configurable al momento de crearlo.

Implementar un programa en Python basado en el anterior que ahora incorpore este nuevo requerimiento.
"""

class Producto:
    def __init__(self, nombre, precio, preciosCuidados = False, primeraNecesidad = 0):
        self.nombre = nombre
        self.precio = precio
        self.pC = preciosCuidados
        self.pN = primeraNecesidad
    
    def __str__(self):
        return f'{self.nombre} | $ {self.precio} | {"Precios Cuidados: SI" if self.pC else "Precios Cuidados: NO"} | {"Primera Necesidad: SI" if self.pN != 0 else "Primera Necesidad: NO"}'

    def precioFinal(self):
        if self.pN > 0:
            return self.precio * (1 - self.pN / 100)
        else:
            return self.precio

class Supermercado:
    def __init__(self, nombre, direccion) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.productos = []

    def __str__(self):
        return f'{self.nombre} | {self.direccion}'
    
    def agregarProducto(self, nombre, precio, preciosCuidados = False, primeraNecesidad = 0):
        producto = Producto(nombre, precio, preciosCuidados, primeraNecesidad)
        self.productos.append(producto)
    
    def mostrarTotal(self):
        cantidad = 0
        sumaTotal = 0
        for producto in self.productos:
            cantidad += 1
            sumaTotal += int(producto.precioFinal())
        print(f'Cantidad: {cantidad} | Suma Total: {sumaTotal}')


los_chinos = Supermercado('Los Chinos', 'Av. Hernandarias 1950')
print(los_chinos)

los_chinos.agregarProducto('Sprite', 500, True, 8)
los_chinos.agregarProducto('CocaCola', 500, True, 11)
los_chinos.agregarProducto('Pan', 200)
los_chinos.mostrarTotal()
