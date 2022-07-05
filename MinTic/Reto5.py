# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 12:18:45 2021

@author: brayan
"""
def categorias():
    entrada=['Electrónica', 'Ropa', 'Video Juegos Retro', 'Alimentos', 'Software' ,'Hardware', 'Alimentos' ,'Herramientas' ,'Ropa', 'Hardware', 'Hardware', 'Hardware', 'Alimentos']
    final=[]
    for x in range (0,len(entrada)):
        if entrada[x] in final:
            pass
        else:

            final.append(entrada[x])
    print(final)
    return final

def notengocategoria():
    entrada=([1,3,6,8], ['Ropa','Electrónica','Alimento', 'Alimento', 'Alimento', 'Ropa', 'Electrónica', 'Alimento', 'Alimento', 'Alimento'],     'Alimento')
    final=[]
    for x in range (0, len(entrada[0])):
        if entrada[1][entrada[0][x]]==entrada[2]:
            final.append(entrada[0][x])
    print(final)
    return final
def notengo():
    entrada=([3,5,7,10,15,16],[4,10,5,8])
    final=[]
    for x in range (0, len(entrada[0])):
        if entrada[0][x] in entrada[1]:
            pass
        else:
            final.append(entrada[0][x])
    print(final)
    return final
def puedocambiar():
    entrada=([3,5,7,10,15,16],[4,10,5,8])
    final=[]
    for x in range (0, len(entrada[0])):
        if entrada[0][x] in entrada[1]:
            final.append(entrada[0][x])
    print(len(final))
    return len(final)

while True:
    print("1. categorias")
    print("2. notengocategoria")
    print("3. notengo")
    print("4. puedocambiar")
    opc=input("Ingrese la funcion a realizar: ")
    if opc=="1":
        categorias()
    elif opc=="2":
        notengocategoria()
    elif opc=="3":
        notengo()
    elif opc=="4":
        puedocambiar()
    else:
        print("Entrada no valida")