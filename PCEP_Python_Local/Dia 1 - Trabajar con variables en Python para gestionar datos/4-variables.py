#Intercambiar valor, variable "a" dentra el valor de la variable "b" y viciversa.

a = input("a: ")
b = input("b: ")


####################################
#El uso de una tercera variable "x" nos ayuda a guardar el valor de una variable en este caso "a" , y poder
#Lograr el intercambio de valores de variables.
x = a
a = b
b = x

####################################

print("a: " + a)
print("b: " + b)