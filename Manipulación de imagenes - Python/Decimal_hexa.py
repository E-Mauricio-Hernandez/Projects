###Juan Esteban Velez hernandez - 161003641 #####
num = abs(int(input("Ingrese un numero decimal: ")));  
vector = "" 

for i in range (40):
  if((num%16)<10):
    n = str(num%16)
    vector = n + vector;

  if((num%16)==10):
    vector = 'A' + vector;

  if((num%16)==11):
    vector = 'B' + vector;

  if((num%16)==12):
    vector = 'C' + vector;

  if((num%16)==13):
    vector = 'D' + vector;

  if((num%16)==14):
    vector = 'E' + vector;

  if((num%16)==15):
    vector = 'F' + vector;
    
  if((num//16)==0):
    #vector = str(num) + vector;
    break
  num = num//16

print('Numero ingresado en hexadecimal: ',vector)
