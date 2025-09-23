payasos=""
muñecas=""

payasos=int(input("Cantidad de payasos vendidos: "))
muñecas=int(input("Cantidad de muñecas vendidas: "))
#proceso
totalpeso=((payasos*112)+(muñecas*75))
#salida

print(f"Total de payasos vendidos:{payasos} total de muñecas vendidas {muñecas} total peso de paquete: {totalpeso}")