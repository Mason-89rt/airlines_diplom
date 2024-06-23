from db.DBmanager import base_manager
from endpoints.models import StatusFlight


def get_gate(status: StatusFlight):
    res = base_manager.execute("""select name from gate 
        inner join flights on flights.id_gate = gate.id
        inner join route on route.id = flights.id_route
        inner join directive on directive.id = route.id_directive
        inner join time_route on time_route.id_route = route.id
        where directive.from_directive = ?""", args=(status.from_,))
    return res
