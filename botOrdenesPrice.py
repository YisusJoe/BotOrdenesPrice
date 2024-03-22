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
# symbol = 'MATICUSDT'
depth = 10 # profundidad de 10 niveles
limit_A = 100
limit_B = 1000
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

    Obj_libro_A = Libro(symbol=symbol,limit=limit_A)
    Obj_libro_B = Libro(symbol=symbol,limit=limit_B)
    Libro_total_A = Obj_libro_A.getlibroTotal()
    Libro_total_B = Obj_libro_B.getlibroTotal()
    # Libro_ventas = Obj_libro_A.getVentas()
    # Libro_compras = Obj_libro_A.getCompras()

    Obj_estrategia_A = RangosEstrategia(Libro_total_A)
    Obj_estrategia_B = RangosEstrategia(Libro_total_B) 
    
    CompraBloque_A = Obj_estrategia_A.getBloqueA('bids')
    VentaBloque_A = Obj_estrategia_A.getBloqueA('asks')
    VentaBloque_B = Obj_estrategia_B.getBloqueB('asks')
    CompraBloque_B = Obj_estrategia_B.getBloqueB('bids')
    
    # Puntos_B = Obj_estrategia.getPuntosB()

    print(f'B_Venta {VentaBloque_B}')
    print(f'A_Venta {VentaBloque_A}')
    print(f'A_Compra {CompraBloque_A}')
    print(f'B_Compra {CompraBloque_B}')

    time.sleep(1)

if __name__ == "__main__":
    
    inicio = time.time()
    main()
    fin = time.time()

    print(f'El tiempo total del programa fue de: {fin - inicio}')