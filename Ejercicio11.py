prod1=input("Ingrese el nombre del producto 1: ")
prec1=int(input(f"Ingrese el precio del {prod1}: "))
cant1=int(input(f"Ingrese la cantidad del {prod1}: "))
prod2=input("Ingrese el nombre del producto 2: ")
prec2=int(input(f"Ingrese el precio del {prod2}: "))
cant2=int(input(f"Ingrese la cantidad del {prod2}: "))
prod3=input("Ingrese el nombre del producto 3: ")
prec3=int(input(f"Ingrese el precio del {prod3}: "))
cant3=int(input(f"Ingrese la cantidad del {prod3}: "))
sub=((prec1*cant1)+(prec2*cant2)+(prec3*cant3))
iva=sub*0.08
total=sub+iva
print(f"total a pagar : $ {total}")

#nombre=input("ingrese el nombre: ")
#convertir en mayuscula 
#5print(nombre.upper())
#5print(nombre.title())
#para contar letras
#print(f"la variable {nombre} tiene {len(nombre)} caracteres")
#para raiz
#2**2-4


