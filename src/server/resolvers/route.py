from endpoints.models import Directive, DirectiveFromTo
from db.DBmanager import base_manager


def get_route(directive: Directive):
    res = base_manager.execute("""SELECT flights.id FROM flights 
							   inner join route on route.id = flights.id_route
							   inner join directive on directive.id = route.id_directive
                               INNER JOIN date_route ON date_route.id = flights.id_date_ 
                               WHERE directive.from_directive = ?
                               AND directive.to_directive = ?
                               and date_route.date_start = ?""",
                               args=(directive.from_directive, directive.to_directive, directive.date_))
    return res


def route_exist(directive: DirectiveFromTo):
    res = base_manager.execute("""SELECT * FROM directive 
                               WHERE directive.from_directive = ?
                               AND directive.to_directive = ?""",
                               args=(directive.from_directive, directive.to_directive))
    return res
