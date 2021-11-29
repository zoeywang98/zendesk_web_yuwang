from copy import copy

import requests
from .settings import *

email = EMAIL
token = TOKEN

#get ticket list using email and token
def get_ticket_list():
    r = requests.get('https://zccyuwang.zendesk.com/api/v2/tickets.json', auth=(email, token))
    ticket_list = r.json()['tickets']
    return ticket_list

#get ticket detail using email and token, use id to call the api
def get_ticket_detail(id):
    r = requests.get('https://zccyuwang.zendesk.com/api/v2/tickets/{0}.json'.format(id), auth=(email, token))
    return r.json()['ticket']

#get user detail using email and token, use id to call the api
def get_ticket_user_info(id):
    r = requests.get('https://zccyuwang.zendesk.com/api/v2/users/{0}.json'.format(id), auth=(email, token))
    return r.json()['user']