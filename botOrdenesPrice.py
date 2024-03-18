from binance.client import Client
import time
import datetime
import os

# import Controller.orderBookController as orderBookController
# import Controller.rangeBookController as rangeBookController

from Controller.rangeBookController import RangosEstrategia
from Controller.orderBookController import Libro

api_key = '2yvdFVl82TZLEATfeefdhA6XmIVBkBH9m3IHudN6PFS2S3akSlqMs4SLKshe5KR5'
api_secret = 'JfWuNLrtLaysmQxrPw6PULQyDzElRYclK8I7Hbrp6G8uSQaNRfl9YpVFIpV0CDRN'
client = Client(api_key,api_secret)

symbol = 'XRPUSDT'
depth = 10 # profundidad de 10 niveles
limit = 100
exchange = 'binance_futures' # intercambio de futuros de Binance
  

# TENGO PENSADO EN METER ESTE FRAGMENTO DE CODIGO EN LA POSICION ABIERTA
def longShort(dolar_buy_a,dolar_buy_b,dolar_sell_a,dolar_sell_b):

    if(abs((dolar_buy_a - dolar_buy_b)) < abs((dolar_sell_b - dolar_sell_a))):

        print("El precio de compra es más viable")
        return 'long'

    if(abs((dolar_sell_b - dolar_sell_a)) < abs((dolar_buy_a - dolar_buy_b))):

        print("El precio de venta es mas viable")
        return 'short'

def obtenerPrecioRT():

    ticker = client.get_symbol_ticker(symbol=symbol)
    precio = float(ticker['price'])
    # print(precio)

def main():

    ticker = client.get_symbol_ticker(symbol=symbol)
    # print(ticker)
    precio = float(ticker['price'])
    # print(f'El precio del activo es: {precio}')

    Obj_libro = Libro(symbol=symbol,limit=limit)
    Libro_total = Obj_libro.getlibroTotal()
    Libro_ventas = Obj_libro.getVentas()
    Libro_compras = Obj_libro.getCompras()

    # print(Libro_total)
    # print(Libro_ventas)
    # print(Libro_compras)

    Obj_estrategia = RangosEstrategia(Libro_total)
    Puntos_estrategia = Obj_estrategia.getPuntosTotales()
    Puntos_A = Obj_estrategia.getPuntosA()
    Puntos_B = Obj_estrategia.getPuntosB()

    print(Puntos_A)

    # orderBook = orderBookController.getTotalLibro(symbol,limit)
    # rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)

    # rangeVenta_A = rangeBookController.getMaxOrderBook(orderBook['asks'])
    
    # print(rangeVenta_A)

    # print('=====================================')

    # #Con esto reviso que trae el libro y si la cantidad de limit es correcta
    # i = 0
    # for a in orderBook['asks']:
    #     i += 1
    #     print(a)

    # print(i)

    # print(f"El precio maximo de venta es: {max(orderBook['asks'])}")
    # print(f"El precio minimo de venta es: {min(orderBook['asks'])}")

    # print('=====================================')

    # #Con esto reviso que trae el libro y si la cantidad de limit es correcta
    # i = 0
    # for a in orderBook['bids']:
    #     i += 1
    #     print(a)

    # print(i)

    # print(f"El precio maximo de compra es: {max(orderBook['bids'])}")
    # print(f"El precio minimo de compra es: {min(orderBook['bids'])}")

    # print('=====================================')

    # print('-------------------------------')
    # print(f'Precio venta B: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
    # print(f'Precio venta A: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
    # print(f'Precio compra A: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
    # print(f'Precio compra B: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
    
    # longShort(rangesEstategia.rangoCompraA,rangesEstategia.rangoCompraB,rangesEstategia.rangoVentaA,rangesEstategia.rangoVentaB)

    # while(1):
        
    #     ticker = client.get_symbol_ticker(symbol=symbol)
    #     precio = float(ticker['price'])

    #     fecha_actual = datetime.datetime.now()
    #     nombre_archivo = fecha_actual.strftime("%Y-%m-%d.txt")
    #     ruta = "./Entradas/" + nombre_archivo

    #     if os.path.exists(ruta):

    #         archivo = open(ruta, 'a')

    #     else:

    #         archivo = open(ruta, 'w')
        
    #     if(precio == rangesEstategia.rangoCompraA):
            
    #         print(f'Abri una entrada en long en el precio {rangesEstategia.rangoCompraA}, con un SL en {rangesEstategia.rangoCompraB} y TP en {rangesEstategia.rangoVentaA}')
            
    #         tp = rangesEstategia.rangoVentaA
    #         sl = rangesEstategia.rangoCompraB

    #         while(1): 

    #             ticker = client.get_symbol_ticker(symbol=symbol)
    #             precio = float(ticker['price'])
    #             print(f'precioActual = {precio}, SL = {sl}, TP = {tp}')
                
    #             if(precio == tp):

    #                 print('Entrada ganada')
    #                 archivo.write(f'Ganada, Entrada {rangesEstategia.rangoCompraA}, SL {rangesEstategia.rangoCompraB}, TP {rangesEstategia.rangoVentaA}\n')
    #                 orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
    #                 # print(orderBook)
    #                 rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
    #                 print('-------------------------------')
    #                 print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
    #                 print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
    #                 break
    #             if(precio == sl):

    #                 print('Entrada perdida')
    #                 archivo.write(f'Perdida, Entrada {rangesEstategia.rangoCompraA}, SL {rangesEstategia.rangoCompraB}, TP {rangesEstategia.rangoVentaA}\n')
    #                 orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
    #                 # print(orderBook)
    #                 rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
    #                 print('-------------------------------')
    #                 print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
    #                 print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
    #                 break
                
    #             time.sleep(1)

    # # if(tipoDeEntrada == 'short'):

    #     # ticker = client.get_symbol_ticker(symbol=symbol)
    #     # precio = float(ticker['price'])

    #     if(precio == rangesEstategia.rangoVentaA):
        
    #         print(f'Abri una entrada en short en el precio {rangesEstategia.rangoVentaA}, con un SL en {rangesEstategia.rangoVentaB} y TP en {rangesEstategia.rangoCompraA}')

    #         tp = rangesEstategia.rangoCompraA
    #         sl = rangesEstategia.rangoVentaB
            
    #         while(1):

    #             ticker = client.get_symbol_ticker(symbol=symbol)
    #             precio = float(ticker['price'])
    #             print(f'precioActual = {precio}, SL = {sl}, TP = {tp}')

    #             if(precio == tp):

    #                 print('Entrada ganada')
    #                 archivo.write(f'Ganada, Entrada {rangesEstategia.rangoVentaA}, SL {rangesEstategia.rangoVentaB}, TP {rangesEstategia.rangoCompraA}\n')
    #                 orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
    #     # print(orderBook)
    #                 rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
    #                 print('-------------------------------')
    #                 print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
    #                 print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
    #                 break
    #             if(precio == sl):

    #                 print('Entrada perdida')
    #                 archivo.write(f'Perdida, Entrada {rangesEstategia.rangoVentaA}, SL {rangesEstategia.rangoVentaB}, TP {rangesEstategia.rangoCompraA}\n')
    #                 orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
    #                 # print(orderBook)
    #                 rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
    #                 print('-------------------------------')
    #                 print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
    #                 print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
    #                 print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
    #                 break
                
    #             time.sleep(1)

    time.sleep(1)

if __name__ == "__main__":
    
    inicio = time.time()
    main()
    fin = time.time()

    print(f'El tiempo total del programa fue de: {fin - inicio}')