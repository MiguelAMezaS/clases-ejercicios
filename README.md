class Instrumento:
    def __init__(self, precio):
        self.precio = precio
    
    def precio(self):
        print("el precio de este instrumento es: $", self.precio)

class Guitarra(Instrumento):
    def __init__(self, tipo_cuerda, precio):
        Instrumento.__init__(self, precio)
        self.tipo_cuerda = tipo_cuerda
        self.precio = precio

Instrumento1 = Guitarra("la guitarra tiene cuerda gruesa", "$5000")
print(Instrumento1.tipo_cuerda)
print(Instrumento1.precio)
