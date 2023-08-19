import time

import priceController
import Model.orderBookModel as orderBookModel
import Controller.orderBookController as orderBookController
import Model.rangeBookModel as rangeBookModel

symbol = 'MATICUSDT'
depth = 5000 # profundidad de 10 niveles
exchange = 'binance_futures' # intercambio de futuros de Binance
  
def main():

    # print(symbol)
    # Va,Vb = priceController.precioVenta(symbol,depth,exchange)
    # Ca,Cb = priceController.precioCompra(symbol,depth,exchange)

    # priceController.longShort(Ca,Cb,Va,Vb)

    # NEW CODE

    orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
    print(orderBook['bids'])
    objranges = rangeBookModel.rangosEstrategia()
    # ragesEstrategia = objranges.getRangosEstrategia(orderBook)

    # orderBookFull = orderBookController.getTotalLibro(symbol,depth,exchange)
    # print(orderBookFull)
    # orderBookCompra = orderBookController.getOrdenesCompra(symbol,depth,exchange)
    # print(orderBookCompra)

    # objOrderBook.getOrdenesCompra()
    # orderBookCompra = objOrderBook.ordenesCompra
    # # print(orderBookCompra)
    # objOrderBook.getOrdebesVentas()
    # OrderBookVenta = objOrderBook.ordenesVenta
    # print(OrderBookVenta)

    time.sleep(1)

    
if __name__ == "__main__":
    
    inicio = time.time()
    main()
    fin = time.time()

    print(f'El tiempo total del programa fue de: {fin - inicio}')