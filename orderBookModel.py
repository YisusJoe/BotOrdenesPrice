from binance.client import Client

api_key = '<tu clave API>'
api_secret = '<tu clave secreta>'
client = Client(api_key,api_secret)

def orderBook(symbol,depth,exchange,flag):

    order_book = client.futures_order_book(symbol=symbol, depth=depth, exchange=exchange)

    if(flag == 0):
        
        bids = sorted(order_book['bids'])
        down_book_buy = min(bids)[0]
        up_book_buy = max(bids)[0]
        return bids,down_book_buy,up_book_buy
    else:
        asks = order_book['asks']
        down_book_sell = min(asks)[0]
        up_book_sell = max(asks)[0]
        return asks,down_book_sell,up_book_sell

def bookPrice(range_min,range_max,book,gap,flag):

    price = []
    quantity = []
    while range_min <= range_max:

        allPrice = 0
        for ubook in book:

            if(float(ubook[0]) > (range_min) and float(ubook[0]) <= (range_min+gap) and flag == 0):

                allPrice += float(ubook[1])
            if(float(ubook[0]) > (range_min-gap) and float(ubook[0]) <= (range_min) and flag == 1):

                allPrice += float(ubook[1])

        price.append(range_min)
        quantity.append(allPrice)
        range_min += gap

    max_quantity = max(quantity)
    index_price = quantity.index(max_quantity)

    return round(price[index_price],3), max_quantity
    
    if flag == 0:
        print(f'The max order buy is {max_quantity} in the price {round(price[index_price],3)}')
    else:
        print(f'The max order sell is {max_quantity} in the price {round(price[index_price],3)}')
