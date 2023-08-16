from binance.client import Client
import requests
import time

import orderBookModel
import priceController

api_key = '<tu clave API>'
api_secret = '<tu clave secreta>'
client = Client(api_key, api_secret)

symbol = 'MATICUSDT'
depth = 5000 # profundidad de 10 niveles
exchange = 'binance_futures' # intercambio de futuros de Binance

order_book = client.futures_order_book(symbol=symbol, depth=depth, exchange=exchange)

# bids = sorted(order_book['bids'])
# asks = order_book['asks']

def funcion1():
    
    print(symbol)
    gap = 0.001
    priceController.precioVenta(symbol,depth,exchange,gap)
    priceController.precioCompra(symbol,depth,exchange,gap)
  
def main():

    print(symbol)
    Va,Vb = priceController.precioVenta(symbol,depth,exchange)
    Ca,Cb = priceController.precioCompra(symbol,depth,exchange)

    priceController.longShort(Ca,Cb,Va,Vb)

    time.sleep(1)

    
if __name__ == "__main__":
    
    inicio = time.time()
    main()
    fin = time.time()

    print(f'El tiempo total del programa fue de: {fin - inicio}')