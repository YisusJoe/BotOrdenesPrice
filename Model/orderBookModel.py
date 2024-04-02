
from binance.client import Client

api_key = '<tu clave API>'
api_secret = '<tu clave secreta>'
client = Client(api_key,api_secret)

class MdlLibro:

    def __init__(self,symbol,limit):
        self.ordenesTotales = client.futures_order_book(symbol=symbol, limit=limit)
        self.ordenesCompra = 0
        self.ordenesVenta = 0

    def getTotalLibro(self):
        ventas = self.getOrdenesVentas()
        compras = self.getOrdenesCompras()

        total = {"bids" : compras, "asks" : ventas}

        return total

    def getOrdenesCompras(self):
        return self.ordenesTotales['bids']

    def getOrdenesVentas(self):
        return self.ordenesTotales['asks']
