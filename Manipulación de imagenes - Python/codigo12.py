from time import time
n = 955234435456443543645645665756734565456763445654757556546
tiempo_inicial = time()
valor = ''
while n != 0:
	r = n % 16
	if r < 10:
		valor = str(r) + valor
	else:
		valor = chr(r + 55) + valor

	n = n // 16
tiempo_final = time()
print('primera forma:', tiempo_final - tiempo_inicial)



#print(valor)

