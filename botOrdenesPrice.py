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

symbols = ['XRPUSDT','MATICUSDT']
# symbol = 'XRPUSDT'
# symbol = 'MATICUSDT'
depth = 10 # profundidad de 10 niveles
limit_A = 100
limit_B = 1000
exchange = 'binance_futures' # intercambio de futuros de Binance
  

# TENGO PENSADO EN METER ESTE FRAGMENTO DE CODIGO EN LA POSICION ABIERTA
def dosaUno(symbol, dolar_buy_a,dolar_buy_b,dolar_sell_a,dolar_sell_b):

    # print(dolar_sell_b/dolar_sell_a)
    # print(dolar_buy_a/dolar_buy_b)
    disCompras_AB = ((dolar_buy_a/dolar_buy_b) - 1) * 100
    disCompras_AB = round(disCompras_AB,2)
    disVentas_AB = ((dolar_sell_b/dolar_sell_a) - 1) * 100
    disVentas_AB = round(disVentas_AB,2)
    dis_compraventa_A = ((dolar_sell_a/dolar_buy_a) - 1) * 100
    dis_compraventa_A = round(dis_compraventa_A,2)

    # print(f'Distancia de venta A a B: {disVentas_AB}')
    # print(f'Distancia de compra y venta A: {dis_compraventa_A}')
    # print(f'Distancia de compra A a B: {disCompras_AB}')

    if( ((dis_compraventa_A >= 1.8*(disCompras_AB)) and disCompras_AB > 0.8) and ((dis_compraventa_A >= 1.8*(disVentas_AB)) and disVentas_AB > 0.8) ):
        # print(f'{symbol} LONG Y SHORT')
        if(disVentas_AB < disCompras_AB):
            print(f'SHORT {symbol} E: {dolar_sell_a} SL: {dolar_sell_b} TP: {dolar_buy_a} TP2: {dolar_buy_b}')
            return ['SHORT',dolar_sell_a, dolar_sell_b, dolar_buy_a]
        
        if(disCompras_AB < disVentas_AB):
            print(f'LONG  {symbol} E: {dolar_buy_a} SL: {dolar_buy_b} TP: {dolar_sell_a} TP2: {dolar_sell_b}')
            return ['LONG',dolar_buy_a, dolar_buy_b, dolar_sell_a]

    if(dis_compraventa_A >= 1.8*(disCompras_AB) and disCompras_AB > 0.8):
        # print(f'dis compraA ventaA: {dis_compraventa_A}, disCompras_AB: {disCompras_AB}; 1.8disCompras_AB {1.8*(disCompras_AB)}')
        print(f'LONG  {symbol} E: {dolar_buy_a} SL: {dolar_buy_b} TP: {dolar_sell_a} TP2: {dolar_sell_b}')
        return ['LONG',dolar_buy_a, dolar_buy_b, dolar_sell_a]

    if(dis_compraventa_A >= 1.8*(disVentas_AB) and disVentas_AB > 0.8):
        # print(f'dis compraA ventaA: {dis_compraventa_A}, disVentas_AB: {disVentas_AB}; 1.8disVentas_AB {1.8*(disVentas_AB)}')
        print(f'SHORT {symbol} E: {dolar_sell_a} SL: {dolar_sell_b} TP: {dolar_buy_a} TP2: {dolar_buy_b}')
        return ['SHORT',dolar_sell_a, dolar_sell_b, dolar_buy_a]

    # if(dolar_sell_b/dolar_sell_a < dolar_buy_a/dolar_buy_b):

    #     print("El precio de venta es mas viable")

    # else:

    #     print("El precio de compra es mas viable")

def getTickets():

    symbols = []
    try:
        exchange_info = client.futures_exchange_info()
        futures_symbols = [symbol['symbol'] for symbol in exchange_info['symbols']]

        # print(futures_symbols)
        for symbol in futures_symbols:
            ticker = client.futures_symbol_ticker(symbol=symbol)
                
            if(ticker):
                precio = float(ticker['price'])
                if(precio < 1):
                    # print(precio)
                    # print(ticker)
                    # print(f'El precio del activo {symbol} es: {precio}')
                    symbols.append(symbol)

        return symbols
    
    except:
        pass

def filtroEntrada(E_dosUno, symbol):
    
    try:
        ticker = client.futures_symbol_ticker(symbol=symbol)
    except:
        pass

    if(ticker):
        precio = float(ticker['price'])
    
    if(E_dosUno[0] == 'LONG'):
        # print("LONG")
        # print(Entrada)
        dis_Entrada = precio - E_dosUno[1]
        dis_Perdida = E_dosUno[3] - precio
        print(f'precio: {precio} {dis_Entrada} {dis_Perdida}')        
        
        if(dis_Entrada < dis_Perdida):
            print(f'{E_dosUno[0]} {symbol} precio: {precio} entrada: {E_dosUno[1]} dis: {dis_Entrada} EP: {E_dosUno[3]} perdida: {dis_Perdida}')
            # return E_dosUno[0], dis_Entrada, dis_Perdida
            return True
        else:
            return False
    
    if(E_dosUno[0] == 'SHORT'):
        # print("SHORT")
        # print(Entrada)
        dis_Entrada = E_dosUno[1] - precio
        dis_Perdida = precio - E_dosUno[3]
        print(f'precio: {precio} {dis_Entrada} {dis_Perdida}')
              
        if(dis_Entrada < dis_Perdida):
            print(f'{E_dosUno[0]} {symbol} precio: {precio} entrada: {E_dosUno[1]} dis: {dis_Entrada} EP: {E_dosUno[3]} perdida: {dis_Perdida}')
            # return E_dosUno[0], dis_Entrada, dis_Perdida
            return True
        else:
            return False

def logWrite(texto):
    
    fecha_actual = datetime.datetime.now()
    nombre_archivo = 'Entradas/' + fecha_actual.strftime("%Y-%m-%d.txt")
    hora_actual = fecha_actual.strftime("%H:%M:%S")
    
    archivo = open(nombre_archivo, 'a')
    archivo.write(f'{hora_actual} | {texto}\n')
    archivo.close()

def getPrice(symbol): 
    try:
        ticker = client.futures_symbol_ticker(symbol=symbol)
    
        if(ticker):
            return float(ticker['price'])
    except:
        pass
  
def main():

      
    if(getTickets()):
        inicio = time.time()
        symbols = getTickets()
        fin = time.time()
        print(f'getTickets() duro: {fin - inicio}')
        # print(symbols)
    
        for symbol in symbols:
            # print(f'Activo {symbol}')
            
            try:
                inicio = time.time()
                Obj_libro_A = Libro(symbol=symbol,limit=limit_A)
                Obj_libro_B = Libro(symbol=symbol,limit=limit_B)
                Libro_total_A = Obj_libro_A.getlibroTotal()
                Libro_total_B = Obj_libro_B.getlibroTotal()

                Obj_estrategia_A = RangosEstrategia(Libro_total_A)
                Obj_estrategia_B = RangosEstrategia(Libro_total_B)
                
                CompraBloque_A = Obj_estrategia_A.getBloqueA('bids')
                VentaBloque_A = Obj_estrategia_A.getBloqueA('asks')
                VentaBloque_B = Obj_estrategia_B.getBloqueB('asks')
                CompraBloque_B = Obj_estrategia_B.getBloqueB('bids')
                fin = time.time()
                print(f'El calculo de rangos duro: {fin - inicio}')
        
                E_dosUno = dosaUno(symbol, float(CompraBloque_A[0]), float(CompraBloque_B[0]), float(VentaBloque_A[0]), float(VentaBloque_B[0]))
                F_Entrada = filtroEntrada(E_dosUno, symbol = symbol)
                # print(f'{F_Entrada}\n')
                # print(f'{symbol} {E_dosUno[0]} E: {E_dosUno[1]} SL: {E_dosUno[2]} TP: {E_dosUno[3]}')

                print(f'B_Venta {VentaBloque_B}')
                print(f'A_Venta {VentaBloque_A}')
                print(f'A_Compra {CompraBloque_A}')
                print(f'B_Compra {CompraBloque_B}\n')
                
                tipoEntrada = E_dosUno[0]
                Entrada = E_dosUno[1]
                StopLoss = E_dosUno[2]
                TakeProfit = E_dosUno[3]

                while(E_dosUno and F_Entrada):
                    
                    precio = getPrice(symbol)
                    
                    print(f'{symbol} | {tipoEntrada} | {precio} E: {Entrada} TP: {TakeProfit} SL: {StopLoss}')
                    # logWrite(f'Encontre {tipoEntrada} | {precio} E: {Entrada} TP: {TakeProfit} SL: {StopLoss}')

                    if(tipoEntrada == 'LONG'):
                        
                        if(precio <= Entrada):
                            
                            print('Entre a la operacion')
                            logWrite(f'{symbol} | {tipoEntrada} | Entre a la operacion en {Entrada}, SL: {StopLoss} y TP: {TakeProfit}')
                            
                            while(True):
                                
                                precio = getPrice(symbol)
                                
                                print(f'{symbol} | {tipoEntrada} | {precio} E: {Entrada} TP: {TakeProfit} SL: {StopLoss}')
                                
                                if(precio >= TakeProfit):
                                    
                                    print("Gane la operacion")
                                    logWrite(f'Gane la operacion, llegue al TP: {TakeProfit}, entre en {Entrada}')
                                    break
                                
                                if(precio <= StopLoss):
                                    
                                    # print("Perdi la operacion")
                                    # logWrite(f'Perdi la operacion, llegue al SL: {StopLoss}, entre en {Entrada}\n')
                                    Sl2 = StopLoss - (StopLoss * 0.01)

                                    while(True):
                                        
                                        precio = getPrice(symbol)

                                        print("Segunda entrada")
                                        logWrite(f'Segunda entrada {StopLoss}')
                                        
                                        if(precio >= TakeProfit):
                                    
                                            print("Gane la operacion")
                                            logWrite(f'Gane la operacion, llegue al TP: {TakeProfit}, entre en {StopLoss} con SL2 en {Sl2}')
                                            break

                                        if(precio <= Sl2):
                                    
                                            print("Perdi la operacion")
                                            logWrite(f'Perdi la operacion, llegue al SL2: {Sl2}, entre en {Entrada}')
                                            break

                                    break
                            
                            break
                                    

                        if(precio >= TakeProfit):
                            
                            print('No pude entrar a la operacion')
                            logWrite(f'{symbol} | {tipoEntrada} | Llegue a {TakeProfit} sin entrar a la operacion en {Entrada}')
                            break
                        
                    if(tipoEntrada == 'SHORT'):
                        if(precio >= Entrada):
                            
                            print('Entre a la operacion')
                            logWrite(f'{symbol} | {tipoEntrada} | Entre a la operacion en {Entrada}, SL: {StopLoss} y TP: {TakeProfit}')
                            
                            while(True):
                                
                                precio = getPrice(symbol)
                                
                                print(f'{symbol} | {tipoEntrada} | {precio} E: {Entrada} TP: {TakeProfit} SL: {StopLoss}')
                                
                                if(precio <= TakeProfit):
                                    
                                    print("Gane la operacion")
                                    logWrite(f'Gane la operacion, llegue al TP: {TakeProfit}, entre en {Entrada}')
                                    break
                                
                                if(precio >= StopLoss):
                                    
                                    # print("Perdi la operacion")
                                    # logWrite(f'Perdi la operacion, llegue al SL: {StopLoss}, entre en {Entrada}')
                                    Sl2 = StopLoss + (StopLoss * 0.01)

                                    while(True):
                                    
                                        precio = getPrice(symbol)

                                        print("Segunda entrada")
                                        logWrite(f'Segunda entrada {StopLoss}')
                                        
                                        if(precio <= TakeProfit):
                                    
                                            print("Gane la operacion")
                                            logWrite(f'Gane la operacion, llegue al TP: {TakeProfit}, entre en {StopLoss} con SL2 en {Sl2}')
                                            break

                                        if(precio >= Sl2):
                                    
                                            print("Perdi la operacion")
                                            logWrite(f'Perdi la operacion, llegue al SL2: {Sl2}, entre en {Entrada}')
                                            break
                                    break
                                
                            break

                        if(precio <= TakeProfit):
                            
                            print('No pude entrar a la operacion')
                            logWrite(f'{symbol} | {tipoEntrada} | Llegue a {TakeProfit} sin entrar a la operacion en {Entrada}')
                            break
                        
            except:
                pass
        # except Exception as error:
        #     print(f'error: {error}')

if __name__ == "__main__":
    
    inicio = time.time()
    while(True):
        main()
    fin = time.time()

    print(f'El tiempo total del programa fue de: {fin - inicio}')