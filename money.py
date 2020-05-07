import requests as res
import json

def cur_in(currency='USD'):
    response = res.get('https://belarusbank.by/api/kursExchange?city=Минск')
    curs = json.loads(response.text)
    curr = curs[0]
    usd_in = curr['USD_in']
    eur_in = curr['EUR_in']
    rub_in = curr['RUB_in']
    curr = f"USD:{usd_in} EUR:{eur_in} RUB:{rub_in}"
    return curr

def cur_out(currency='USD'):
     response = res.get('https://belarusbank.by/api/kursExchange?city=Минск')
     curs = json.loads(response.text)
     curr = curs[1]
     usd_out = curr['USD_out']
     eur_out = curr['EUR_out']
     rub_out = curr['RUB_out']
     curr = f"USD:{usd_out} EUR:{eur_out} RUB:{rub_out}"
     return curr
 
