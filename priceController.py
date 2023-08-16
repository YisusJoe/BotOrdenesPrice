import sys
sys.path.append('/home/yisusjoe/projects/binance/Model')
import orderBookModel

def rangosVenta(symbol,depth,exchange):

    asks,down_book_sell, up_book_sell = orderBookModel.orderBook(symbol,depth,exchange,1)
    range_min_sell = float(down_book_sell[:5])
    range_max_sell = float(up_book_sell[:5])
    # print(range_min_sell,range_max_sell)
    return asks,range_min_sell,range_max_sell
    
def rangosCompra(symbol,depth,exchange):

    bids,down_book_buy, up_book_buy = orderBookModel.orderBook(symbol,depth,exchange,0)
    range_min_buy = float(down_book_buy[:5])
    range_max_buy = float(up_book_buy[:5])
    # print(range_min_buy,range_max_buy)
    return bids,range_min_buy,range_max_buy

def precioVenta(symbol,depth,exchange):

    asks,range_min_sell,range_max_sell = rangosVenta(symbol,depth,exchange)
    dolar_sell_a, quantity_sell_a = orderBookModel.bookPrice(range_min_sell,range_max_sell,asks,0.001,1)
    dolar_sell_b, quantity_sell_b = orderBookModel.bookPrice(range_min_sell,range_max_sell,asks,0.01,1)
    print(quantity_sell_a,dolar_sell_a)
    print(quantity_sell_b,dolar_sell_b)
    return quantity_sell_a,dolar_sell_a

def precioCompra(symbol,depth,exchange):

    bids,range_min_buy,range_max_buy = rangosCompra(symbol,depth,exchange)
    dolar_buy_a, quantity_buy_a = orderBookModel.bookPrice(range_min_buy,range_max_buy,bids,0.001,0)
    dolar_buy_b, quantity_buy_b = orderBookModel.bookPrice(range_min_buy,range_max_buy,bids,0.01,0)
    print(quantity_buy_a,dolar_buy_a)
    print(quantity_buy_b,dolar_buy_b)
    return quantity_buy_a,dolar_buy_a

def longShort(dolar_buy_a,dolar_buy_b,dolar_sell_a,dolar_sell_b):

    if(abs((dolar_buy_a - dolar_buy_b)) < abs((dolar_sell_b - dolar_sell_a))):

        print("El precio de compra es más viable")

    if(abs((dolar_sell_b - dolar_sell_a)) < abs((dolar_buy_a - dolar_buy_b))):

        print("El precio de venta es mas viable")