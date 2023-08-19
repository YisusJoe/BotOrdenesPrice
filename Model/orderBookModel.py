
from binance.client import Client

api_key = '<tu clave API>'
api_secret = '<tu clave secreta>'
client = Client(api_key,api_secret)

class orderBook:

    def __init__(self):

        self.ordenesTotales = ''
        self.ordenesCompra = ''
        self.ordenesVenta = ''

    def getTotalLibro(self,symbol,depth,exchange):

        print('Obtive el libro total de ordenes')
        self.ordenesTotales = client.futures_order_book(symbol=symbol, depth=depth, exchange=exchange)

    def getOrdenesCompra(self):

        print('Obtuve ordenes de compras')
        self.ordenesCompra = sorted(self.ordenesTotales['bids'])
        # down_book_buy = min(bids)[0]
        # up_book_buy = max(bids)[0]
        # # return bids,down_book_buy,up_book_buy

    def getOrdenesVentas(self):

        print('Obtuve ordenes de ventas')
        self.ordenesVenta = self.ordenesTotales['asks']
        # down_book_sell = min(self.ordenesVenta)[0]
        # up_book_sell = max(self.ordenesVenta)[0]
        # # return asks,down_book_sell,up_book_sell
