import random
import os.path
import json
from datetime import datetime

user_card = {}
class Card:
    def __init__(self,telegram_id,card_num,item,amount=0,currency='BY',number='0000'):
        item = []
        self.telegram_id = telegram_id
        self.amount=amount
        self.currency = currency
        self.card_num = card_num
        self.number = number
        
def subtracting_from_card(bot,telegram_id,number,amount=10):
    file_client = f'.\\storage\\{telegram_id}.json'
    with open(file_client,'r') as file:
        client = json.load(file)
        
    card = client['cards'][number]
    
    card['amount'] -= amount
    with open(file_client, 'w') as file:
        json.dump(client, file, indent=4, sort_keys=True)
        
def new_card(telegram_id, amount=500, currency='BYR'):
    card_num = ' '.join([str(i) for i in
                         [random.randint(1000, 9999) for i in range(4)]])
    
    card = {f'{card_num}': {'currency': currency.upper(), 
                            'amount': amount
                            }
            }

    file_client = f'.\\storage\\{telegram_id}.json' 
    
    
    if os.path.exists(file_client):
        with open(file_client, 'r') as file:
            client = json.load(file)
    else:
        client = {'telegram_id': telegram_id, 
                  'cards': {}
                  }
    client['cards'].update(card)
    
    with open(file_client, 'w') as file:
        json.dump(client, file, indent=4, sort_keys=True)
        
    result = {'card_num': card_num, 
              'currency': currency.upper(), 
              'amount': amount}
    return result

def save(telegram_id, card, amount,type_of):
    now = datetime.now()
    date_time = now.strftime('%m/%d/%Y,%H:%M:%S')
    file_client = f'.\\pay\\{telegram_id}.json' 
    pay = {f'{date_time}':{'card':card, 
                      'amount': amount,
                      'type_of': type_of[0],
                      'details': type_of[1]
                      }
           }
    if os.path.exists(file_client):
        with open(file_client, 'r') as file:
            client = json.load(file)
    else:
        client = {'telegram_id': telegram_id, 
                  'date': {}
                  }
    client['date'].update(pay)
    with open(file_client, 'w') as file:
        json.dump(client, file, indent=4, sort_keys=True)
        
    result = {'card': card, 
              'date': date_time, 
              'amount': amount,
              'type_of': type_of[0],
              'details': type_of[1]
              }
    return result

def get_pay(telegram_id):
    file_client = f'.\\pay\\{telegram_id}.json' 
    if os.path.exists(file_client):
        with open(file_client, 'r') as file:
            client = json.load(file)
            
        return client['date']
    return {'error': 'You don\'t have any payments. Make one, please.'}

def get_cards(telegram_id):
    file_client = f'.\\storage\\{telegram_id}.json' 
    if os.path.exists(file_client):
        with open(file_client, 'r') as file:
            client = json.load(file)
            
        return client['cards']
    return {'error': 'You don\'t have any cards. Make one, please.'}