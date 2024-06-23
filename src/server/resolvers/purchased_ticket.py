from fastapi import APIRouter
from endpoints.models import (SeatBookCreate, IDSeatBook, PassengerId, )
from db.DBmanager import base_manager

router = APIRouter()


def seat_buy(directive: IDSeatBook):
    time_start_str = directive.time_start.strftime('%H:%M')
    time_end_str = directive.time_end.strftime('%H:%M')
    res = base_manager.execute("""SELECT id_seat from buy_ticket
inner join seat on seat.id = buy_ticket.id_seat
inner join flights on flights.id = buy_ticket.id_flights
inner join route on route.id = flights.id_route
inner join directive on route.id_directive = directive.id
inner join date_route on date_route.id = flights.id_date_
inner join time_route on time_route.id = flights.id_time_
where from_directive = ? AND to_directive = ? and date_route.date_start = ? and time_route.time_start = ? 
and time_route.time_end = ? 
and seat.name = ?""", args=(directive.from_directive, directive.to_directive, directive.date_, time_start_str,
                            time_end_str, directive.seat_name))
    return res


def buy_insert(directive: SeatBookCreate):
    date_str = directive.date_.strftime('%Y-%m-%d')
    res = base_manager.execute("""insert into buy_ticket(id_passenger, id_flights, id_seat) 
        SELECT ( SELECT passenger.id from passenger inner join user on user.id = passenger.id_user where 
        passenger.id_user = ?) as id_passenger, flights.id as flights_id, seat.id as seat_id from flights 
    inner join route on route.id = flights.id_route
    inner join directive on directive.id = route.id_directive
    INNER JOIN date_route ON flights.id_date_ = date_route.id
    inner join plane on plane.id = flights.id_plane
    inner join seat on seat.id_plane = plane.id
    where from_directive = ? AND to_directive = ? and date_route.date_start = ? and seat.name = ?""",
                               args=(directive.id_passenger, directive.from_directive, directive.to_directive,
                                     date_str, directive.seat_name))
    return res


def visible_buy_ticket_on_my_flights(directive: PassengerId):
    res = base_manager.execute("""SELECT directive.from_directive, directive.to_directive, date_route.date_start,  
    time_route.time_start, time_route.time_end, seat.name, passenger.name, passenger.surname, flights.id, gate.name, class.name
    FROM buy_ticket
    INNER JOIN flights ON buy_ticket.id_flights = flights.id
    INNER JOIN route ON route.id = flights.id_route
    INNER JOIN seat ON seat.id = buy_ticket.id_seat
    INNER JOIN directive ON directive.id = route.id_directive
    INNER JOIN date_route ON date_route.id = flights.id_date_
    INNER JOIN time_route ON time_route.id = flights.id_time_
    INNER JOIN passenger ON passenger.id = buy_ticket.id_passenger
    inner join class on class.id = seat.id_class
	inner join gate on gate.id = flights.id_gate
    WHERE (select id_user from passenger where id_user = ?);""", args=(directive.id,))
    return res
