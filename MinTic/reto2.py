texla = input("ingrese cadena tex" " ")
volksbaguen = input("ingrese cadena volks" " ")
priorizacion = input("cadena facebook" " ")
v1_tex = 0
v2_volk = 0
letra = ""
for x in priorizacion:
  if x in texla:
    v1_tex +=1
  if x in volksbaguen:
    v2_volk +=1
  if v1_tex == v2_volk:
    letra += "_"
  if v1_tex > v2_volk:
    letra += "Q"
  if v2_volk > v1_tex:
    letra +="F"
print(letra)