import Controller.orderBookController as orderBookController

class rangosEstrategia:

    def __init__(self):

        self.rangoCompraA = 0.0
        self.rangoCompraB = 0.0
        self.rangoVentaA = 0.0
        self.rangoVentaB = 0.0
        self.cantidadCompraA = 0.0
        self.cantidadCompraB = 0.0
        self.cantidadVentaA = 0.0
        self.cantidadVentaB = 0.0
        self.rangeMaxCompra = 0.0
        self.rangeMinCompra = 0.0
        self.rangeMaxVenta = 0.0
        self.rangeMinVenta = 0.0

    def getRangosEstrategia(self, orderBook):

        # print(f'Entre a obtener los rangos del orderBook')

        self.rangoCompraA, self.cantidadCompraA = self.rangosAB(orderBook['bids'], self.rangeMinCompra, self.rangeMaxCompra, 0.001, 0)
        self.rangoCompraB, self.cantidadCompraB = self.rangosAB(orderBook['bids'], self.rangeMinCompra, self.rangeMaxCompra, 0.01, 0)
        self.rangoVentaA, self.cantidadVentaA = self.rangosAB(orderBook['asks'], self.rangeMinVenta, self.rangeMaxVenta, 0.001, 1)
        self.rangoVentaB, self.cantidadVentaB = self.rangosAB(orderBook['asks'], self.rangeMinVenta, self.rangeMaxVenta, 0.01, 1)

    def rangosAB(self, orderBook, range_min, range_max, gap, flag):

        price = []
        quantity = []
        while range_min <= range_max:

            allPrice = 0
            for ubook in orderBook:

                if(float(ubook[0]) > (range_min) and float(ubook[0]) <= (range_min+gap) and flag == 0):

                    allPrice += float(ubook[1])
                if(float(ubook[0]) > (range_min-gap) and float(ubook[0]) <= (range_min) and flag == 1):

                    allPrice += float(ubook[1])

            price.append(range_min)
            quantity.append(allPrice)
            range_min += gap

        max_quantity = max(quantity)
        index_price = quantity.index(max_quantity)

        return round(price[index_price],3),  max_quantity

    def rangeMaxMin(self,orderBook):

        compras = sorted(orderBook['bids'])
        ventas = orderBook['asks']

        self.rangeMaxCompra = float(max(compras)[0])
        self.rangeMinCompra = float(min(compras)[0])
        self.rangeMaxVenta = float(max(ventas)[0])
        self.rangeMinVenta = float(min(ventas)[0])
        # down_book_sell = min(self.ordenesVenta)[0]
        # up_book_sell = max(self.ordenesVenta)[0]