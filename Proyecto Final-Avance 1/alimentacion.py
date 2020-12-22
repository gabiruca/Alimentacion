import numpy as np

def leerProductos():
	return np.array([linea.strip() for linea in open("productos.txt","r") ])

def leerInformacionNutricional():
    np.set_printoptions(suppress=True)
    iArchivo = open("informacion_nutricional.txt","r")
    lineas = []
    for linea in iArchivo:
        lineas.append([float(elemento) for elemento in linea.strip().split(",")])
    iArchivo.close()

    matriz = np.array(lineas)
    return matriz


def leerCaracteristicas():
    return np.array(['%Aprovechamiento', 'Energía Kcal', 'Proteinas', 'H. de Carbono', 'Fibra', 'Lípidos', 'Ac. Grasos Saturados', 'Ac. Grasos Poliinsaturados', 'Colesterol', 'Sodio Na', 'Potasio K', 'Calcio Ca', 'Fosforo P', 'Magnesio Mg', 'Hierro Fe', 'Zinc Zn', 'Fluor F', 'Vit.B1 Tiamina', 'Vit.B2 Riboflavina', 'Vit.B3 Niacina', 'Vit.B6 Piridoxina', 'Vit. B12 *', 'Vit.C Acido Ascorbico*', 'Vit. A  *', 'Vit. D *', 'Vit. E'])

def caracteristicasProducto(producto):
    i=0
    lCaract=[]
    lDatos=[]
    condicion= producto.upper()==leerProductos()
    infoN=leerInformacionNutricional()[condicion]
    for dato in infoN[0]:
        if dato <0:
            dato=0
        lCaract.append(leerCaracteristicas()[i])
        lDatos.append(dato)
        i+=1
    return np.array(lCaract),np.array(lDatos)

def compararProductos(producto1,producto2,caracteristica):
    condicion= caracteristica.capitalize()==leerCaracteristicas()
    nCaract1,datos1=caracteristicasProducto(producto1.upper())
    nCaract2,datos2=caracteristicasProducto(producto2.upper())
    datoAComp1=datos1[condicion][0]
    datoAComp2=datos2[condicion][0]
    if datoAComp1>datoAComp2:
        print("El producto", producto1, "aporta mas",caracteristica, "que el producto",producto2)
    elif datoAComp2>datoAComp1:
        print("El producto", producto2, "aporta mas", caracteristica, "que el producto", producto1)
    else:
        print("Ambos aportan con la misma cantidad de", caracteristica)

def cantidadEnergia(listaProd):
    energia=0
    for elemento in listaProd:
        lCar,lDat=caracteristicasProducto(elemento)
        lDat1=lDat.tolist()
        energia=energia+lDat1[1]
    return energia

def caractdifpeso(producto):
    lCar,lDatos=caracteristicasProducto(producto)
    lDatos1=lDatos.tolist()
    lCar1=lCar.tolist()
    peso=0
    v=0
    for i in range(len(lDatos1)):
        if i >=2 and i <=9:
            peso=peso+lDatos1[i]
        elif i>=10 and i<=20:
            transf1=lDatos1[i]/1000
            peso=peso+transf1
        elif i==21:
            transf2=lDatos1[i]/1000000
            peso=peso+transf2
        elif i==22:
            transf3 = lDatos1[i] / 1000
            peso=peso+transf3
        elif i>=23 and i<=25:
            transf4= lDatos1[i]/1000000
            peso=peso+transf4
    if peso != 100:
        for dato in lDatos1:
            print(lCar1[v], dato)
            v += 1

def analisis(lista):
    energia=[]
    proteina=[]
    cho=[]
    fiber=[]
    for e in lista:
        caracter, camb = caracteristicasProducto(e)
        camb1=camb.tolist()
        if camb1[1] not in energia:
            energia.append(camb1[1])
        if camb1[2] not in proteina:
            proteina.append(camb1[2])
        if camb1[3] not in cho:
            cho.append(camb1[3])
        if camb1[4] not in fiber:
            fiber.append(camb1[4])
    max1=np.array(energia).max()
    ind1=lista[np.array(energia).argmax()]
    max2=np.array(proteina).max()
    ind2 = lista[np.array(proteina).argmax()]
    max3=np.array(cho).max()
    ind3 = lista[np.array(cho).argmax()]
    max4=np.array(fiber).max()
    ind4 = lista[np.array(fiber).argmax()]
    maxis=[(ind1,max1),(ind2,max2),(ind3,max3),(ind4,max4)]
    return maxis
