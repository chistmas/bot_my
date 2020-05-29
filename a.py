import os.path
import json
from pylab import figure, axes, pie, title, show
from matplotlib import pyplot as plt

def ris_in(telegram_id):
    file_client = f'.\\pay\\{telegram_id}.json' 
    if os.path.exists(file_client):
        with open(file_client) as file:
            client = json.load(file)

    
    date = client['date']
    ar = []
    co = []
    l = 0
    for elem in date:
        if date[elem]['type_of'] == 'internet':
            ar.append(date[elem]['amount'])
            l += 1
            co.append(l)
    
    # Make a square figure and axes
    fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
    ax.plot(co, ar)
    fig.savefig('to.png')   # save the figure to file
    plt.close(fig)

def ris_ph(telegram_id):
    file_client = f'.\\pay\\{telegram_id}.json' 
    if os.path.exists(file_client):
        with open(file_client) as file:
            client = json.load(file)

    
    date = client['date']
    ar = []
    co = []
    l = 0
    for elem in date:
        if date[elem]['type_of'] == 'phone':
            ar.append(date[elem]['amount'])
            l += 1
            co.append(l)
    if len(co)==1:
        fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
        ax.scatter(co[0], ar[0], s=1000)
        fig.savefig('to.png')   # save the figure to file
        plt.close(fig)
    else:
        # Make a square figure and axes
        fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
        ax.plot(co, ar)
        fig.savefig('to.png')   # save the figure to file
        plt.close(fig)
