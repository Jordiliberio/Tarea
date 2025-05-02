# Realizar un diagrama de flujo que permita verificar la edad exacta de una persona, en años, meses y días,
#  y presentar por pantalla, para lo cual debe de permitir ingresar por teclado la fecha actual 
# y la fecha de nacimiento de la persona.
# Ingreso de fecha actual
dia_act = int(input("Ingrese el día actual: "))
mes_act = int(input("Ingrese el mes actual: "))
año_act = int(input("Ingrese el año actual: "))

# Ingreso de fecha de nacimiento
dia_nac = int(input("Ingrese el día de nacimiento: "))
mes_nac = int(input("Ingrese el mes de nacimiento: "))
año_nac = int(input("Ingrese el año de nacimiento: "))

# Inicialización de variables
años = año_act - año_nac
meses = mes_act - mes_nac
días = dia_act - dia_nac

# Ajustes si el día actual es menor que el de nacimiento
if días < 0:
    meses -= 1
    días += 30  # aproximación de 30 días por mes

# Ajustes si el mes actual es menor que el de nacimiento
if meses < 0:
    años -= 1
    meses += 12

# Mostrar resultado
print("Edad exacta:")
print("Años:", años)
print("Meses:", meses)
print("Días:", días)

