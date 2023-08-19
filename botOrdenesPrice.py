import time

import Model.orderBookModel as orderBookModel
import Controller.orderBookController as orderBookController
import Controller.rangeBookController as rangeBookController

symbol = 'MATICUSDT'
depth = 5000 # profundidad de 10 niveles
exchange = 'binance_futures' # intercambio de futuros de Binance
  
def main():

    orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
    # print(orderBook)
    rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
    
    print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
    print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
    print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
    print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
   
    def longShort(dolar_buy_a,dolar_buy_b,dolar_sell_a,dolar_sell_b):

        if(abs((dolar_buy_a - dolar_buy_b)) < abs((dolar_sell_b - dolar_sell_a))):

            print("El precio de compra es más viable")

        if(abs((dolar_sell_b - dolar_sell_a)) < abs((dolar_buy_a - dolar_buy_b))):

            print("El precio de venta es mas viable")

    longShort(rangesEstategia.rangoCompraA,rangesEstategia.rangoCompraB,rangesEstategia.rangoVentaA,rangesEstategia.rangoVentaB)        
    
    time.sleep(1)

    
if __name__ == "__main__":
    
    inicio = time.time()
    main()
    fin = time.time()

    print(f'El tiempo total del programa fue de: {fin - inicio}')