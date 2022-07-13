"""Al mismo tiempo hay una serie de reglas de facturación:

* Los días miércoles todos los alquileres tienen una bonificación de 50 pesos.

* Si quien alquila es una empresa (cuit empieza con 26) tiene un descuento del 5% como 
parte de la política de fidelización de clientes

* Si el auto es devuelto luego de finalizado el tiempo establecido al momento de alquiler, 
se cobra un recargo del 100%.
"""
#ejercicio de POO

class Alquiler:
    def __init__(self, tipo, cuit, horas, dias = 0, kilometros = 0, miercoles = 0):
        self.tipo = tipo
        self.cuit = cuit
        self.horas = horas
        self.dias = dias
        self.kilometros = kilometros
        self.miercoles = miercoles
        self.precio = 0
        self.bonificacion = 0
        self.descuento = 0
        self.recargo = 0
        self.total = 0
        self.calcularPrecio()
        self.calcularBonificacion()
        self.calcularDescuento()
        self.calcularRecargo()
        self.calcularTotal()

    def __str__(self):
        return f"Tipo: {self.tipo}\nCuit: {self.cuit}\nHoras: {self.horas}\nDias: {self.dias}\nKilometros: {self.kilometros}\nMiercoles: {self.miercoles}\nPrecio: {self.precio}\nBonificación: {self.bonificacion}\nDescuento: {self.descuento}\nRecargo: {self.recargo}\nTotal: {self.total}"
        
    def calcularPrecio(self):
        if self.tipo == 'Horas':
            self.precio = self.horas * 100
        elif self.tipo == 'Dias':
            self.precio = self.dias * 2000
        elif self.tipo == 'Kilometros':
            self.precio = 100 + (self.kilometros * 10)

    def calcularBonificacion(self):
        if self.miercoles > 0:
            self.bonificacion = 50

    def calcularDescuento(self): # [inicio, fin, paso]
        if self.cuit[0:2] == '26':
            self.descuento = self.precio * 0.05

    def calcularRecargo(self):
        if self.tipo == 'Kilometros':
            self.recargo = self.precio

    def calcularTotal(self):
        self.total = (self.precio + self.recargo) - (self.bonificacion + self.descuento)


aa = Alquiler('Horas', '20345534342', 5)
print(aa)

print()

bb = Alquiler('Dias', '26345534342', 0, 5)
print(bb)

print()

cc = Alquiler('Kilometros', '2343253456', 0, 2, 100, 1)
print(cc)

dd = Alquiler('Dias', '2601032213', 10, 0, 10, 2)
print(dd)

print()

gg = Alquiler('Horas', '26346538344', 0, 0, 1 )
print(gg)

print()

ee = Alquiler('Dias', '2643253456', 1, 3.5, 25.5, 20.5)
print(ee)