# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-03-11
# RLAB-23-02-09-0044-2
#

# Advertencia
print("!!! Los valores ingresados deben ser enteros y sin separador de millares ¡¡¡")

# Definicion de variables
P = int(input("Ingrese precio de suscripción $: "))
Unorm = int(input("Ingrese número de usuarios normales: "))
Uprem = int(input("Ingrese número de usuarios premium: "))
GT = int(input("Ingrese el gasto total $: "))

# Calculamos
UT = P*(Unorm+(Uprem*1.5))-GT

# Imprimir resultados
print(f"La rentabilidad es: ${UT}")