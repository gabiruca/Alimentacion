from alimentacion import *
def obtenerRecetas():
    archivo=open("recetas.txt",encoding="utf-8")
    dicRec=dict()
    for line in archivo:
        cleanLine=line.strip().split(",")
        tupla=dicRec.get(cleanLine[0],set())
        tupla=(cleanLine[1],cleanLine[2])
        dicRec[cleanLine[0]]=tupla
    archivo.close()
    return dicRec

def detallesReceta(nombreReceta,diccionarioRecetas):
    for receta in diccionarioRecetas.keys():
        if receta == nombreReceta:
