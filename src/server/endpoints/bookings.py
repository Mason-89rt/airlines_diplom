from fastapi import APIRouter
from endpoints.models import (SearchBookingTicketInfo, Directive, SeatBookCreate, IDSeatBook, SeatBookDelete,
                              PassengerId, SeatBookDeleteOnID)
from resolvers.bookings import (id_all_in_bookings_seat, visible_ticket_on_my_flights, seat_delete_on_id,
                                seat_book, seat_insert, seat_delete, id_plane)

router = APIRouter()


@router.get('/seat_name_book')
def get_endpoint(endpoint: IDSeatBook):
    return seat_book(endpoint)


@router.post('/booked_ticket_create')
def post_endpoint(endpoint: SeatBookCreate):
    return seat_insert(endpoint)


@router.delete('/seat_name_delete')
def post_endpoint(endpoint: SeatBookDelete):
    return seat_delete(endpoint)


@router.delete('/seat_name_delete_id')
def post_endpoint(endpoint: SeatBookDeleteOnID):
    return seat_delete_on_id(endpoint)


@router.get('/id_plane')
def get_endpoint(endpoint: Directive):
    return id_plane(endpoint)


@router.get('/id_ticket_bookings_seat')
def post_endpoint(endpoint: SearchBookingTicketInfo):
    return id_all_in_bookings_seat(endpoint)


@router.get('/visible_ticket_book')
def post_endpoint(endpoint: PassengerId):
    return visible_ticket_on_my_flights(endpoint)
