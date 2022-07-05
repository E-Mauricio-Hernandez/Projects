from time import time

n = 955234435456443543645645665756734565456763445654757556546
tiempo_inicial = time()
valores = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
valor = ''
while n != 0:
	r = n % 16
	valor = valores[r] + valor
	n = n // 16

tiempo_final = time()
print('primera forma:', tiempo_final - tiempo_inicial)
