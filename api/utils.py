from datetime import datetime

def amount_to_pay(discount, price):
    result = price - (price/100*discount)
    return round(result, 2)


def str_to_date_converter(date_str):
    if len(date_str) <= 10:
        data = datetime.strptime(date_str, "%d-%m-%Y")
    else:
        data = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
    return data

