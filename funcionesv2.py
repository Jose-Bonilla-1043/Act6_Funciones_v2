print("Mas sobre funciones")
#  Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s

def rest(a2,b2):
    r=a2-b2
    return r

def div(a3,b3):
    d=a3/b3
    return d

def mul(a4,b4):
    m=a4*b4
    return m
#Llamando a funciones
print("---Calculando suma---")
n1=int(input("Ingresa el primer numero "))
n2=int(input("ingresa el segundo numero "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} = {suma}")

print("")
print("---Calculando resta---")
n3=int(input("Ingresa el primer numero "))
n4=int(input("ingresa el segundo numero "))
resta=rest(n3,n4)
print(f"La resta de {n3} - {n4} = {resta}")

print("")
print("---Calculando division---")
n5=int(input("Ingresa el primer numero "))
n6=int(input("ingresa el segundo numero "))
divicion=div(n5,n6)
print(f"La division de {n5} / {n6} = {divicion}")

print("")
print("---Calculando multiplicacion---")
n7=int(input("Ingresa el primer numero "))
n8=int(input("ingresa el segundo numero "))
multiplicacion=mul(n7,n8)
print(f"La multiplicacion de {n7} * {n8} = {multiplicacion}")