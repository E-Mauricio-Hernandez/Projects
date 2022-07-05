factorial = int(input('Ingrese Factorial a calcular: '))
resultado = 1


for n in range(1, factorial + 1):
	resultado = resultado * n

resultado = 1
n = 1
while n <= factorial:
	resultado = resultado * n
	n = n + 1 

print ('resultado =', resultado)
