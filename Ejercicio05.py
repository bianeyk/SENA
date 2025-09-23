peso=""
estatura=""

peso=float(input("Digite su peso en kl: "))
estatura=float(input("Digite su estatura en mt: "))
#proceso
imc=(peso/(estatura**2))
#salida

print(f"Tu índice de masa corporal es: {imc}")