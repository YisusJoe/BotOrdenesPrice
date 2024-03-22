from Model.rangeBookModel import MdlRangosEstrategia

class RangosEstrategia:

    def __init__(self,orderBook):
        self.Rangos = MdlRangosEstrategia(orderBook)
        
    def getPuntosTotales(self):
        pass

    def getBloqueA(self,cv):
        return self.Rangos.getABloque(cv)

    def getBloqueB(self,cv):
        return self.Rangos.getBBloque(cv)