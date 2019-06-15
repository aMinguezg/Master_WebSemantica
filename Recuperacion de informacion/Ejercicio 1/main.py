import json
import math
import operator

# VARIABLES
redit = {}
txt = {}
resultado = ""
cadena = []
totalR = 0
totalT = 0
resultadoFinal = {}

# CONVERTIMOS EL JSON EN UN DICCIONARIO
with open('reddit.json') as file:
    data = json.load(file)
    
    for datos in data['data']:
        texto = datos.get('selftext', " ")
        texto = texto.replace('\n','')
        texto = texto.replace('.','')
        texto = texto.replace(',','')
        texto = texto.replace('(','')
        texto = texto.replace(')','')
        texto = texto.replace('?','')
        texto = texto.replace('!','')
        listaTexto = texto.split(" ")
      
        for palabra in listaTexto:

                if palabra in redit:
                    redit[palabra] += 1
                else:
                    redit[palabra] = 1


#   CONVERTIMOS EL TXT EN UN DICCIONARIO
archivo = open('norvig.txt')
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



# ALGORITMO ROOTLOGLIKELIHOODRATIO
def rootLogLikelihoodRatio (a, b, c, d):
    E1=c*(a+b)/(c+d)
    E2=d*(a+b)/(c+d)
 # To avoid a division by 0 if a or b equal 0 they are replaced by 1
    if a==0 and b==0:
        result=2*(a*math.log(a/E1+1)+b*math.log(b/E2+1))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    elif a==0 and b!=0:
        result=2*(a*math.log(a/E1+1)+b*math.log(b/E2))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    elif a!=0 and b==0:
        result=2*(a*math.log(a/E1)+b*math.log(b/E2+1))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    else:
        result=2*(a*math.log(a/E1)+b*math.log(b/E2))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    
    return result


# RELLENAMOS UN DICCIONARIO CON LOS VALORES OBTENIDOS
for elementos in txt:
    totalT += txt[elementos]

for elementos in redit:
    totalR += redit[elementos]

for elementos in redit:
    if elementos in txt:
        resultadoFinal[elementos] = rootLogLikelihoodRatio(redit[elementos],txt[elementos],totalR,totalT)
    else:
        continue


# ORDEMANOS EL DICCIONARIO PARA VER LOS POSITIVOS
resultadoFinal = sorted(resultadoFinal.items(), key=operator.itemgetter(1))
resultadoFinal.reverse()
print(resultadoFinal)