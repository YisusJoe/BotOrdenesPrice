# import Model.orderBookModel as orderBookModel
from Model.orderBookModel import MdlLibro 

class Libro:

    def __init__(self,symbol,limit):
        self.libroTotal = MdlLibro(symbol=symbol,limit=limit)

    def getlibroTotal(self):
        return self.libroTotal.getTotalLibro()
    
    def getVentas(self):
        return self.libroTotal.getOrdenesVentas()
    
    def getCompras(self):
        return self.libroTotal.getOrdenesCompras()
