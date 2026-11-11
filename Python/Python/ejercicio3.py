# Ejercicio 3 Tipos de variables
nombre = "Carlos"
apellidos = "Rojas Guevara"
nombre_completo = nombre + " " + apellidos
edad = 16
vivo = True

# Muestro los tipos de variables
print("Tipo de variable nombre_completo:", type(nombre_completo))
print("Tipo de variable edad:", type(edad))
print("Tipo de variable vivo:", type(vivo))

# Muestro por pantalla la presentacion de la persona
print("\n\t********************************\n")
print("\tCarta de presentación\t")
print("\tMe llamo", nombre_completo, "y tengo", edad, "años.\n")
print("\t********************************\n")