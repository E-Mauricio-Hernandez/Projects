from numpy import *
import time

def NRZ() :
	flag = 0
	for i in range(0,len(ins)):
		if ins[i] == '1':
			vpos()
			vpos()
		else:
			vneg()
			vneg()
def NRZM():
	flag = -1
	for i in range(0,len(ins)):
		if ins[i] == '1' and flag == -1:
			flag = 1
			vpos()
			vpos()
		elif ins[i]== '1' and flag == 1:
			flag = -1
			vneg()
			vneg()
		else:
			if flag == 1:
				vpos()
				vpos()
			else:
				vneg()
				vneg()

def NRZS():
	flag = -1
	for i in range(0,len(ins)):
		if (ins[i]== '0' and flag == -1):
			flag = 1
			vpos()
			vpos()
		elif ins[i]== '0' and flag == 1:
			flag = -1
			vneg()
			vneg()
		else:
			if flag == 1:
				vpos()
				vpos()
			else:
				vneg()
				vneg()

def unipolarRZ():  #1 dura la mitad
	for i in range(0,len(ins)):
		if ins[i]== '1':
			vpos()
			vcero()
		else:
			vcero()
			vcero()
			
def RZAMI():   #1 dura 3 parte
	flag = 0
	for i in range(0,len(ins)):
		if (ins[i]== '1' and flag == 0):
			flag=1
			time.sleep(0.1)
			vpos()
			time.sleep(0.1)
		elif ins[i]== '1' and flag == 1:
			flag=0
			time.sleep(0.1)
			vneg()
			time.sleep(0.1)
		else:
			vcero()
			vcero()
def dicodeNRZ():
	flag = 0
	for i in range(0,len(ins)):
		if (i > 0):
			if(ins[i] != ins[i-1]):
				flag = 0
			else:
				flag = 1

		if (ins[i]== '1' and flag == 0):
			vneg()
			vneg()
		elif(ins[i]== '0' and flag == 0):
			vpos()
			vpos()
		else:
			vcero()
			vcero()
  
def bios():
	flag = 0
	flag2 = 1
	limite = len(ins)
	limite = limite*2
	cont = 0
	sal = zeros(limite)
	for i in range(0,limite,2):
		if(ins[cont]== '0' and flag == 0):
			sal[i] = 0
			sal[i+1] = 1
			fsu()
		elif(ins[cont]== '0' and flag == 1):
			sal[i] = 1
			sal[i+1] = 0
			fba()
		elif(ins[cont] == '1' and sal[i-1] == 0 and flag2 !=1):
			sal[i] = 1
			sal[i+1] = 1
			flag = 0
			vpos()
			vpos()
		else:
			sal[i] = 0
			sal[i+1] = 0
			flag = 1
			vcero()
			vcero()
		cont = cont + 1
		flag2 = 0

def biom():
	flag = 0
	limite = len(ins)
	limite = limite*2
	cont = 0
	sal = zeros(limite)
	for i in range(0,limite,2):
		if (ins[cont]== '1' and flag == 0):
			sal[i] = 0
			sal[i+1] = 1
			fsu()
		elif(ins[cont]== '1'and flag == 1):
			sal[i] = 1
			sal[i+1] = 0
			fba()
		elif(ins[cont] == '0' and sal[i-1] == 0):
			sal[i] = 1
			sal[i+1] = 1
			flag = 0
			vpos()
			vpos()
		else:
			sal[i] = 0
			sal[i+1] = 0
			flag =1
			vcero()
			vcero()
		cont = cont + 1

def Bipolar_RZ():
	for x in range (0,len(ins)):
		if ins[x] == "1":
			fba()
		elif ins[x] == "0":
			fsuneg()
def Bifase_L():
	for x in range (0,len(ins)):
		if ins[x] == "1":
			cfpn()
		elif ins[x] == "0":
			cfnp()
def Dicode_RZ():
	if ins[0] == 1:
		aux = 0
	else:
		aux = 1
	for x in range(0,len(ins)):
		if ins[x] == "1":
			if aux == 0:
				fsuneg()
				aux = 1
			elif aux >= 1:
				vcero()
				vcero()
		elif ins[x] == "0":
			if aux >= 1:
				fba()
				aux = 0
			elif aux == 0:
				vcero()
				vcero()
def DelayModulation():
	if ins[0] == 1:
		aux = 0
	else:
		aux = 1
	for x in range(0,len(ins)):
		if ins[x] == "1":
			if  aux == 1:
				cfnp()
				aux = 0   
			elif aux == 0:
				cfpn()
				aux = 0
		elif ins[x] == "0":
			if aux == 0:
				vneg()
				vneg()
				aux = 1
			elif aux == 1:
				vpos()
				vpos()  
				aux = 0
def vpos():
	print("+v")
	time.sleep(0.2)
def vneg():
	print("-v")
	time.sleep(0.2)
def vcero():
	print("0")
	time.sleep(0.2)
def fba():
	print("+v")	
	time.sleep(0.2)
	print("0")
	time.sleep(0.2)
def fsu():
	print("0")
	time.sleep(0.2)
	print("+v")
	time.sleep(0.2)
def cfpn():
	print("+v")
	time.sleep(0.2)
	print("-v")
	time.sleep(0.2)
def cfnp():
	print("-v")
	time.sleep(0.2)
	print("+v")
	time.sleep(0.2)
def fsuneg():
	print("-v")
	time.sleep(0.2)
	print("0")
	time.sleep(0.2)
while True:
	data=open("datos.txt","r")
	c=data.read()
	prueba=c.split(",")
	ins=prueba[1]
	if (prueba[0]=="1"):
		NRZ()
	elif (prueba[0]=="2"):
		NRZM()
	elif (prueba[0]=="3"):
		NRZS()
	elif (prueba[0]=="4"):
		unipolarRZ()
	elif (prueba[0]=="5"):
		Bipolar_RZ()
	elif (prueba[0]=="6"):
		RZAMI()
	elif (prueba[0]=="7"):
		Bifase_L()
	elif (prueba[0]=="8"):
		biom()
	elif (prueba[0]=="9"):
		bios()
	elif (prueba[0]=="10"):
		DelayModulation()
	elif (prueba[0]=="11"):
		dicodeNRZ()
	elif (prueba[0]=="12"):
		Dicode_RZ()
	print("----------")

