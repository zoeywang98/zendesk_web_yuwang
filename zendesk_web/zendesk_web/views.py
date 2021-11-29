from django.http import HttpResponse
from . import api
from django.shortcuts import render
from django.core.paginator import Paginator

def ticket_list(request):
    ticket_list = api.get_ticket_list()
    cur_page_num = request.GET.get('cur_page_num', 1)
    paginator = Paginator(ticket_list, 25)
    page = paginator.page(int(cur_page_num))
    context = {
        'page': page,
        'total_page': paginator.num_pages,
        'count': paginator.per_page
    }
    return render(request, 'ticket_list.html', context)

def ticket_detail(request, id):
    ticket = api.get_ticket_detail(id)
    user = api.get_ticket_user_info(ticket['requester_id'])
    assignee = api.get_ticket_user_info(ticket['assignee_id'])
    context = {
        'ticket': ticket,
        'user': user,
        'assignee': assignee
    }
    return render(request, 'ticket_detail.html', context)