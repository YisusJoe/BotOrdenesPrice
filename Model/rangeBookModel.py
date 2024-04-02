

def getSecciones_001(libro):
    secciones = []

    for seccion in libro:
        secciones.append(seccion[0][0:5])

    return sorted(list(set(secciones)))

def getSecciones_01(libro):
    secciones = []

    for seccion in libro:
        secciones.append(seccion[0][0:4])

    return sorted(list(set(secciones)))

def getBloqueCompra(secciones,Libro_compra):
    precio = []
    cantidad = []
    retCantidad = []
    suma = 0
    puntos =  []
    listpuntos = []

    for seccion in secciones:
        # print(f'seccion = {seccion}')
        precio.append(seccion)

        for Lc in Libro_compra:

            if(Lc[0].startswith(seccion)):
                # print(f'precio = {Lc[0]}, cantidad = {Lc[1]}')
                suma += float(Lc[1])

        # print(round(suma,2))
        cantidad.append(round(suma,2))
        retCantidad.append(round(suma,2))
        puntos = precio + cantidad
        # print(f'puntos = {puntos}')
        listpuntos.append(puntos)
        puntos = []
        precio = []
        cantidad = []
        suma = 0

    posicion = retCantidad.index(max(retCantidad))
    bloqueMax = listpuntos[posicion]

    # print(bloqueMax)
    return bloqueMax

def getBloqueVenta(secciones,Libro_venta):
    retPrecio = []
    precio = []
    cantidad = []
    retCantidad = []
    suma = 0
    longPrecio =  0
    listpuntos = []
    i = 0
    j = 0

    for v in Libro_venta:
        # print(v[0])     #DESCOMENTAR PARA REVISAR EL LIBRO DE ORDENES
        precio.append(v[0])
        cantidad.append(v[1])

    for v in Libro_venta:
        pass
        # print(v[1])     #DESCOMENTAR PARA REVISAR EL LIBRO DE ORDENES
    # print(Libro_venta)

    longPrecio = len(precio[0])
    # print(longPrecio)
    # toy haciendo la logica de la venta

    # print(len(secciones))
    while(i <= len(secciones)-1):

        suma = 0
        # print(i)
        if(i != len(secciones)-1):
            # print(f'Entre a poner la primera seccion {secciones[i]}')
            # print(f'seccion {secciones[i+1]}')
            s = secciones[i].ljust(longPrecio,'0')
            s2 = secciones[i+1].ljust(longPrecio,'0') 
            # print(f'seccion s: {s}')
            # print(f'seccion s: {s2}')
            suma += float(cantidad[precio.index(s)])
            suma = round(suma,2)

            for j in Libro_venta:

                # print(j)
                if(j[0].startswith(secciones[i+1])):
                    # print(f'precio = {Lc[0]}, cantidad = {Lc[1]}')
                    # print(suma)
                    if(j[0] == s2):
                        pass
                        # print(f'es igual {j[0]} y {s2}')

                    else:
                        suma += float(j[1])
                        suma = round(suma,2)    
                    
            
            listpuntos.append([secciones[i], suma])
            

        if(i == len(secciones)-1):
            pass
            # print(len(secciones)-1)
            # print(i)
            # print(secciones[i])
            # # s = secciones[i].ljust(6,'0')
            # print(f'Ultimo : {secciones[i]}')
            # # listpuntos.append([secciones[i], cantidad[Lv.index(s)]])
            # suma += float(cantidad[Lv.index(s)])
            # suma = round(suma,2)
            # listpuntos.append([secciones[i], suma])

        # if(i != len(secciones)-1):
        #     print(f'{i} {secciones[i]} {secciones[i+1]}')

        # print(i)
        i+=1

    # print(f'Lista puntos {listpuntos}')
 
    for p in listpuntos:
        retPrecio.append(p[0])
        retCantidad.append(p[1])

    # print(f'precios : {retPrecio}')
    # print(f'cantidades : {retCantidad} \n')     

    posicion = retCantidad.index(max(retCantidad))
    bloqueMax = listpuntos[posicion]

    # print(bloqueMax)
    return bloqueMax

class MdlRangosEstrategia:

    def __init__(self,orderBook):

        self.libro = orderBook

    def getPuntosTotales(self):
        RangosCompra = {'A':self.A_compra,'B':self.B_compra}
        return RangosCompra

    def getABloque(self,cv):
        Libro = self.libro[cv]
        secciones = []

        if(cv == 'bids'):
            secciones = sorted(getSecciones_001(Libro))
            bloque = getBloqueCompra(secciones,Libro)
        if(cv=='asks'):
            secciones = sorted(getSecciones_001(Libro))
            # print(sorted(secciones, reverse=True))      #COMENTAR PARA EJECUTAR
            secciones = sorted(secciones, reverse=True)
            bloque = getBloqueVenta(secciones,Libro)

        return bloque

    def getBBloque(self,cv):
        Libro = self.libro[cv]
        secciones = []

        if(cv == 'bids'):
            secciones = sorted(getSecciones_01(Libro))
            bloque = getBloqueCompra(secciones,Libro)
        if(cv=='asks'):
            secciones = sorted(getSecciones_01(Libro))
            # print(sorted(secciones, reverse=True))      #COMENTAR PARA EJECUTAR
            secciones = sorted(secciones, reverse=True)
            bloque = getBloqueVenta(secciones,Libro)

        return bloque