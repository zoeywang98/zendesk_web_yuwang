# ZenDesk Mobile Ticket Viewer

## Environment

- Backend: Python3.8(3.6+ is ok) django == 2.1.8
- Frontend: javaScript jQuery Bootstrap

## How to Run

### Backend Server
```shell
cd ./zendesk_web
python manage.py runserver
```
### Frontend
- http://127.0.0.1:8000/ticket/list
  - show the list of tickets
  - display id, subject, type, update time, priority and status
  - the subject field would have a link to get the ticket detail
  - display 25 tickets one page, support paging
- http://127.0.0.1:8000/ticket/detail/{id}
  - show the detail of tickets and its requester
  - display requester's photo, name, assignee's email, ticket's subject, description and tags
  - use id to identify one specific ticket
  - have a button to get back to the tickets list


## Design
### Backend Server
- use email and token to authenticate the account to get tickets
- design RESTful APIs
  - /ticket/list
  - /ticket/detail/{id}
- use django template to render data in backend to frontend
- use django pagination to do the pagination in backend

### Frontend
- use jQuery to do the pagination in the frontend
- use Bootstrap to render the frontend page

## Test
test.py have unit test for api calls.