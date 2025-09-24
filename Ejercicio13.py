la1=float(input("ingrese la medida del primer lado del triangulo: "))
la2=float(input("ingrese la medida del segundo lado del triangulo: "))
la3=int(input("ingrese la medida del tercer lado del triangulo: "))
s=(la1+la2+la3)/2
total=match.sqrt(s*((s-la1)*(s-la2)*(s-la3)))
totaltr=total**0.55



print(f"el area del triangulo es : {total}")
