from fastapi import APIRouter
from endpoints.models import DirectiveFromTo, FlightsCreate, FlightsUpdate, FlightsShow
from db.DBmanager import base_manager

router = APIRouter()


def get_flights():
    res = base_manager.execute("""SELECT * from flights""", args=())
    flights = []
    for i in res:
        flights.append(FlightsShow(id_=i[0], id_flights_status=i[1], id_route=i[2], id_time_=i[3], id_date_=i[4],
                                   id_plane=i[5], id_gate=i[6]))
    return flights


def get_gate(directive: DirectiveFromTo):
    res = base_manager.execute("""SELECT gate.name from gate
    inner join flights on gate.id = flights.id_gate
    WHERE flights.id_route = (select route.id from route
    inner join directive on directive.id = route.id_directive
    where directive.from_directive = ?
    AND directive.to_directive =?)""", args=(directive.from_directive, directive.to_directive))
    return res


def get_number_flight(directive: DirectiveFromTo):
    res = base_manager.execute("""SELECT flights.id from flights
    INNER JOIN route ON flights.id_route = route.id
    inner join directive on directive.id = route.id_directive
    WHERE directive.from_directive = ? and to_directive = ?""", args=(directive.from_directive, directive.to_directive))
    return res


def insert_flights(flights: FlightsCreate):
    time_start_str = flights.time_start.strftime('%H:%M')
    time_end_str = flights.time_end.strftime('%H:%M')
    res = base_manager.execute("""INSERT INTO flights(id_flights_status, id_route, id_time_, id_date_, id_plane, id_gate)
SELECT (SELECT flights_status.id from flights_status where flights_status.status = ?) as status_flights, 
(SELECT route.id from route inner join directive on directive.id = route.id_directive where directive.from_directive = ? 
and directive.to_directive = ?) as route, 
(SELECT time_route.id from time_route where time_route.time_start = ? and time_route.time_end = ?) as time, 
(SELECT date_route.id from date_route where date_route.date_start = ?) as date,
(SELECT plane.id from plane inner join model on model.id = plane.id_model where model.name = ?) as model,
(SELECT gate.id from gate where gate.name = ?) as gate""", args=(flights.flights_status, flights.from_directive,
                                                                 flights.to_directive, time_start_str,
                                                                 time_end_str, flights.date_, flights.plane_model,
                                                                 flights.gate))
    return res


def update_flights(flights: FlightsUpdate):
    time_start_str = flights.time_start.strftime('%H:%M')
    time_end_str = flights.time_end.strftime('%H:%M')
    res = base_manager.execute("""UPDATE flights 
    SET
    id_flights_status = (SELECT flights_status.id FROM flights_status WHERE flights_status.status = ?),
    id_route = (
        SELECT route.id 
        FROM route 
        INNER JOIN directive ON directive.id = route.id_directive 
        WHERE directive.from_directive = ? AND directive.to_directive = ?
    ),
    id_time_ = (
        SELECT time_route.id 
        FROM time_route 
        WHERE time_route.time_start = ? AND time_route.time_end = ?
    ),
    id_date_ = (
        SELECT date_route.id 
        FROM date_route 
        WHERE date_route.date_start = ?
    ),
    id_plane = (
        SELECT plane.id 
        FROM plane 
        INNER JOIN model ON model.id = plane.id_model 
        WHERE model.name = ?
    ),
    id_gate = (SELECT gate.id FROM gate WHERE gate.name = ?)
WHERE 
    flights.id = ?;""", args=(flights.flights_status, flights.from_directive,
                              flights.to_directive, time_start_str,
                              time_end_str, flights.date_, flights.plane_model,
                              flights.gate, flights.id_))
    return res
