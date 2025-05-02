#2. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, 
# la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto,
#  ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que
#  entrega en un embarque,considerando lo siguiente:
#Si es de tipo A, se le cargan 20¢ al precio inicial cuando es de tamaño 1; y 30¢ si es de tamaño 2.
#Si es de tipo B, se rebajan 30¢ cuando es de tamaño 1, y 50¢ cuando es de tamaño 2. Realice un algoritmo
#  para determinar la ganancia obtenida
#creacion de variables
tipo_uva=0
tamano_uva=0
precio_inicial=0
kilos=0


# Entrada de datos
tipo_uva = input("Ingrese el tipo de uva (A o B): ").upper()
tamano_uva = int(input("Ingrese el tamaño de la uva (1 o 2): "))
precio_inicial = float(input("Ingrese el precio inicial por kilo de uva: "))
kilos = float(input("Ingrese la cantidad de kilos entregados: "))


# Determinar el ajuste según el tipo y tamaño de la uva
precio = 0

if tipo_uva == "A":
    if tamano_uva == 1:
        precio = 0.20
    elif tamano_uva == 2:
        precio = 0.30
elif tipo_uva == "B":
    if tamano_uva == 1:
        precio = -0.30
    elif tamano_uva == 2:
        precio = -0.50
else:
    print("Tipo de uva inválido.")
    
# Calcular el precio final por kilo
precio_final = precio_inicial + precio

# Calcular la ganancia total
ganancia = precio_final * kilos

# Mostrar el resultado
print("Precio final por kilo: "precio_final)
print("Ganancia total del productor: "ganancia)
