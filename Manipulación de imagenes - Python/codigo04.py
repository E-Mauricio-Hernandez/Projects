def factorial(f):
	resultado = 1
	for n in range(1, f + 1):
		resultado = resultado * n

	return resultado

f = int(input('Ingrese Factorial a calcular: '))
print ('resultado =', factorial(f))
