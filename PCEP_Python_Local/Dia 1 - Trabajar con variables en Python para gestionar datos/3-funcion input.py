# Usando variable, funcion input(), y funcion dentro de otra funcion, ej: len dentro de print.
# la funcion input() por defecto espera el ingreso de una palabra o cadena que es un dato de tipo string.
# la funcion len() calcula el largo de un string y devuelve un valor integer

name = input("Cual es tu nombre version1?: ")
print(len(name))


# Python permite anidar funciones en una misma linea. La anidacion debe tener logica osea y se lee desde dentro hacia afuera.
# primero ingreso un string con input()
# segundo calculo el largo del string con len()
# tercero muestro el resultado por consola con print()

print(len(input("Cual es tu nombre version2: ")))

