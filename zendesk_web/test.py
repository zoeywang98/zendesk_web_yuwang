import pytest
from zendesk_web.api import *

def test_get_ticket_list():
    ticket_list = get_ticket_list()
    assert len(ticket_list) == 100

def test_get_ticket_detail():
    ticket_detail = get_ticket_detail(1)
    assert ticket_detail['subject'] == 'Sample ticket: Meet the ticket'

def test_get_ticket_user_info():
    detail = get_ticket_detail(1)
    user = get_ticket_user_info(detail['requester_id'])
    assert user['name'] == 'The Customer'