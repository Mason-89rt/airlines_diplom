from fastapi import APIRouter
from endpoints.models import Directive
from db.DBmanager import base_manager

router = APIRouter()


# def get_ticket_time_night(directive: Directive):
#     res = base_manager.execute("""SELECT DISTINCT time_route.time_start, time_route.time_end
#         FROM time_route
#         inner join flights on flights.id_time_ = time_route.id
#         WHERE flights.id_route =
#         (SELECT route.id from route inner join directive on directive.id = route.id
#         inner join flights on route.id = flights.id_route
#         inner join date_route on date_route.id = flights.id_date_
#         where from_directive=? and to_directive = ? and date_route.date_start = ?)
#         and time_route.time_start >= '00:00' AND time_route.time_start <= '04:00';""",
#                                args=(directive.from_directive, directive.to_directive, directive.date_))
#     return res
#
#
# def get_ticket_time_day(directive: Directive):
#     res = base_manager.execute("""SELECT DISTINCT time_route.time_start, time_route.time_end
#         FROM time_route
#         inner join flights on flights.id_time_ = time_route.id
#         WHERE flights.id_route =
#         (SELECT route.id from route inner join directive on directive.id = route.id
#         inner join flights on route.id = flights.id_route
#         inner join date_route on date_route.id = flights.id_date_
#         where from_directive=? and to_directive = ? and date_route.date_start = ?)
#         and time_route.time_start >= '04:00' AND time_route.time_start <= '23:59';""",
#                                args=(directive.from_directive, directive.to_directive, directive.date_))
#     return res


def get_ticket_time(directive: Directive):
    res = base_manager.execute("""SELECT DISTINCT time_route.time_start, time_route.time_end 
        FROM time_route 
        inner join flights on flights.id_time_ = time_route.id
        WHERE flights.id_route = 
        (SELECT route.id from route inner join directive on directive.id = route.id 
        inner join flights on route.id = flights.id_route 
        inner join date_route on date_route.id = flights.id_date_
        where from_directive=? and to_directive = ? and date_route.date_start = ?)""",
                               args=(directive.from_directive, directive.to_directive, directive.date_))
    return res
