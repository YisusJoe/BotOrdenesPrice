

def getSecciones(libro):
    secciones = []

    for seccion in libro:
        secciones.append(seccion[0][0:5])

    return list(set(secciones))

def getSeccionesCantidad(secciones,Libro_compra):

    precio = []
    cantidad = []
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
        puntos = precio + cantidad
        # print(f'puntos = {puntos}')
        listpuntos.append(puntos)
        puntos = []
        precio = []
        cantidad = []
        suma = 0
        
        # print(f'punto maximo {max(listpuntos)}')
    
    # print(f'listapuntos = {listpuntos}')
    return listpuntos

class MdlRangosEstrategia:

    def __init__(self,orderBook):

        # self.cantidadCompraA = 0.0
        # self.cantidadCompraB = 0.0
        # self.cantidadVentaA = 0.0
        # self.cantidadVentaB = 0.0
        # self.rangeMaxCompra = 0.0
        # self.rangeMinCompra = 0.0
        # self.rangeMaxVenta = 0.0
        # self.rangeMinVenta = 0.0
        self.libro = orderBook
        self.B_compra = ['0.62', '10000']
        self.A_compra = ['0.70', '1000']
        self.B_venta = []
        self.A_venta = []

    def getPuntosTotales(self):
        RangosCompra = {'A':self.A_compra,'B':self.B_compra}
        return RangosCompra

    def getACompra(self):
        Libro_compra = self.libro['bids']
        secciones = []

        secciones = sorted(getSecciones(Libro_compra))
        # print(secciones)

        seccionCantidad = getSeccionesCantidad(secciones,Libro_compra)
        print(seccionCantidad)

        
        # for a in Libro_compra:    
        #     print(a[1])


    def getRangosEstrategia(self, orderBook):

        self.rangoCompraA, self.cantidadCompraA = self.rangosAB(orderBook['bids'], self.rangeMinCompra, self.rangeMaxCompra, 0.001, 0)
        self.rangoCompraB, self.cantidadCompraB = self.rangosAB(orderBook['bids'], self.rangeMinCompra, self.rangeMaxCompra, 0.01, 0)
        self.rangoVentaA, self.cantidadVentaA = self.rangosAB(orderBook['asks'], self.rangeMinVenta, self.rangeMaxVenta, 0.001, 1)
        self.rangoVentaB, self.cantidadVentaB = self.rangosAB(orderBook['asks'], self.rangeMinVenta, self.rangeMaxVenta, 0.01, 1)

    def rangosAB(self, orderBook, range_min, range_max, gap, flag):

        price = []
        quantity = []
        while range_min <= range_max:

            allPrice = 0
            for ubook in orderBook:

                if(float(ubook[0]) > (range_min) and float(ubook[0]) <= (range_min+gap) and flag == 0):
                    allPrice += float(ubook[1])
                
                if(float(ubook[0]) > (range_min-gap) and float(ubook[0]) <= (range_min) and flag == 1):
                    allPrice += float(ubook[1])

            price.append(range_min)
            quantity.append(allPrice)
            range_min += gap

        max_quantity = max(quantity)
        index_price = quantity.index(max_quantity)

        return round(price[index_price],3),  max_quantity

    def rangeMaxMin(self,orderBook):

        compras = sorted(orderBook['bids'])
        ventas = orderBook['asks']

        self.rangeMaxCompra = float(max(compras)[0])
        self.rangeMinCompra = float(min(compras)[0])
        self.rangeMaxVenta = float(max(ventas)[0])
        self.rangeMinVenta = float(min(ventas)[0])
        # print(f'El rango max de compra es: {self.rangeMaxCompra}')
        # print(f'El rango min de compra es: {self.rangeMinCompra}')
        # down_book_sell = min(self.ordenesVenta)[0]
        # up_book_sell = max(self.ordenesVenta)[0]