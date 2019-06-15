import json
import math
import operator

#VARIABLES
redit = {}
txt = {}
puntuacion = {}
resultado = ""
x = 0
y = 0



#CONVERTIMOS EL JSON EN UN DICCIONARIO
with open('reddit.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
            texto = datos.get('selftext', " ")
            texto = texto.replace('\n','')
            texto = texto.replace('.','')
            texto = texto.replace('','')
            texto = texto.replace('-','')
            texto = texto.replace(',','')
            texto = texto.replace('(','')
            texto = texto.replace(')','')
            texto = texto.replace('?','')
            texto = texto.replace('!','')
            redit[texto] = 0             



#CONVERTIMOS EL TXT EN UN DICCIONARIO
archivo = open('100Muestras.txt')
datos = archivo.readlines()
archivo.close()   

for elemento in datos:
    resultado = resultado + elemento + " "
resultado = resultado.replace('\n','')    

cadena = resultado.split()

for i in range(0,len(cadena)-1):
    
    if i % 2 != 0:
        continue
    else:
        txt[cadena[i]] = int(cadena[i+1])



#CALCULOS DE PUNTOS POR TEXTO
for selfText in redit:
    for palabra in txt:
        if palabra in selfText:
            redit[selfText] += txt[palabra]
        else:
            continue


# ORDEMANOS EL DICCIONARIO DE MAYOR A MENOR
redit = sorted(redit.items(), key=operator.itemgetter(1))
redit.reverse()


#LISTA 100 PRIMEROS
for selfText in redit:
    if x < 100:
        print("100 Primeros")
        print(selfText)
        print(" ")

        x += 1
  
    else:
        break



#LISTA 100 ULTIMOS
redit.reverse()
for selfText in redit:
    if y < 100:
        print("100 Ultimos")
        print(selfText)
        print(" ")
        y += 1
       
    else:
        redit.reverse()
        break

