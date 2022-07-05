#############################CODIGO COMPLETO DE MEJORAMIENTO DE IMAGEN A GRISES SON FORMULA SK########################
import cv2
import numpy as np

a = 0
m = 0
p = 0
r = 0
ko = 0
hu = 0
imagen_BGR = cv2.imread ('lena_RGB.png')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)


cv2.imshow('imagen_BGR' , imagen_BGR)
cv2.imshow('imagen_GRIS' , imagen_GRIS)

#print(imagen_GRIS.shape)
#print(imagen_GRIS.size)
x = imagen_GRIS.shape[0]
y = imagen_GRIS.shape[1]
#print(x)
#print(y)

#ma = np.zeros((256))
mas = np.zeros((256))
sk = np.zeros((256))
r = np.zeros((256))
histogramagraf = np.zeros((x, 256, 1),np.uint8)##GRAFICA_HISTOGRAMA##
histogramagra2 = np.zeros((x, 256, 1),np.uint8)##GRAFICA_HISTOGRAMA##

imagen_negra= np.zeros((512, 512, 1),np.uint8)
#print(ma)
#print('tamaño vector',ma.size)

#print(imagen_GRIS.dtype)
#print(imagen_GRIS)
#######GNERAR HISTOGRAMA MI FORMA########
#for pos in range(0, x):
	#for pos1 in range(0, y):
		#m = imagen_GRIS[pos][pos1]
		#ma[m] +=1
########GENERAR HISTOGRAMA########
ma = cv2.calcHist([imagen_GRIS], [0], None, [256], [0, 256])##generar histograma


#print(ma) 
#print(ma.size)
#for pos in range(0, 255):
	#a = ma[pos]+a

#print('tamaño vector histograma',a)
#print('tamaño imagen grises',imagen_GRIS.size)



################formula AJUSTE del histograma########################
L = 256
M = imagen_GRIS.shape[0]
N = imagen_GRIS.shape[1]
K = (L-1)/(M*N)
##nj recorrer el histograma
for pos3 in range(0, (L)):
	p = K*ma[pos3]
	sk[pos3] = sk[pos3-1] + p
	r[pos3] = round(sk[pos3])
# redondeo	
#for pos4 in range(0, (L-1)):
	#r[pos4] = round(sk[pos4])
#r[255] = 255
print('SK',r)
#print
#cv2.imshow('imagen negra',imagen_negra)
#imagen_GRIS2 = imagen_GRIS.copy()

for pos8 in range(0, M):
	for pos9 in range(0, N):
		ko= imagen_GRIS[pos8][pos9]
		#hu = r[ko]
		imagen_negra[pos8][pos9] = r[ko]
		#imagen_GRIS2[pos][pos1] = r[ko]
		##imagen_negra = imagen_GRIS[pos][pos1]
		##
#######n PARA IMAGEN ORIGINAL##############
maxs = max(ma)
n = maxs/x	
#############NORMALIZAR IMAGEN ORIGINAL###############
for pos in range(0, 255):
	 ma[pos]= ma[pos]/n
#print('vector histograma normalizado',ma) 

#####GRAFICA HISTOGRAMA IMAGEN ORIGINAL############
for pos in range(0, x):
	for pos1 in range(0, 255):
		#hc = ma[pos1]
		if pos <= ma[pos1]:
			histogramagraf[-pos][pos1] = 255

###########histograma imagen sk #################
mas = cv2.calcHist([imagen_negra], [0], None, [256], [0, 256])##generar histograma

#######n PARA IMAGEN filtro##############
maxs = max(mas)
n = maxs/x	
#############NORMALIZAR IMAGEN filtro###############
for pos in range(0, 255):
	 mas[pos]= mas[pos]/n
#print('vector histograma normalizado',ma) 

#####GRAFICA HISTOGRAMA IMAGEN filtro############
for pos in range(0, x):
	for pos1 in range(0, 255):
		#hc = ma[pos1]
		if pos <= mas[pos1]:
			histogramagra2[-pos][pos1] = 255
#for pos in range(0, x):
	#for pos1 in range(0, y):
		#m = imagen_negra[pos][pos1]
		#mas[m] +=1
############NORMALIZAR#############		
#for pos in range(0, 255):
#	 mas[pos]= mas[pos]/16
#####GRAFICA HISTOGRAMA############
#for pos in range(0, 512):
	#for pos1 in range(0, 255):
		#hc = mas[pos1]
		#if pos < hc:
		#	histogramagraf[-pos][pos1] = 255

#cv2.imshow('histograma de formula',histogramagraf)		
cv2.imshow('imagen de formula',imagen_negra)
cv2.imshow('Histograma1',histogramagraf)		
cv2.imshow('Histograma2',histogramagra2)				
cv2.waitKey()
cv2.destroyAllWindows()

#histograma3 = [0] * 256 vector de 256 posiciones


##########################################################