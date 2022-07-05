from time import time
n = 955234435456443543645645665756734565456763445654757556546
tiempo_inicial = time()
valor = ''
while n != 0:
	r = n % 16
	if r < 10:
		valor = str(r) + valor
	if r == 10:
		valor = 'A' + valor
	elif r ==11:
		valor = 'B' + valor
	elif r ==12:
		valor = 'C' + valor
	elif r ==13:
		valor = 'D' + valor
	elif r ==14:
		valor = 'E' + valor
	else:
		valor = 'F' + valor

	n = n // 16
tiempo_final = time()
print('primera forma:', tiempo_final - tiempo_inicial)



#print(valor)

