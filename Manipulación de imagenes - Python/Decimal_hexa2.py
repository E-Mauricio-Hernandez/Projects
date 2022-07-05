num = 6990
vector = "" 

for i in range (400):
  #if((num%16)<10):
    #n = str(num//16)
    #vector = n + vector;
  if((num%16)==10):
    print('A')
  if((num%16)==11):
    print('B')
  if((num%16)==12):
    print('C')
  if((num%16)==13):
    print('D')
  if((num%16)==14):
    print('E')
  if((num%16)==15):
    print('F')
  if((num//16)==0):
    print(num)
    break
  num = num//16

#print('hexa mia ',vector)
