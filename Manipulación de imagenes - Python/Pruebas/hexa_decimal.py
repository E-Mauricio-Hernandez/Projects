###Juan Esteban Velez hernandez - 161003641 #####
num = abs(input("Ingrese un numero hexadecimal: "));
n = len(num)
lista = [0]*n
k = 0

for i in range (n):
    if(num[i]=='A' or num[i]=='a'):
        lista[i] = 10
    elif(num[i]=='B' or num[i]=='b'):
        lista[i] = 11
    elif(num[i]=='C' or num[i]=='c'):
        lista[i] = 12
    elif(num[i]=='D' or num[i]=='d'):
        lista[i] = 13
    elif(num[i]=='E' or num[i]=='e'):
        lista[i] = 14
    elif(num[i]=='F' or num[i]=='f'):
        lista[i] = 15
    else:
        lista[i] = int(num[i])
    k = lista[i]*16**(n-1-i) + k
print('numero ingresado',num)
print('Numero en decimal: ',k)