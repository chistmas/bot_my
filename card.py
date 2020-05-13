import random
import os.path
import json

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

def subtracting_from_card(bot,telegram_id,number,amount):
    file_client = f'.\\storage\\{telegram_id}.json'
    with open(file_client,'w') as file:
        client = json.load(file)
        card = client['cards']
        for item in card.item():
            if number == item[0]:
                item[1]['amount'] -= amount