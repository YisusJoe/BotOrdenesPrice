from Model.rangeBookModel import MdlRangosEstrategia

class RangosEstrategia:

    def __init__(self,orderBook):
        self.Rangos = MdlRangosEstrategia(orderBook)
        
    def getPuntosTotales(self):
        pass

    def getPuntosA(self):
        return self.Rangos.getACompra()

    def getPuntosB(self):
        pass

# def getRangoEstrastegia(orderBook):

#     # print('Retorno de puntos de clave estrategia')
#     objranges = rangeBookModel.rangosEstrategia()
#     objranges.rangeMaxMin(orderBook)
#     objranges.getRangosEstrategia(orderBook)
#     return objranges
#     # return objranges.rangoCompraA, objranges.cantidadCompraA, objranges.rangoCompraB, objranges.cantidadCompraB, objranges.rangoVentaA, objranges.cantidadVentaA, objranges.rangoVentaB, objranges. cantidadVentaB

# def getMaxOrderBook(orderBook):
    
#     return max(orderBook)

# def getMinOrderBook(orderBook):
    
#     return min(orderBook)