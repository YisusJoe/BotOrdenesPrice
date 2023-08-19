import Model.rangeBookModel as rangeBookModel

def getRangoEstrategia(orderBook):

    print('Retorno de puntos de clave estrategia')
    objranges = rangeBookModel.rangosEstrategia()
    objranges.rangeMaxMin(orderBook)
    objranges.getRangosEstrategia(orderBook)
    return objranges
    # return objranges.rangoCompraA, objranges.cantidadCompraA, objranges.rangoCompraB, objranges.cantidadCompraB, objranges.rangoVentaA, objranges.cantidadVentaA, objranges.rangoVentaB, objranges. cantidadVentaB