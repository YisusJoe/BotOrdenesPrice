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

def getOrdebesVentas(symbol,depth,exchange):

    objOrderBook = orderBookModel.orderBook()
    objOrderBook.getTotalLibro(symbol,depth,exchange)
    objOrderBook.getOrdebesVentas()
    return objOrderBook.ordenesVenta

def bookPrice(range_min,range_max,book,gap,flag):

    price = []
    quantity = []
    while range_min <= range_max:

        allPrice = 0
        for ubook in book:

            if(float(ubook[0]) > (range_min) and float(ubook[0]) <= (range_min+gap) and flag == 0):

                allPrice += float(ubook[1])
            if(float(ubook[0]) > (range_min-gap) and float(ubook[0]) <= (range_min) and flag == 1):

                allPrice += float(ubook[1])

        price.append(range_min)
        quantity.append(allPrice)
        range_min += gap

    max_quantity = max(quantity)
    index_price = quantity.index(max_quantity)

    return round(price[index_price],3), max_quantity