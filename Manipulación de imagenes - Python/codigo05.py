from time import time

valor = input ('valor:')
palindromo = 'Es palindromo'

tiempo_inicial = time()

for pos in range(0, len(valor)//2):
	if valor[pos] != valor[-(pos + 1)]:
		palindromo = 'No es palindromo'
		break

tiempo_final = time()
print(palindromo)
print('tiempo:', tiempo_final - tiempo_inicial)