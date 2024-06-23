from fastapi import APIRouter
from endpoints.models import Directive
from resolvers.ticket_time import get_ticket_time

router = APIRouter()


# @router.get('/ticket_time_night')
# def get_endpoint(endpoint: Directive):
#     return get_ticket_time_night(endpoint)
#
#
# @router.get('/ticket_time_day')
# def get_endpoint(endpoint: Directive):
#     return get_ticket_time_day(endpoint)


@router.get('/ticket_time')
def get_endpoint(endpoint: Directive):
    return get_ticket_time(endpoint)
