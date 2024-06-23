from fastapi import APIRouter
from endpoints.models import (SeatBookCreate, IDSeatBook, PassengerId)
from resolvers.purchased_ticket import (buy_insert, seat_buy, visible_buy_ticket_on_my_flights)

router = APIRouter()


@router.get('/seat_name_buy')
def get_endpoint(endpoint: IDSeatBook):
    return seat_buy(endpoint)


@router.post('/buy_ticket_create')
def post_endpoint(endpoint: SeatBookCreate):
    return buy_insert(endpoint)


@router.get('/visible_buy_ticket_book')
def post_endpoint(endpoint: PassengerId):
    return visible_buy_ticket_on_my_flights(endpoint)
