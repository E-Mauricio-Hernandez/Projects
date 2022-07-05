import json
st = input("Ingrese su diccionario en formato JSON: ") 
midiccionario = json.loads(st)
a=input("Ingrese los codigos que desea comprar separados por espacio: ")
b=a.split(" ")
final=""
final2=0
for x in range (0, len(b)):
	if b[x] in midiccionario:	
		final=final+b[x]+" "
		final2=final2+midiccionario[b[x]]
print(final)
print(final2)