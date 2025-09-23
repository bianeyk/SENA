# calcular el area del tringulo y muestre su resultado.
#iniciar variables
base=""
altura=""
area=""

base=float(input("Digite la base: "))
altura=float(input("Digite la altura: "))
#proceso
area=(base*altura)/2
#salida
print("El area del triangulo de base:{} y altura {} es: {}".format(base,altura,area))
print("El area del triangulo de base:%s y altura %s es: %s"%(base,altura,area))
print(f"El area del triangulo de base:{base} y altura {altura} es: {area}")

