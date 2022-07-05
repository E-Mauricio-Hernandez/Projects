numero = 'FF'
valores = {
	'0': 0,
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5, 
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'A': 10,
	'B': 11,
	'C': 12,
	'D': 13,
	'E': 14,
	'F': 15
}

resultado = 0
for pos in range(len(numero)):
	resultado = resultado + (valores[numero[len(numero) - 1 - pos]] * (16 ** pos))
print(resultado)