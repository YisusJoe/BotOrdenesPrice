import Model.orderBookModel as orderBookModel

def getTotalLibro(symbol,depth,exchange):

    objOrderBook = orderBookModel.orderBook()
    objOrderBook.getTotalLibro(symbol,depth,exchange)
    return objOrderBook.ordenesTotales

def getOrdenesCompra(symbol,depth,exchange):

    objOrderBook = orderBookModel.orderBook()
    objOrderBook.getTotalLibro(symbol,depth,exchange)
    objOrderBook.getOrdenesCompra()
    return objOrderBook.ordenesCompra

def getOrdenesVentas(symbol,depth,exchange):

    objOrderBook = orderBookModel.orderBook()
    objOrderBook.getTotalLibro(symbol,depth,exchange)
    objOrderBook.getOrdebesVentas()
    return objOrderBook.ordenesVenta
