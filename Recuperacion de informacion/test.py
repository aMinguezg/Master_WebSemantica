txt={}
resultado = ""
archivo = open('ejemplotxt.txt')
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

print(txt)