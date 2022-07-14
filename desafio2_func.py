#Crea una tupla con los factores que más afectan a los mares. Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino muestra un mensaje de error.
#El programa termina cuando el usuario introduce un cero.


factores = "", "plastico", "carton", "vidrio", "petroleo"

print("aprendiendo sobre contaminacion")

opcion = int(input("ingresar un numero del  1 al 4"))

while opcion != 0:
    if opcion > len(factores):
        print("error")
    else:
        print(factores[opcion])
    
    opcion = int(input("INGRESE UN NUMERO PARA CONTINUAR O 0 PARA SALIR"))