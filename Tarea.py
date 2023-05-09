# Trabajo Practico X2.2
"""
# Actividad 3.1

lista = [] # Inicio la Lista vacia
i = 1 # Creo un Contador

for n in range(0,100): # Condicion For de 0 a 100
    lista.insert(i,i)
    i+= 1
    
print(lista) # Imprimo la lista entera en busca de buen funcionamiento
print("\n")

# Actividad 3.2
tupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre") # Creo la tupla con los meses del año
limit = 12 # Establesco un limite
print("Escriba el numero del més que desea ver ") # Le pide al usuario que ingrese el numero del més que desea ver
opcion = int (input()) # Introduce el valor anteriormente mencionado a opcion

if opcion <= limit: # Condicion Si la opcion no supera el limite
    print(tupla[opcion]) # Se Muestra el Mes seleccionado
else: # Condicion Sino se cumple lo Solicitado
    print("ERROR: EL NUMERO INGRESADO SUPERA EL LIMITE DE LA TUPLA") # Salta Mensaje de Error en caso de pasar el limite
print("\n") # Salto de Linea

# Actividad 3.3
listaTabMult = [] # Inicio la Lista
i2 = 0 # Inicio el Contador
print("Ingrese un numero para ver su tabla de multiplicar ") # Mensaje para que el usuario ingrese el numero para mostrarle su tabla de multiplicar
i = int(input()) # Input para ingresar el valor anteriormente mencionado

for n in range(0,11): # Inicio un For desde 0 a 10
    listaTabMult.insert(i2, i2) # Ingreso valores para la Lista
    listaTabMult[i2] = i*i2 # Modifico la Lista para hacer que se multiplique como en la tabla
    i2+= 1 # Aumento en 1 el contador

print(listaTabMult) # Imprimo la Lista
print("\n")

# Actividad 3.4

contactos = {} # Creamos un diccionario vacío para guardar los contactos

# Pedimos al usuario que ingrese los contactos
while True:
    nombre = input("Ingresa el nombre del contacto (o 'salir' para terminar): ")
    if nombre == 'salir':
        break
    telefono = input("Ingresa el número de teléfono: ")
    if nombre in contactos:
        print("El contacto ya existe. Por favor, ingresa un nombre diferente.")
    else:
        contactos[nombre] = telefono
        print("Contacto agregado.")

# Mostramos los contactos
print("Lista de contactos:")
for nombre, telefono in contactos.items():
    print(nombre + ": " + telefono)


# Actividad 4.1
# Pedir dos números enteros al usuario
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

# Determinar cuál es el número más pequeño y cuál es el número más grande
if num1 < num2:
  start_num = num1
  end_num = num2
else:
  start_num = num2
  end_num = num1

# Iterar desde el número más pequeño hasta el número más grande
for num in range(start_num, end_num+1):
  if num % 2 == 0:
    print(num, "es par")
  else:
    print(num, "es impar")


# Actividad 4.2
while True: # crea un bucle infinito, lo que significa que el código dentro del bucle se ejecutará una y otra vez hasta que se encuentre una instrucción break que lo interrumpa.
    num = input("Ingrese un número positivo: ") # pide al usuario que ingrese un número, y lo guarda en la variable num.
    if num.isdigit() and int(num) > 0: # verifica si num es un número positivo. 
        break # Si el número ingresado es un número positivo, la instrucción break rompe el bucle while y el programa continúa. Si el número ingresado no es un número positivo, se imprime un mensaje de error y el bucle while continúa.
    else: # se ejecuta si la instrucción if anterior es falsa, lo que significa que el número ingresado no es un número positivo. En este caso, se imprime un mensaje de error.
        print("Error: debe ingresar un número positivo.") 


# Actividad 4.3
while True: #  crea un bucle infinito
    num1 = int(input("Ingrese el primer número entero: ")) # pide al usuario que ingrese el primer número entero, lo convierte a un entero usando la función int(), y lo guarda en la variable num1
    num2 = int(input("Ingrese el segundo número entero: ")) # pide al usuario que ingrese el segundo número entero, lo convierte a un entero usando la función int(), y lo guarda en la variable num2.
    if num2 > num1: # verifica si num2 es mayor que num1. Si es así, la instrucción break rompe el bucle while y el programa continúa. Si num2 no es mayor que num1, se imprime un mensaje de error y el bucle while continúa.
        break 
    else: # se ejecuta si la instrucción if anterior es falsa, lo que significa que num2 no es mayor que num1. En este caso, se imprime un mensaje de error.
        print("Error: el segundo número debe ser mayor que el primero.") # Si el usuario ingresa dos números enteros y el segundo número es mayor que el primero, el programa sale del bucle while y continúa con la última instrucción print("Los números ingresados son:", num1, "y", num2)", que imprime los dos números ingresados por el usuario.
print("Los números ingresados son:", num1, "y", num2)
"""

# Actividad 4.4
num1 = int(input("Ingrese el primer número entero: "))  # Pedimos al usuario que ingrese el primer número y lo convertimos a un entero
num2 = int(input("Ingrese el segundo número entero: "))  # Pedimos al usuario que ingrese el segundo número y lo convertimos a un entero

if num1 < num2:  # Verificamos si el primer número es menor que el segundo
    for i in range(num1, num2+1):  # Si es así, usamos un bucle for para imprimir los números consecutivos de menor a mayor
        print(i, end=' ')
else:  # Si el primer número es mayor que el segundo, hacemos lo mismo pero intercambiando los números
    for i in range(num2, num1+1):
        print(i, end=' ')
