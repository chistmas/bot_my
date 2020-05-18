import random
import os.path
import json

user_card = {}
class Card:
    def __init__(self,telegram_id,card_num,amount=0,currency='BY',number='0000'):
        self.telegram_id = telegram_id
        self.amount=amount
        self.currency = currency
        self.card_num = card_num
        self.number = number
        
        
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

def get_cards(telegram_id):
    file_client = f'.\\storage\\{telegram_id}.json' 
    if os.path.exists(file_client):
        with open(file_client, 'r') as file:
            client = json.load(file)
            
        return client['cards']
    return {'error': 'You don\'t have any cards. Make one, please.'}