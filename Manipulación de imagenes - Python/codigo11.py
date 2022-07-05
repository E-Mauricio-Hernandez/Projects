import numpy as np 

t = int(input('Tamaño del kernel: '))
k = np.zeros((t, t))
print(k)

for f in range (0, t):
	for c in range (0, t):
		k[f, c] = int(input('valor: '))

print(k)