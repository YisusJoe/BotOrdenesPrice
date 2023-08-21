from binance.client import Client
import time
import datetime
import os

import Controller.orderBookController as orderBookController
import Controller.rangeBookController as rangeBookController

api_key = '2yvdFVl82TZLEATfeefdhA6XmIVBkBH9m3IHudN6PFS2S3akSlqMs4SLKshe5KR5'
api_secret = 'JfWuNLrtLaysmQxrPw6PULQyDzElRYclK8I7Hbrp6G8uSQaNRfl9YpVFIpV0CDRN'
client = Client(api_key,api_secret)

symbol = 'MATICUSDT'
depth = 5000 # profundidad de 10 niveles
exchange = 'binance_futures' # intercambio de futuros de Binance
  
def main():

    ticker = client.get_symbol_ticker(symbol=symbol)
    precio = float(ticker['price'])
    # print(precio)

    # fecha_actual = datetime.datetime.now()
    # nombre_archivo = fecha_actual.strftime("%Y-%m-%d.txt")
    # archivo = open(nombre_archivo, 'w')

    orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
    # print(orderBook)
    rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
    
    print('-------------------------------')
    print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
    print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
    print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
    print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
    
    
    # tipoDeEntrada = longShort(rangesEstategia.rangoCompraA,rangesEstategia.rangoCompraB,rangesEstategia.rangoVentaA,rangesEstategia.rangoVentaB)        
    
    # if(tipoDeEntrada == 'long'):

    while(1):

        ticker = client.get_symbol_ticker(symbol=symbol)
        precio = float(ticker['price'])
        # print(precio)

        fecha_actual = datetime.datetime.now()
        nombre_archivo = fecha_actual.strftime("%Y-%m-%d.txt")
        
        if os.path.exists(nombre_archivo):

            archivo = open(nombre_archivo, 'a')

        else:

            archivo = open(nombre_archivo, 'w')

        # archivo.write(f'Ganada, Entrada {rangesEstategia.rangoCompraA}, SL {rangesEstategia.rangoCompraB}, TP {rangesEstategia.rangoVentaA}\n')
        
        if(precio == rangesEstategia.rangoCompraA):
            
            print(f'Abri una entrada en long en el precio {rangesEstategia.rangoCompraA}, con un SL en {rangesEstategia.rangoCompraB} y TP en {rangesEstategia.rangoVentaA}')
            
            tp = rangesEstategia.rangoVentaA
            sl = rangesEstategia.rangoCompraB

            while(1): 

                ticker = client.get_symbol_ticker(symbol=symbol)
                precio = float(ticker['price'])
                print(f'precioActual = {precio}, SL = {sl}, TP = {tp}')
                
                if(precio == tp):

                    print('Entrada ganada')
                    archivo.write(f'Ganada, Entrada {rangesEstategia.rangoCompraA}, SL {rangesEstategia.rangoCompraB}, TP {rangesEstategia.rangoVentaA}\n')
                    orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
                    # print(orderBook)
                    rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
                    print('-------------------------------')
                    print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
                    print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
                    print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
                    print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
                    break
                if(precio == sl):

                    print('Entrada perdida')
                    archivo.write(f'Perdida, Entrada {rangesEstategia.rangoCompraA}, SL {rangesEstategia.rangoCompraB}, TP {rangesEstategia.rangoVentaA}\n')
                    orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
                    # print(orderBook)
                    rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
                    print('-------------------------------')
                    print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
                    print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
                    print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
                    print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
                    break
                
                time.sleep(1)

    # if(tipoDeEntrada == 'short'):

        # ticker = client.get_symbol_ticker(symbol=symbol)
        # precio = float(ticker['price'])

        if(precio == rangesEstategia.rangoVentaA):
        
            print(f'Abri una entrada en short en el precio {rangesEstategia.rangoVentaA}, con un SL en {rangesEstategia.rangoVentaB} y TP en {rangesEstategia.rangoCompraA}')

            tp = rangesEstategia.rangoCompraA
            sl = rangesEstategia.rangoVentaB
            
            while(1):

                ticker = client.get_symbol_ticker(symbol=symbol)
                precio = float(ticker['price'])
                print(f'precioActual = {precio}, SL = {sl}, TP = {tp}')

                if(precio == tp):

                    print('Entrada ganada')
                    archivo.write(f'Ganada, Entrada {rangesEstategia.rangoVentaA}, SL {rangesEstategia.rangoVentaB}, TP {rangesEstategia.rangoCompraA}\n')
                    orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
        # print(orderBook)
                    rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
                    print('-------------------------------')
                    print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
                    print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
                    print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
                    print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
                    break
                if(precio == sl):

                    print('Entrada perdida')
                    archivo.write(f'Perdida, Entrada {rangesEstategia.rangoVentaA}, SL {rangesEstategia.rangoVentaB}, TP {rangesEstategia.rangoCompraA}\n')
                    orderBook = orderBookController.getTotalLibro(symbol,depth,exchange)
                    # print(orderBook)
                    rangesEstategia = rangeBookController.getRangoEstrategia(orderBook)
                    
                    print('-------------------------------')
                    print(f'Precio: {rangesEstategia.rangoCompraA} cantidad: {rangesEstategia.cantidadCompraA}')
                    print(f'Precio: {rangesEstategia.rangoCompraB} cantidad: {rangesEstategia.cantidadCompraB}')
                    print(f'Precio: {rangesEstategia.rangoVentaA} cantidad: {rangesEstategia.cantidadVentaA}')
                    print(f'Precio: {rangesEstategia.rangoVentaB} cantidad: {rangesEstategia.cantidadVentaB}')
                    break
                
                time.sleep(1)

    time.sleep(1)

# TENGO PENSADO EN METER ESTE FRAGMENTO DE CODIGO EN LA POSICION ABIERTA
def longShort(dolar_buy_a,dolar_buy_b,dolar_sell_a,dolar_sell_b):

    if(abs((dolar_buy_a - dolar_buy_b)) < abs((dolar_sell_b - dolar_sell_a))):

        print("El precio de compra es más viable")
        return 'long'

    if(abs((dolar_sell_b - dolar_sell_a)) < abs((dolar_buy_a - dolar_buy_b))):

        print("El precio de venta es mas viable")
        return 'short'
    
if __name__ == "__main__":
    
    inicio = time.time()
    main()
    fin = time.time()

    print(f'El tiempo total del programa fue de: {fin - inicio}')