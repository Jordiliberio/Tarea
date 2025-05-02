#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe 
# cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es 
# la siguiente: si son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos,
#  el costo es de$70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús 
# es de $4000.00, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago
# a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
# Inicializar variables
alumnos=0
costo_por_alumno = 0
pago_total = 0
# Entrada de datos
alumnos = int(input("Ingrese el número de alumnos que van al viaje: "))
# Determinar el costo según el número de alumnos
if alumnos >= 100:
    costo_por_alumno = 65.00
    pago_total = alumnos * costo_por_alumno
elif alumnos >= 50:
    costo_por_alumno = 70.00
    pago_total = alumnos * costo_por_alumno
elif alumnos >= 30:
    costo_por_alumno = 95.00
    pago_total = alumnos * costo_por_alumno
else:
    pago_total = 4000.00
    costo_por_alumno = pago_total / alumnos

# Mostrar resultados
print("Pago total a la compañía de autobuses: ",pago_total)
print("Cada alumno debe pagar: ",costo_por_alumno)
